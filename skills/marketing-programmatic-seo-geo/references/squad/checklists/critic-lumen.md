# Checklist do critic Lumen — Programmatic SEO + GEO/AEO

**Pattern:** Quality Gate · **Modo:** bloqueante · **Fonte:** especificação do critic do squad (literal)

## Descrição do critic (literal)

Lumen — O Guardiao da Qualidade Editorial — Valida TODO conteudo gerado pelo Scribe e otimizado pelo Beacon antes de qualquer publicacao. Checklist obrigatorio de 10 pontos — reprovar em qualquer ponto critico bloqueia a publicacao: (1) SEO Score minimo: o conteudo atinge o score minimo configurado no Frase ou SemRush (baseline: 70/100 para producao programatica, 80/100 para artigos editoriais)? Abaixo do threshold = REESCREVER com instrucoes especificas; (2) Factualidade: CADA afirmacao factual tem fonte verificavel com URL e data? Zero tolerancia para dados sem fonte — qualquer dado sem rastreabilidade = REPROVAR; (3) Unicidade: a pagina tem menos de 20% de overlap textual com outras paginas do mesmo dominio (canibalizacao) e menos de 10% com conteudo externo (plágio)? Verificado via ferramenta de similarity check; (4) GEO Score minimo: o conteudo tem pelo menos 3 elementos explicitamente citable por LLMs (stat block, definition box, answer snippet, tabela comparativa com dados)? Abaixo do threshold = OTIMIZAR com Beacon antes de publicar; (5) Brand compliance: o tom, vocabulario e posicionamento estao alinhados com o guia de voz da marca? Nenhuma afirmacao que o cliente nao possa defender publicamente; (6) E-E-A-T signals: o conteudo demonstra experiencia e especialidade reais? Links para fontes autoritativas, dados de primeira parte quando disponiveis, perspectiva especialista — nao conteudo generico de IA sem substantia; (7) Internal linking: as sugestoes de internal link do Atlas fazem sentido contextual? Links forcados ou irrelevantes = corrigir antes de publicar; (8) Conteudo thin: cada pagina tem no minimo 800 palavras de conteudo real (nao contando boilerplate de navegacao, footer, etc)? Paginas thin abaixo de 800 palavras = expandir ou combinar com outra pagina do batch; (9) Metadata quality: meta title <= 60 chars com keyword, meta description <= 155 chars com CTA, slug limpo sem stopwords? Qualquer campo fora do spec = corrigir automaticamente; (10) Duplicate metadata: os campos de meta title e meta description sao unicos no dominio inteiro? Duplicata encontrada = gerar nova variacao automaticamente. Veredicto: APROVADO (segue para Atlas publicar) / OTIMIZAR com instrucoes especificas por ponto (volta para Scribe ou Beacon, max 1 ciclo automatico) / BLOQUEAR_HITL para casos que exigem revisao humana (factualidade questionavel, compliance de marca, conteudo em cluster estrategico de alta competicao). Opera em paralelo em todos os itens do batch — nunca um a um sequencialmente.

## Itens de verificação (derivados da descrição, uma frase = um item)

- [ ] **C01** — O Guardiao da Qualidade Editorial
- [ ] **C02** — Valida TODO conteudo gerado pelo Scribe e otimizado pelo Beacon antes de qualquer publicacao
- [ ] **C03** — Checklist obrigatorio de 10 pontos
- [ ] **C04** — reprovar em qualquer ponto critico bloqueia a publicacao: (1) SEO Score minimo: o conteudo atinge o score minimo configurado no Frase ou SemRush (baseline: 70/100 para producao programatica, 80/100 para artigos editoriais)? Abaixo do threshold = REESCREVER com instrucoes especificas
- [ ] **C05** — (2) Factualidade: CADA afirmacao factual tem fonte verificavel com URL e data? Zero tolerancia para dados sem fonte
- [ ] **C06** — qualquer dado sem rastreabilidade = REPROVAR
- [ ] **C07** — (3) Unicidade: a pagina tem menos de 20% de overlap textual com outras paginas do mesmo dominio (canibalizacao) e menos de 10% com conteudo externo (plágio)? Verificado via ferramenta de similarity check
- [ ] **C08** — (4) GEO Score minimo: o conteudo tem pelo menos 3 elementos explicitamente citable por LLMs (stat block, definition box, answer snippet, tabela comparativa com dados)? Abaixo do threshold = OTIMIZAR com Beacon antes de publicar
- [ ] **C09** — (5) Brand compliance: o tom, vocabulario e posicionamento estao alinhados com o guia de voz da marca? Nenhuma afirmacao que o cliente nao possa defender publicamente
- [ ] **C10** — (6) E-E-A-T signals: o conteudo demonstra experiencia e especialidade reais? Links para fontes autoritativas, dados de primeira parte quando disponiveis, perspectiva especialista
- [ ] **C11** — nao conteudo generico de IA sem substantia
- [ ] **C12** — (7) Internal linking: as sugestoes de internal link do Atlas fazem sentido contextual? Links forcados ou irrelevantes = corrigir antes de publicar
- [ ] **C13** — (8) Conteudo thin: cada pagina tem no minimo 800 palavras de conteudo real (nao contando boilerplate de navegacao, footer, etc)? Paginas thin abaixo de 800 palavras = expandir ou combinar com outra pagina do batch
- [ ] **C14** — (9) Metadata quality: meta title <= 60 chars com keyword, meta description <= 155 chars com CTA, slug limpo sem stopwords? Qualquer campo fora do spec = corrigir automaticamente
- [ ] **C15** — (10) Duplicate metadata: os campos de meta title e meta description sao unicos no dominio inteiro? Duplicata encontrada = gerar nova variacao automaticamente
- [ ] **C16** — Veredicto: APROVADO (segue para Atlas publicar) / OTIMIZAR com instrucoes especificas por ponto (volta para Scribe ou Beacon, max 1 ciclo automatico) / BLOQUEAR_HITL para casos que exigem revisao humana (factualidade questionavel, compliance de marca, conteudo em cluster estrategico de alta competicao)
- [ ] **C17** — Opera em paralelo em todos os itens do batch
- [ ] **C18** — nunca um a um sequencialmente

## Gates humanos (bloqueiam até decisão)

- [ ] **HITL** — Gate L3 no Atlas: qualquer publicacao ou edicao de paginas na lista de URLs estrategicas (pillar pages, paginas com backlinks externos, paginas de alta competicao definidas no onboarding) bloqueia e notifica o gestor de conteudo com preview completo para aprovacao antes de publicar um caracter.
- [ ] **HITL** — Lumen reprova 2x no mesmo item: conteúdo que falhou no ciclo automático de otimização (Scribe ou Beacon reescreve 1x, Lumen reprova novamente) e escalado para o editor humano com o checklist completo de reprovações e sugestões específicas de correção.
- [ ] **HITL** — Factualidade questionável detectada pelo Lumen: qualquer dado que não tem fonte verificável com URL ativo e data recente é imediatamente bloqueado e sinalizado para o time de conteúdo verificar manualmente antes de qualquer publicação — zero tolerância para afirmação sem rastreabilidade.
- [ ] **HITL** — Batch de publicação programática acima de 50 páginas: qualquer batch acima do threshold configurado (default: 50 páginas/batch) requer aprovação do gestor de SEO antes do Atlas iniciar a publicação — para proteger o crawl budget e a reputação do domínio.
- [ ] **HITL** — Queda abrupta de visibilidade detectada pelo Sonar: queda de >30% em tráfego orgânico em 7 dias ou desaparecimento de cluster inteiro das SERPs = alerta imediato ao time de SEO para investigação manual antes de qualquer ação automática do squad — pode ser update algorítmico que requer análise humana.
- [ ] **HITL** — Novos templates programáticos: sempre que Lexus ou Argo identificam um novo tipo de página programática não mapeada anteriormente, o template precisa de aprovação humana antes de entrar em produção em escala — para garantir alinhamento estratégico e qualidade do formato.
- [ ] **HITL** — Decisões de redirects e exclusão de conteúdo: qualquer ação que envolva deletar, redirecionar ou desindexar páginas existentes (especialmente com tráfego ou backlinks) é sempre humana — reversibilidade zero para ações de remoção de conteúdo já indexado.

## Veredito

- **APROVADO** — todos os itens com evidência.
- **REPROVADO** — pelo menos um item falhou; feedback específico obrigatório por item.
- **BLOQUEADO** — condição de gate humano pendente.

_Gerado em 2026-09-16._
