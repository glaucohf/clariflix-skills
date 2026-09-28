const encoder = new TextEncoder();
const COOKIE = "clariflix_access";
const ONE_DAY_SECONDS = 60 * 60 * 24;

function readCookie(request, name) {
  const match = (request.headers.get("Cookie") || "").match(new RegExp(`(?:^|;\\s*)${name}=([^;]+)`));
  return match ? match[1] : null;
}

function equal(left, right) {
  if (left.length !== right.length) return false;
  let result = 0;
  for (let index = 0; index < left.length; index += 1) result |= left.charCodeAt(index) ^ right.charCodeAt(index);
  return result === 0;
}

async function sign(value, secret) {
  const key = await crypto.subtle.importKey("raw", encoder.encode(secret), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const signature = await crypto.subtle.sign("HMAC", key, encoder.encode(value));
  return Array.from(new Uint8Array(signature), byte => byte.toString(16).padStart(2, "0")).join("");
}

async function hasAccess(request, secret) {
  const token = readCookie(request, COOKIE);
  if (!token) return false;
  const [expiresAt, signature] = token.split(".");
  if (!expiresAt || !signature || Number(expiresAt) <= Date.now()) return false;
  return equal(signature, await sign(expiresAt, secret));
}

function redirectToLogin(request) {
  const url = new URL(request.url);
  url.pathname = "/login";
  url.search = "";
  return Response.redirect(url, 302);
}

export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  const secret = env.CLARIFLIX_PASSWORD;

  if (url.pathname === "/login" || url.pathname === "/login.html") return context.next();
  if (!secret) return new Response("Configuração de acesso ausente.", { status: 500 });

  if (url.pathname === "/auth/login" && request.method === "POST") {
    let password = "";
    try { password = String((await request.json()).password || ""); } catch (_) { /* resposta negada abaixo */ }
    if (!equal(password, secret)) return new Response(JSON.stringify({ error: "Acesso negado." }), { status: 401, headers: { "content-type": "application/json" } });
    const expiresAt = String(Date.now() + ONE_DAY_SECONDS * 1000);
    const signature = await sign(expiresAt, secret);
    return new Response(null, { status: 204, headers: { "Set-Cookie": `${COOKIE}=${expiresAt}.${signature}; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=${ONE_DAY_SECONDS}` } });
  }

  if (await hasAccess(request, secret)) return context.next();
  if ((request.headers.get("Accept") || "").includes("text/html")) return redirectToLogin(request);
  return new Response("Acesso negado.", { status: 401 });
}
