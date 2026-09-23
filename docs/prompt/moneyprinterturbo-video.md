# moneyprinterturbo-video · arquivo para anexar

Ao ativar esta skill, siga o procedimento abaixo e use as seções `Referência:` no lugar dos arquivos citados. Esta versão reúne instruções e arquivos de apoio textuais; não instala ferramentas nem integrações. Scripts são apresentados como código de referência e não devem ser executados apenas por anexar este arquivo. Para trabalhar com a estrutura de arquivos original, instale o pacote completo.

Esta skill exige ferramentas de execução para parte do procedimento. Anexar este arquivo a um chat não habilita essas ferramentas; confira os requisitos da skill antes de prometer o resultado.

---

---
name: moneyprinterturbo-video
description: Gera vídeos curtos a partir de tema ou roteiro usando o fluxo MoneyPrinterTurbo. Use quando o resultado esperado for um arquivo de vídeo final.
version: 0.5.0
license: MIT
author: Harry
---

# Vídeo que vira entrega

As instruções oficiais e o helper da fonte estão preservados em [references/source/](references/source/).

## When to Use

Use para criar um vídeo final a partir de tema, título, ideia ou roteiro. Leia [references/source/SKILL.md](references/source/SKILL.md) antes de iniciar para verificar sistema operacional, dependências e provedores necessários.

## Quick Reference

O fluxo requer terminal, rede, armazenamento local, `uv` e pode solicitar credenciais de provedores de IA ou de mídia. Use os parâmetros de tema, roteiro, formato e voz fornecidos pelo usuário.

## Procedure

1. Confirme os pré-requisitos e identifique credenciais ausentes sem exibi-las em saídas ou logs.
2. Execute o helper oficial conforme a fonte, com um único trabalho por vez.
3. Informe o caminho do vídeo resultante e o resumo das escolhas usadas.

## Pitfalls

Não exponha chaves de API, não inicie serviços desnecessários e não execute opções que geram cobranças sem confirmação explícita do usuário. Respeite licenças de mídia, direitos de imagem e políticas da plataforma de destino.

## Verification

Confirme que o arquivo final existe, que o formato e o conteúdo correspondem ao pedido e que qualquer custo ou publicação externa recebeu autorização específica.


## Referência: LICENSE.source

```text
MIT License

Copyright (c) 2024 Harry

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```


## Referência: SOURCE.md

# Proveniência

- Fonte: [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo/tree/3d5f4e421927d61f3eac729cf4b711ac0b69d688/docs/skill)
- Commit: `3d5f4e421927d61f3eac729cf4b711ac0b69d688`
- Licença: MIT, preservada em `LICENSE.source`.
- Arquivos de origem preservados em `references/source/`; inventário e hashes em `references/moneyprinterturbo-source-inventory.json`.


## Referência: references/moneyprinterturbo-source-inventory.json

```json
{
  "source_url": "https://github.com/harry0703/MoneyPrinterTurbo/tree/3d5f4e421927d61f3eac729cf4b711ac0b69d688/docs/skill",
  "source_repository": "https://github.com/harry0703/MoneyPrinterTurbo",
  "source_commit": "3d5f4e421927d61f3eac729cf4b711ac0b69d688",
  "license": "MIT",
  "files": [
    {
      "path": "mpt_agent.py",
      "sha256": "a147d9b7ff7e0fa59e31d34e67a207d6a4a6a8bb9b7d284135d96f7b4a59e60f"
    },
    {
      "path": "SKILL.md",
      "sha256": "dffb69536e0b704663bc87176e4ac25a039fea5a01f47a99deb4646d54f7e9b7"
    }
  ]
}
```


## Referência: references/source/SKILL.md

---
name: moneyprinterturbo-video
description: Use this skill whenever the user wants to create a finished video from a topic, title, idea, prompt, or script with MoneyPrinterTurbo. This includes short-form, voice-over, educational, marketing, social-media, and stock-footage videos. Also use it when the user mentions MoneyPrinterTurbo, provides this Skill URL, asks an AI agent to install or configure MoneyPrinterTurbo, needs missing API keys identified, wants a failed generation repaired, or wants a generated MP4 located and delivered. Use this skill when the expected outcome is a final video file, not setup instructions.
compatibility: Requires an AI agent with terminal, network, filesystem, and long-running command support. Supports macOS and Windows and uses uv exclusively.
metadata:
  author: "harry0703@hotmail.com"
  version: "1.3.2"
  upstream: "https://github.com/harry0703/MoneyPrinterTurbo"
---

# MoneyPrinterTurbo Video Generation

The user only needs to provide a video topic or script. Complete installation, configuration reuse, generation, waiting, and final MP4 delivery automatically. Do not stop after giving instructions or commands.

## Required Behavior

1. Ask the user only for required API credentials that are missing, rejected, or unusable. Combine all required credentials into one request.
2. Do not ask for confirmation before installing, generating, waiting, using defaults, or returning the result.
3. Do not create or repeatedly update a detailed plan for a standard generation request. Send one short progress update and execute.
4. Run the helper as one foreground command with a timeout of at least 20 minutes.
5. Never poll with `sleep`, `echo`, `ps`, repeated `ls`, or repeated `tail`. If the terminal returns a resumable session ID, continue waiting on that same session.
6. Do not read the full log after success. Read only the short reported error or the relevant log tail after failure.
7. Never print API keys, tokens, the full `config.toml`, or credential-bearing configuration fragments.

## Defaults

Unless the user requests otherwise, generate one Chinese `9:16` portrait video with Pexels footage, the default Chinese Edge TTS voice, subtitles, and background music. Install MoneyPrinterTurbo under the user's home directory.

## Execution

### 1. Locate the helper

Resolve `SKILL_DIR` from this `SKILL.md` file. The helper is the adjacent `mpt_agent.py`. Set the terminal tool's working directory to `SKILL_DIR` and invoke the helper by its relative filename. Do not put the absolute helper path in the command, and do not run an extra `ls` or `dir` check.

This is required on Windows because some agent terminal validators remove backslashes from absolute paths embedded in commands. Using `mpt_agent.py` with `workdir=SKILL_DIR` avoids that failure and works on both macOS and Windows.

If the client loaded only the remote `SKILL.md`, download the helper from the official repository to a temporary directory, then use that temporary directory as the command working directory:

```text
https://raw.githubusercontent.com/harry0703/MoneyPrinterTurbo/main/docs/skill/mpt_agent.py
```

### 2. Run the helper

Do not run a separate `uv --version` preflight. Run the helper directly. If the shell explicitly reports that uv is missing, install uv and retry the same helper command once.

macOS uv installation:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows PowerShell uv installation:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Use this foreground command with `workdir=SKILL_DIR` and a timeout of at least 20 minutes:

```bash
uv run --no-project --python 3.11 python mpt_agent.py --subject "<video topic>"
```

On Windows, do not try absolute backslash paths, absolute forward-slash paths, or copies in the workspace before this relative command. If a terminal tool reports `referenced_script_path_missing`, verify that its working directory is exactly `SKILL_DIR` and retry the relative command once. Do not cycle through path variants.

Do not use Docker, Conda, system pip, or a manually managed virtual environment.

## Exit Handling

### Exit code 0: deliver the result

Successful output has this form:

```text
MPT_RESULT
VIDEO_FILE=<absolute path>/final-1.mp4
TASK_DIR=<absolute path>/storage/tasks/<task_id>
LOG_FILE=<absolute path>/run-<task_id>.log
RESULT_FILE=<absolute path>/latest-result.json
```

`mpt_agent.py` emits `VIDEO_FILE` only after confirming that the file exists and is non-empty. Do not run another `ls`, `stat`, or file validation command.

If the terminal reports `exitCode=0` but truncates the output or returns a history-file reference without `MPT_RESULT`, do not infer failure and do not inspect old logs. Read this file once:

```text
~/MoneyPrinterTurbo/.agent-logs/moneyprinterturbo-video/latest-result.json
```

Treat `status=completed` as success. Return only the absolute video path and a concise description, for example:

```text
The video is ready.
Topic: ...
Video file: /absolute/path/to/final-1.mp4
Summary: Chinese portrait video with voice-over, subtitles, and background music.
```

### Exit code 10: request credentials once

`MPT_NEEDS_INPUT` includes only the required fields, recommended LLM providers and signup links, custom OpenAI-compatible requirements, and material-provider signup links. Ask only for the listed values and do not request credentials already found in `config.toml`.

After the user responds, rerun the same foreground command with only the required environment variables:

```text
MPT_LLM_PROVIDER
MPT_LLM_API_KEY
MPT_LLM_BASE_URL
MPT_LLM_MODEL_NAME
MPT_PEXELS_API_KEY
MPT_VOLCENGINE_ARK_API_KEY
MPT_OFOX_API_KEY
MPT_METASO_MINIMAX_API_KEY
MPT_MUAPI_API_KEY
```

When `SEEDANCE_CHARGE_CONFIRMATION_REQUIRED` is present, explain that every
generated Seedance clip creates a paid Ark task. Only after the user explicitly
confirms, rerun with `--confirm-seedance-charge`; never add this flag silently.

When `WAVESPEED_CHARGE_CONFIRMATION_REQUIRED` is present, explain that every
generated WaveSpeed clip is billed per request by WaveSpeed. Only after the user
explicitly confirms, rerun with `--confirm-wavespeed-charge`; never add this
flag silently.

When `OFOX_CHARGE_CONFIRMATION_REQUIRED` is present, explain that every
generated OFox clip creates a paid task. Only after the user explicitly
confirms, rerun with `--confirm-ofox-charge`; never add this flag silently.

When `METASO_MINIMAX_CHARGE_CONFIRMATION_REQUIRED` is present, explain that
every generated MiniMax H3 clip creates a paid Metaso task. Only after the user
explicitly confirms, rerun with `--confirm-metaso-minimax-charge`; never add
this flag silently.

When `MUAPI_CHARGE_CONFIRMATION_REQUIRED` is present, explain that every
generated MuAPI clip creates a paid task. Only after the user explicitly
confirms, rerun with `--confirm-muapi-charge`; never add this flag silently.

### Exit code 1: repair or report

Use `MPT_ERROR` and `LOG_FILE` to repair a recoverable problem and retry once. Ask the user only if the repair requires a new API key. If the retry fails, report the failed stage, a short error, and the log path.

A terminal-tool path validation error is not a video-generation failure because the helper did not start. Correct the working directory and retry the relative command once. Never ask the user to copy `mpt_agent.py`, run commands manually, or confirm whether the agent should continue.

## Configuration and Background Fallback

The helper may read the complete local `config.toml` to reuse existing settings, but it must never print its contents. It reuses a working LLM provider automatically and validates configured Pexels keys through the authenticated My Collections endpoint before generation.

Use background mode only if the agent platform cannot wait for a foreground process. Wait for the platform's process-completion notification without polling, then read `latest-result.json` once.

## Scope

- Support macOS and Windows only.
- Use uv and the MoneyPrinterTurbo CLI only.
- Do not start Docker, WebUI, or API services.
- Do not run multiple video jobs concurrently.
- Pass additional video requirements after `--`. Run `cli.py --help` once only when an unfamiliar option must be verified.


## Referência: references/source/mpt_agent.py

```python
#!/usr/bin/env python3
"""Cross-platform installation and video generation for the MoneyPrinterTurbo Skill."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
import uuid
import zipfile
from datetime import datetime, timezone
from pathlib import Path


PROJECT_ARCHIVE_URL = (
    "https://github.com/harry0703/MoneyPrinterTurbo/archive/refs/heads/main.zip"
)
DEFAULT_ROOT = Path.home() / "MoneyPrinterTurbo"
DEFAULT_VOICE_NAME = "zh-CN-XiaoxiaoNeural-Female"
NEEDS_INPUT_EXIT_CODE = 10
SUPPORTED_SOURCES = {
    "pexels",
    "pixabay",
    "coverr",
    "wavespeed",
    "volcengine_seedance",
    "ofox",
    "metaso_minimax",
    "muapi",
    # Keep this list aligned with ``_CLI_VIDEO_SOURCES`` in cli.py. A source that
    # the CLI accepts must not be rejected here as unsupported.
    "openai_image",
    "local",
}
VOLCENGINE_ARK_API_KEY_URL = (
    "https://console.volcengine.com/ark/region:ark+cn-beijing/apikey"
)
OFOX_API_KEY_URL = "https://ofox.ai"
MUAPI_API_KEY_URL = "https://muapi.ai"
PEXELS_API_KEY_URL = "https://www.pexels.com/api/"
PEXELS_VALIDATION_URL = "https://api.pexels.com/v1/collections?per_page=1"
PEXELS_API_KEY_HELP_URL = (
    "https://help.pexels.com/hc/en-us/articles/"
    "900004904026-How-do-I-get-an-API-key"
)

# Keep the recommended list focused on commonly used providers. When an LLM
# key is missing, the helper emits all choices at once to avoid extra turns.
RECOMMENDED_LLM_PROVIDERS = {
    "moonshot": (
        "Kimi / Moonshot AI",
        "https://platform.kimi.com?track_id=track-2f5441d6ffd84c509dd079d78e9db5dc&aff=moneyprinterturbo",
    ),
    "openai": ("OpenAI", "https://platform.openai.com/api-keys"),
    "gemini": ("Google Gemini", "https://aistudio.google.com/app/apikey"),
    "deepseek": ("DeepSeek", "https://platform.deepseek.com/api_keys"),
    "volcengine": (
        "ByteDance VolcEngine Ark / Doubao",
        "https://www.volcengine.com/activity/ai618?utm_source=MoneyPrinterTurbo",
    ),
    "minimax": ("MiniMax", "https://platform.minimax.io/"),
    "mimo": (
        "Xiaomi MiMo",
        "https://platform.xiaomimimo.com/docs/zh-CN/quick-start/first-api-call",
    ),
}
# Providers that generate without an API key stored in config.toml: Ollama talks
# to a local server, LiteLLM resolves credentials through its own environment,
# and ``claude_code`` consumes the Claude subscription through the locally
# logged-in ``claude`` CLI. Keep this set aligned with the
# ``requires_api_key=False`` entries of ``app/models/llm_provider.py``; asking
# the user for a key that the provider never reads leaves the Skill stuck.
KEYLESS_LLM_PROVIDERS = {"ollama", "litellm", "claude_code"}
CUSTOM_OPENAI_PROVIDER = "oneapi"

# Hidden providers such as Qwen, Azure, and Grok remain usable when already
# selected, but are not automatic fallback candidates. A fully configured
# generic OpenAI-compatible endpoint can be reused safely.
ADDITIONAL_REUSABLE_PROVIDERS = (CUSTOM_OPENAI_PROVIDER,)


class SkillError(RuntimeError):
    """An actionable Skill error that can be reported without a traceback."""


def log(message: str) -> None:
    """Flush concise progress so the agent knows the long-running job started."""
    print(f"[MoneyPrinterTurbo] {message}", flush=True)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install MoneyPrinterTurbo and generate a final video from a topic."
    )
    parser.add_argument("--subject", required=True, help="video topic")
    parser.add_argument(
        "--root",
        type=Path,
        default=DEFAULT_ROOT,
        help=f"MoneyPrinterTurbo installation directory (default: {DEFAULT_ROOT})",
    )
    parser.add_argument(
        "cli_args",
        nargs=argparse.REMAINDER,
        help="additional MoneyPrinterTurbo CLI arguments placed after --",
    )
    args = parser.parse_args(argv)
    args.subject = args.subject.strip()
    if not args.subject:
        parser.error("--subject cannot be empty")
    if args.cli_args and args.cli_args[0] == "--":
        args.cli_args = args.cli_args[1:]
    return args


def _safe_extract(archive: zipfile.ZipFile, destination: Path) -> None:
    """Reject ZIP entries that would escape the temporary extraction directory."""
    destination = destination.resolve()
    for member in archive.infolist():
        target = (destination / member.filename).resolve()
        if target != destination and destination not in target.parents:
            raise SkillError(f"project archive contains an unsafe path: {member.filename}")
    archive.extractall(destination)


def ensure_project(root: Path) -> None:
    """Reuse an existing project or install it from the official GitHub archive."""
    root = root.expanduser().resolve()
    if (root / "cli.py").is_file() and (root / "config.example.toml").is_file():
        log(f"using existing project: {root}")
        return
    if root.exists() and any(root.iterdir()):
        raise SkillError(f"installation directory exists but is not a valid project: {root}")

    root.parent.mkdir(parents=True, exist_ok=True)
    log(f"first-time installation: downloading the official project to {root}")
    with tempfile.TemporaryDirectory(prefix="mpt-install-") as temp_dir_value:
        temp_dir = Path(temp_dir_value)
        archive_path = temp_dir / "MoneyPrinterTurbo.zip"
        request = urllib.request.Request(
            PROJECT_ARCHIVE_URL,
            headers={"User-Agent": "MoneyPrinterTurbo-Agent-Skill"},
        )
        with urllib.request.urlopen(request, timeout=120) as response:
            # Stream the archive to avoid holding a second full copy in memory.
            with archive_path.open("wb") as archive_file:
                shutil.copyfileobj(response, archive_file)
        with zipfile.ZipFile(archive_path) as archive:
            _safe_extract(archive, temp_dir)

        candidates = [
            path
            for path in temp_dir.iterdir()
            if path.is_dir() and (path / "cli.py").is_file()
        ]
        if len(candidates) != 1:
            raise SkillError("download completed but no valid MoneyPrinterTurbo project was found")
        if root.exists():
            root.rmdir()
        shutil.move(str(candidates[0]), str(root))
    log("project download completed")


def ensure_config(root: Path) -> Path:
    """Create the initial configuration without overwriting an existing file."""
    config_path = root / "config.toml"
    if not config_path.exists():
        shutil.copy2(root / "config.example.toml", config_path)
        log(f"created configuration file: {config_path}")
    return config_path


def _plain_config_value(text: str, key: str) -> str:
    """Read a simple top-level TOML value without printing its contents."""
    match = re.search(rf"(?m)^{re.escape(key)}\s*=\s*(.*)$", text)
    if not match:
        return ""
    value = match.group(1).split("#", 1)[0].strip()
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    return value


def _replace_config_value(text: str, key: str, value: object) -> str:
    """Replace one active field while preserving the configuration layout."""
    pattern = re.compile(rf"(?m)^({re.escape(key)}\s*=\s*).*$")
    if not pattern.search(text):
        raise SkillError(f"configuration field not found in config.toml: {key}")
    encoded = json.dumps(value, ensure_ascii=False)
    return pattern.sub(lambda match: f"{match.group(1)}{encoded}", text, count=1)


def _has_configured_value(value: str) -> bool:
    """Treat empty strings and whitespace-only key arrays as unconfigured."""
    if not value:
        return False
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError:
        return bool(value.strip())
    if isinstance(parsed, list):
        return any(str(item).strip() for item in parsed)
    return bool(str(parsed).strip())


def _parse_string_list(value: str) -> list[str]:
    """Parse a configured string list while removing blanks and duplicates."""
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError:
        return []
    if not isinstance(parsed, list):
        return []
    return list(dict.fromkeys(str(item).strip() for item in parsed if str(item).strip()))


def apply_environment_config(config_path: Path) -> None:
    """Write supplied credentials while logging field names only."""
    provider = os.environ.get("MPT_LLM_PROVIDER", "").strip().lower()
    if provider == "openai_compatible":
        provider = CUSTOM_OPENAI_PROVIDER
    llm_key = os.environ.get("MPT_LLM_API_KEY", "").strip()
    base_url = os.environ.get("MPT_LLM_BASE_URL", "").strip()
    model_name = os.environ.get("MPT_LLM_MODEL_NAME", "").strip()
    pexels_key = os.environ.get("MPT_PEXELS_API_KEY", "").strip()
    seedance_key = os.environ.get("MPT_VOLCENGINE_ARK_API_KEY", "").strip()
    ofox_key = os.environ.get("MPT_OFOX_API_KEY", "").strip()
    metaso_minimax_key = os.environ.get(
        "MPT_METASO_MINIMAX_API_KEY", ""
    ).strip()
    muapi_key = os.environ.get("MPT_MUAPI_API_KEY", "").strip()
    if not any(
        (
            provider,
            llm_key,
            base_url,
            model_name,
            pexels_key,
            seedance_key,
            ofox_key,
            metaso_minimax_key,
            muapi_key,
        )
    ):
        return

    text = config_path.read_text(encoding="utf-8")
    current_provider = _plain_config_value(text, "llm_provider") or "moonshot"
    provider = provider or current_provider
    changes: list[str] = []
    if os.environ.get("MPT_LLM_PROVIDER", "").strip():
        text = _replace_config_value(text, "llm_provider", provider)
        changes.append("llm_provider")
    if llm_key:
        text = _replace_config_value(text, f"{provider}_api_key", llm_key)
        changes.append(f"{provider}_api_key")
    if base_url:
        text = _replace_config_value(text, f"{provider}_base_url", base_url)
        changes.append(f"{provider}_base_url")
    if model_name:
        text = _replace_config_value(text, f"{provider}_model_name", model_name)
        changes.append(f"{provider}_model_name")
    if pexels_key:
        text = _replace_config_value(text, "pexels_api_keys", [pexels_key])
        changes.append("pexels_api_keys")
    if seedance_key:
        text = _replace_config_value(
            text, "volcengine_seedance_api_key", seedance_key
        )
        changes.append("volcengine_seedance_api_key")
    if ofox_key:
        text = _replace_config_value(text, "ofox_api_key", ofox_key)
        changes.append("ofox_api_key")
    if metaso_minimax_key:
        text = _replace_config_value(
            text, "metaso_minimax_api_key", metaso_minimax_key
        )
        changes.append("metaso_minimax_api_key")
    if muapi_key:
        text = _replace_config_value(text, "muapi_api_key", muapi_key)
        changes.append("muapi_api_key")
    config_path.write_text(text, encoding="utf-8")
    log("updated configuration fields: " + ", ".join(changes))


def _provider_is_ready(text: str, provider: str) -> bool:
    """Return whether a provider has enough configuration to generate."""
    if provider in KEYLESS_LLM_PROVIDERS:
        return True
    if not _has_configured_value(
        _plain_config_value(text, f"{provider}_api_key")
    ):
        return False
    if provider == CUSTOM_OPENAI_PROVIDER:
        return all(
            _has_configured_value(_plain_config_value(text, f"{provider}_{suffix}"))
            for suffix in ("base_url", "model_name")
        )
    return True


def reuse_existing_llm_provider(config_path: Path) -> str:
    """
    Reuse existing LLM credentials before asking the user for another key.

    Keep the current provider when it is ready. Otherwise, scan configured
    recommended providers in UI order and update ``llm_provider``. Credential
    values are inspected in memory and are never logged.
    """
    text = config_path.read_text(encoding="utf-8")
    current_provider = _plain_config_value(text, "llm_provider") or "moonshot"
    if _provider_is_ready(text, current_provider):
        return current_provider

    reusable_providers = (
        *RECOMMENDED_LLM_PROVIDERS,
        *ADDITIONAL_REUSABLE_PROVIDERS,
    )
    for provider in reusable_providers:
        if _provider_is_ready(text, provider):
            text = _replace_config_value(text, "llm_provider", provider)
            config_path.write_text(text, encoding="utf-8")
            log(f"reusing configured LLM provider: {provider}")
            return provider
    return current_provider


def selected_video_source(cli_args: list[str]) -> str:
    """Read the effective material source from forwarded CLI arguments."""
    for index, item in enumerate(cli_args):
        if item == "--video-source" and index + 1 < len(cli_args):
            return cli_args[index + 1].strip().lower()
        if item.startswith("--video-source="):
            return item.split("=", 1)[1].strip().lower()
    return "pexels"


def has_cli_option(cli_args: list[str], option: str) -> bool:
    """Return whether forwarded arguments explicitly set a CLI option."""
    return any(item == option or item.startswith(f"{option}=") for item in cli_args)


def missing_config(config_path: Path, cli_args: list[str]) -> tuple[str, list[str]]:
    """Return the active provider and only the fields required by this run."""
    text = config_path.read_text(encoding="utf-8")
    provider = _plain_config_value(text, "llm_provider") or "moonshot"
    missing: list[str] = []
    if provider not in KEYLESS_LLM_PROVIDERS and not _has_configured_value(
        _plain_config_value(text, f"{provider}_api_key")
    ):
        missing.append(f"{provider}_api_key")
    if provider == CUSTOM_OPENAI_PROVIDER:
        for suffix in ("base_url", "model_name"):
            field = f"{provider}_{suffix}"
            if not _has_configured_value(_plain_config_value(text, field)):
                missing.append(field)

    source = selected_video_source(cli_args)
    if source not in SUPPORTED_SOURCES:
        raise SkillError(f"unsupported video source: {source}")
    if source == "volcengine_seedance":
        # 与运行时 Provider 保持完全一致的凭据优先级，避免 Skill 预检通过后
        # 主程序却读取了另一把 Key。ARK_API_KEY 语义过于宽泛，明确不再兼容。
        value = (
            _plain_config_value(text, "volcengine_seedance_api_key")
            or os.environ.get("VOLCENGINE_ARK_API_KEY", "").strip()
            or _plain_config_value(text, "volcengine_api_key")
        )
        if not _has_configured_value(value):
            missing.append("volcengine_seedance_api_key")
        if not has_cli_option(cli_args, "--confirm-seedance-charge"):
            missing.append("confirm_seedance_charge")
    elif source == "wavespeed":
        # WaveSpeed 的运行时凭据只来自 wavespeed_api_keys，没有环境变量回退，
        # 这里保持同一口径。按次计费的生成源还必须显式确认收费。
        if not _has_configured_value(
            _plain_config_value(text, "wavespeed_api_keys")
        ):
            missing.append("wavespeed_api_keys")
        if not has_cli_option(cli_args, "--confirm-wavespeed-charge"):
            missing.append("confirm_wavespeed_charge")
    elif source == "ofox":
        # 与运行时 Provider 保持完全一致的凭据优先级：配置键优先，其次是
        # 语义明确的 OFOX_API_KEY 环境变量。
        value = (
            _plain_config_value(text, "ofox_api_key")
            or os.environ.get("OFOX_API_KEY", "").strip()
        )
        if not _has_configured_value(value):
            missing.append("ofox_api_key")
        if not has_cli_option(cli_args, "--confirm-ofox-charge"):
            missing.append("confirm_ofox_charge")
    elif source == "metaso_minimax":
        # 秘塔 Key 与 MiniMax 官方 LLM Key 不互通，Skill 必须沿用运行时的
        # 独立配置优先级，不能因为已经配置 minimax_api_key 就误判为可用。
        value = (
            _plain_config_value(text, "metaso_minimax_api_key")
            or os.environ.get("METASO_MINIMAX_API_KEY", "").strip()
        )
        if not _has_configured_value(value):
            missing.append("metaso_minimax_api_key")
        if not has_cli_option(cli_args, "--confirm-metaso-minimax-charge"):
            missing.append("confirm_metaso_minimax_charge")
    elif source == "muapi":
        value = (
            _plain_config_value(text, "muapi_api_key")
            or os.environ.get("MUAPI_API_KEY", "").strip()
        )
        if not _has_configured_value(value):
            missing.append("muapi_api_key")
        if not has_cli_option(cli_args, "--confirm-muapi-charge"):
            missing.append("confirm_muapi_charge")
    elif source == "openai_image":
        # 与运行时的 is_openai_image_enabled() 保持一致：文生图素材源只要求端点
        # 与模型名。完全本地的 ComfyUI/SD 网关允许不配置 API Key，因此这里不
        # 能把 openai_image_api_keys 当作必填项。
        for field in ("openai_image_base_url", "openai_image_model"):
            if not _has_configured_value(_plain_config_value(text, field)):
                missing.append(field)
    elif source != "local":
        value = _plain_config_value(text, f"{source}_api_keys")
        if not _has_configured_value(value):
            missing.append(f"{source}_api_keys")
    return provider, missing


def report_missing_config(provider: str, missing: list[str]) -> int:
    """Tell the agent exactly which credentials must be requested."""
    print("MPT_NEEDS_INPUT")
    print(f"LLM_PROVIDER={provider}")
    for field in missing:
        print(f"MISSING={field}")
    if any(
        field.endswith("_api_key")
        and field not in {
            "volcengine_seedance_api_key",
            "ofox_api_key",
            "metaso_minimax_api_key",
            "muapi_api_key",
        }
        for field in missing
    ):
        print("LLM_PROVIDER_OPTIONS_BEGIN")
        for provider_id, (label, url) in RECOMMENDED_LLM_PROVIDERS.items():
            print(f"LLM_PROVIDER_OPTION={provider_id}|{label}|{url}")
        print(
            "LLM_PROVIDER_OPTION=oneapi|Other OpenAI-compatible provider|"
            "requires an API key, API base URL, and model name"
        )
        print("LLM_PROVIDER_OPTIONS_END")
    if any(field.startswith(f"{CUSTOM_OPENAI_PROVIDER}_") for field in missing):
        print(
            "OPENAI_COMPATIBLE_REQUIRED="
            "API key, API base URL, model name"
        )
    if any(field.startswith("openai_image_") for field in missing):
        print(
            "OPENAI_IMAGE_REQUIRED="
            "openai_image_base_url, openai_image_model (the API key is optional "
            "for local gateways)"
        )
    if "pexels_api_keys" in missing:
        print(f"PEXELS_API_KEY_URL={PEXELS_API_KEY_URL}")
        print(f"PEXELS_API_KEY_HELP_URL={PEXELS_API_KEY_HELP_URL}")
    if "volcengine_seedance_api_key" in missing:
        print(f"VOLCENGINE_ARK_API_KEY_URL={VOLCENGINE_ARK_API_KEY_URL}")
        print("VOLCENGINE_ARK_API_KEY_ENV=MPT_VOLCENGINE_ARK_API_KEY")
    if "confirm_seedance_charge" in missing:
        print("SEEDANCE_CHARGE_CONFIRMATION_REQUIRED=--confirm-seedance-charge")
    if "confirm_wavespeed_charge" in missing:
        print("WAVESPEED_CHARGE_CONFIRMATION_REQUIRED=--confirm-wavespeed-charge")
    if "ofox_api_key" in missing:
        print(f"OFOX_API_KEY_URL={OFOX_API_KEY_URL}")
        print("OFOX_API_KEY_ENV=MPT_OFOX_API_KEY")
    if "confirm_ofox_charge" in missing:
        print("OFOX_CHARGE_CONFIRMATION_REQUIRED=--confirm-ofox-charge")
    if "metaso_minimax_api_key" in missing:
        print("METASO_MINIMAX_API_KEY_ENV=MPT_METASO_MINIMAX_API_KEY")
    if "confirm_metaso_minimax_charge" in missing:
        print(
            "METASO_MINIMAX_CHARGE_CONFIRMATION_REQUIRED="
            "--confirm-metaso-minimax-charge"
        )
    if "muapi_api_key" in missing:
        print(f"MUAPI_API_KEY_URL={MUAPI_API_KEY_URL}")
        print("MUAPI_API_KEY_ENV=MPT_MUAPI_API_KEY")
    if "confirm_muapi_charge" in missing:
        print("MUAPI_CHARGE_CONFIRMATION_REQUIRED=--confirm-muapi-charge")
    print("Request only the listed values, set the environment variables, and rerun the same command.")
    return NEEDS_INPUT_EXIT_CODE


def report_invalid_pexels_config() -> int:
    """Request only a new Pexels key when every configured key is rejected."""
    print("MPT_NEEDS_INPUT")
    print("INVALID=pexels_api_keys")
    print(f"PEXELS_API_KEY_URL={PEXELS_API_KEY_URL}")
    print(f"PEXELS_API_KEY_HELP_URL={PEXELS_API_KEY_HELP_URL}")
    print("All configured Pexels API keys were rejected or are unavailable. Provide a new key.")
    return NEEDS_INPUT_EXIT_CODE


def _validate_pexels_key(api_key: str) -> str:
    """
    Return ``valid``, ``rejected``, or ``unknown`` for a Pexels key.

    HTTP 401, 403, and rate-limited 429 responses make a key unusable for this
    run. Network and server errors return unknown so the configuration is kept.
    """
    # Curated and popular search requests may hit a public cache and return 200
    # without valid authorization. My Collections is account-specific, requires
    # authentication, and still returns 200 for an empty collection list.
    request = urllib.request.Request(
        PEXELS_VALIDATION_URL,
        headers={
            "Authorization": api_key,
            "User-Agent": "MoneyPrinterTurbo-Agent-Skill",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            return "valid" if 200 <= response.status < 300 else "unknown"
    except urllib.error.HTTPError as exc:
        if exc.code in {401, 403, 429}:
            return "rejected"
        return "unknown"
    except (TimeoutError, urllib.error.URLError):
        return "unknown"


def validate_pexels_config(config_path: Path, cli_args: list[str]) -> bool:
    """
    Validate all Pexels keys used by the default material source.

    Downstream code selects configured keys randomly. Keeping rejected keys can
    cause intermittent 401 responses and missing material results. If at least
    one key is verified, retain only verified keys. If validation is impossible
    because of a transient network failure, keep the original configuration.
    """
    if selected_video_source(cli_args) != "pexels":
        return True

    text = config_path.read_text(encoding="utf-8")
    keys = _parse_string_list(_plain_config_value(text, "pexels_api_keys"))
    if not keys:
        return False

    valid_keys: list[str] = []
    rejected_count = 0
    unknown_count = 0
    for api_key in keys:
        status = _validate_pexels_key(api_key)
        if status == "valid":
            valid_keys.append(api_key)
        elif status == "rejected":
            rejected_count += 1
        else:
            unknown_count += 1

    if valid_keys:
        if valid_keys != keys:
            text = _replace_config_value(text, "pexels_api_keys", valid_keys)
            config_path.write_text(text, encoding="utf-8")
        log(
            "Pexels key validation completed: "
            f"valid={len(valid_keys)}, rejected={rejected_count}, "
            f"unknown={unknown_count}"
        )
        return True
    if unknown_count:
        log("Pexels keys could not be verified due to a network or service error; keeping the existing configuration")
        return True

    log(f"Pexels key validation failed: all {rejected_count} configured keys are unusable")
    return False


def result_manifest_path(root: Path) -> Path:
    return root / ".agent-logs" / "moneyprinterturbo-video" / "latest-result.json"


def write_result_manifest(root: Path, payload: dict[str, object]) -> Path:
    """
    Atomically write the stable result file for agents that cannot wait.

    The file contains task status and result paths only, never configuration
    contents, credentials, or full logs.
    """
    result_path = result_manifest_path(root)
    result_path.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        **payload,
    }
    unique_suffix = str(uuid.uuid4()).replace("-", "")
    temp_path = result_path.with_name(
        f".{result_path.name}.{os.getpid()}.{unique_suffix}.tmp"
    )
    temp_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    temp_path.replace(result_path)
    return result_path.resolve()


def run_checked(command: list[str], *, cwd: Path) -> None:
    """Run dependency sync quietly and show only the last 30 lines on failure."""
    log("installing or verifying project dependencies with uv")
    result = subprocess.run(
        command,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if result.returncode != 0:
        output_tail = (result.stdout or "").splitlines()[-30:]
        if output_tail:
            print("\n".join(output_tail), file=sys.stderr)
        raise SkillError(f"dependency installation failed with exit code {result.returncode}")


def generate_video(
    root: Path,
    subject: str,
    cli_args: list[str],
) -> tuple[list[Path], Path, Path, Path]:
    """Run one traceable CLI task and return only its final video files."""
    uv = shutil.which("uv")
    if not uv:
        raise SkillError("uv was not found; reopen the terminal or add uv to PATH")
    run_checked([uv, "sync", "--frozen"], cwd=root)

    task_id = str(uuid.uuid4())
    task_dir = root / "storage" / "tasks" / task_id
    log_dir = root / ".agent-logs" / "moneyprinterturbo-video"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"run-{task_id}.log"
    write_result_manifest(
        root,
        {
            "status": "running",
            "subject": subject,
            "task_id": task_id,
            "task_dir": str(task_dir.resolve()),
            "log_file": str(log_path.resolve()),
            "video_files": [],
        },
    )
    voice_args = (
        []
        if has_cli_option(cli_args, "--voice-name")
        else ["--voice-name", DEFAULT_VOICE_NAME]
    )
    command = [
        uv,
        "run",
        "python",
        "cli.py",
        *cli_args,
        "--video-subject",
        subject,
        "--task-id",
        task_id,
        # Older CLI versions leave voice_name empty and fail during Edge TTS
        # with ``Invalid voice ''``. Supply a stable Chinese voice unless the
        # user has explicitly selected another voice.
        *voice_args,
        # A Skill request must produce a finished video. Force the final stage
        # so forwarded options cannot stop at script, audio, or materials.
        "--stop-at",
        "video",
    ]
    log(f"starting video generation, task ID: {task_id}")
    log(f"full generation log: {log_path}")
    with log_path.open("w", encoding="utf-8") as log_file:
        result = subprocess.run(
            command,
            cwd=root,
            stdout=log_file,
            stderr=subprocess.STDOUT,
            text=True,
            check=False,
        )
    if result.returncode != 0:
        tail = log_path.read_text(encoding="utf-8", errors="replace").splitlines()[-30:]
        if tail:
            print("\n".join(tail), file=sys.stderr)
        error = (
            f"video generation failed with exit code {result.returncode}; "
            f"log: {log_path}"
        )
        write_result_manifest(
            root,
            {
                "status": "failed",
                "subject": subject,
                "task_id": task_id,
                "task_dir": str(task_dir.resolve()),
                "log_file": str(log_path.resolve()),
                "video_files": [],
                "error": error,
            },
        )
        raise SkillError(error)

    videos = sorted(
        path.resolve()
        for path in task_dir.glob("final-*.mp4")
        if path.is_file() and path.stat().st_size > 0
    )
    if not videos:
        error = f"generation completed without a valid final MP4; log: {log_path}"
        write_result_manifest(
            root,
            {
                "status": "failed",
                "subject": subject,
                "task_id": task_id,
                "task_dir": str(task_dir.resolve()),
                "log_file": str(log_path.resolve()),
                "video_files": [],
                "error": error,
            },
        )
        raise SkillError(error)
    result_path = write_result_manifest(
        root,
        {
            "status": "completed",
            "subject": subject,
            "task_id": task_id,
            "task_dir": str(task_dir.resolve()),
            "log_file": str(log_path.resolve()),
            "video_files": [str(video) for video in videos],
        },
    )
    return videos, task_dir.resolve(), log_path.resolve(), result_path


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root = args.root.expanduser().resolve()
    try:
        ensure_project(root)
        config_path = ensure_config(root)
        apply_environment_config(config_path)
        reuse_existing_llm_provider(config_path)
        provider, missing = missing_config(config_path, args.cli_args)
        if missing:
            write_result_manifest(
                root,
                {
                    "status": "needs_input",
                    "subject": args.subject,
                    "missing": missing,
                },
            )
            return report_missing_config(provider, missing)
        if not validate_pexels_config(config_path, args.cli_args):
            write_result_manifest(
                root,
                {
                    "status": "needs_input",
                    "subject": args.subject,
                    "invalid": ["pexels_api_keys"],
                },
            )
            return report_invalid_pexels_config()
        videos, task_dir, log_path, result_path = generate_video(
            root, args.subject, args.cli_args
        )
    except (OSError, SkillError, urllib.error.URLError, zipfile.BadZipFile) as exc:
        print(f"MPT_ERROR={exc}", file=sys.stderr)
        return 1

    print("MPT_RESULT")
    for video in videos:
        print(f"VIDEO_FILE={video}")
    print(f"TASK_DIR={task_dir}")
    print(f"LOG_FILE={log_path}")
    print(f"RESULT_FILE={result_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```
