---
task: integrateCRM()
agent: ce-integrator
description: "EXCLUSIVO: integração com CRM (HubSpot / ActiveCampaign / RD Station) — sync de leads, tags, pipelines"
elicit: true
responsavel: "Link"
responsavel_type: Agente
atomic_layer: Organism

Entrada:
  - nome: crmConfig
    tipo: object
    obrigatorio: true
    descricao: "API key e configuração do CRM (HubSpot/ActiveCampaign/RD Station)"

Saida:
  - nome: crmIntegration
    tipo: file
    obrigatorio: true
    descricao: "Integração CRM com sync de leads, tags e pipelines"

Checklist:
  pre-conditions:
    - "[ ] CRM escolhido e API key disponível"
  post-conditions:
    - "[ ] Leads sincronizando para CRM"
    - "[ ] Tags automáticas configuradas"
    - "[ ] Pipeline de vendas mapeado"
---

# Task: integrateCRM()

## Objetivo
Integrar a landing page com o CRM do cliente para sincronização automática de leads, aplicação de tags e atribuição ao pipeline correto. A integração CRM elimina trabalho manual, garante que nenhum lead se perca e permite rastreamento completo do ciclo de vida do cliente — desde o primeiro clique até o fechamento.

## Inputs Necessários
- `scope.md` (flag `crm` ativa, CRM escolhido)
- Credenciais da API do CRM (API Key, URL da conta)
- `funnel-map.md` (pipeline e estágios definidos)
- `requirements.md` (Q12 sobre ferramentas — qual CRM o cliente já usa)
- Definição de tags a aplicar no momento da conversão (fonte, produto, campanha)

## Processo
1. **Elicitação de configuração** — Identificar CRM e coletar credenciais:
   - **HubSpot:** API Key + Portal ID + Pipeline ID + Stage IDs
   - **ActiveCampaign:** API URL + API Key + List ID + Tag IDs
   - **RD Station:** Client ID + Client Secret + OAuth2 token

2. **Abstração de CRM** — Criar interface comum para múltiplos CRMs:
   ```python
   # src/services/crm/base.py
   from abc import ABC, abstractmethod

   class CRMProvider(ABC):
       @abstractmethod
       async def create_contact(self, lead: Lead) -> str:
           """Retorna ID do contato criado no CRM"""

       @abstractmethod
       async def add_tags(self, contact_id: str, tags: list[str]) -> bool:
           pass

       @abstractmethod
       async def add_to_pipeline(self, contact_id: str, pipeline_id: str, stage_id: str) -> bool:
           pass

       @abstractmethod
       async def update_contact(self, contact_id: str, properties: dict) -> bool:
           pass
   ```

3. **Integração HubSpot** — `src/services/crm/hubspot.py`:
   ```python
   import httpx

   class HubSpotCRM(CRMProvider):
       BASE = "https://api.hubapi.com"

       async def create_contact(self, lead: Lead) -> str:
           async with httpx.AsyncClient() as client:
               response = await client.post(
                   f"{self.BASE}/crm/v3/objects/contacts",
                   headers={"Authorization": f"Bearer {settings.HUBSPOT_API_KEY}"},
                   json={
                       "properties": {
                           "email": lead.email,
                           "firstname": lead.name.split()[0],
                           "lastname": ' '.join(lead.name.split()[1:]) if len(lead.name.split()) > 1 else '',
                           "phone": lead.phone or '',
                           "company": lead.company or '',
                           "hs_lead_status": "NEW",
                           "lifecyclestage": "lead",
                           # UTM params como propriedades customizadas
                           "utm_source_first": lead.source or '',
                           "utm_campaign_first": lead.campaign or '',
                           "landing_page_url": lead.landing_page or '',
                       }
                   }
               )
               data = response.json()
               return data.get("id", "")

       async def create_deal(self, contact_id: str, lead: Lead) -> str:
           """Criar deal/oportunidade no pipeline automaticamente"""
           async with httpx.AsyncClient() as client:
               response = await client.post(
                   f"{self.BASE}/crm/v3/objects/deals",
                   headers={"Authorization": f"Bearer {settings.HUBSPOT_API_KEY}"},
                   json={
                       "properties": {
                           "dealname": f"{lead.name} — {lead.source or 'Direct'}",
                           "pipeline": settings.HUBSPOT_PIPELINE_ID,
                           "dealstage": settings.HUBSPOT_STAGE_NEW_LEAD,
                           "amount": 0,
                       },
                       "associations": [{"to": {"id": contact_id}, "types": [{"associationCategory": "HUBSPOT_DEFINED", "associationTypeId": 3}]}]
                   }
               )
               return response.json().get("id", "")
   ```

4. **Integração ActiveCampaign** — `src/services/crm/activecampaign.py`:
   ```python
   class ActiveCampaignCRM(CRMProvider):
       async def create_contact(self, lead: Lead) -> str:
           async with httpx.AsyncClient() as client:
               response = await client.post(
                   f"{settings.AC_API_URL}/api/3/contacts",
                   headers={"Api-Token": settings.AC_API_KEY},
                   json={
                       "contact": {
                           "email": lead.email,
                           "firstName": lead.name.split()[0],
                           "lastName": ' '.join(lead.name.split()[1:]),
                           "phone": lead.phone or '',
                       }
                   }
               )
               return response.json().get("contact", {}).get("id", "")

       async def add_to_list(self, contact_id: str, list_id: str) -> bool:
           async with httpx.AsyncClient() as client:
               response = await client.post(
                   f"{settings.AC_API_URL}/api/3/contactLists",
                   headers={"Api-Token": settings.AC_API_KEY},
                   json={"contactList": {"contact": contact_id, "list": list_id, "status": 1}}
               )
               return response.status_code == 201
   ```

5. **Integração RD Station** — `src/services/crm/rdstation.py`:
   ```python
   class RDStationCRM(CRMProvider):
       async def create_contact(self, lead: Lead) -> str:
           # RD Station usa webhook format para leads
           async with httpx.AsyncClient() as client:
               response = await client.post(
                   f"https://api.rd.services/platform/contacts",
                   headers={"Authorization": f"Bearer {settings.RD_ACCESS_TOKEN}"},
                   json={
                       "contact": {
                           "name": lead.name,
                           "email": lead.email,
                           "mobile_phone": lead.phone,
                           "tags": [f"utm_{lead.source}", "landing-page"],
                           "cf_landing_page": lead.landing_page,
                       }
                   }
               )
               return response.json().get("uuid", "")
   ```

6. **Factory e dispatcher** — `src/services/crm/factory.py`:
   ```python
   def get_crm_provider() -> CRMProvider:
       providers = {
           "hubspot": HubSpotCRM,
           "activecampaign": ActiveCampaignCRM,
           "rdstation": RDStationCRM,
       }
       provider_class = providers.get(settings.CRM_PROVIDER)
       if not provider_class:
           return None  # CRM não configurado — graceful degradation
       return provider_class()

   async def sync_lead_to_crm(lead: Lead):
       crm = get_crm_provider()
       if not crm:
           return
       try:
           contact_id = await crm.create_contact(lead)
           if contact_id:
               await crm.add_tags(contact_id, [f"source:{lead.source}", "lp-conversion"])
               if hasattr(crm, 'create_deal'):
                   await crm.create_deal(contact_id, lead)
       except Exception as e:
           logger.error(f"CRM sync failed for lead {lead.id}: {e}")
           # Não falhar a conversão por erro de CRM
   ```

## Veto Conditions
- Falha de CRM bloqueando a conversão do lead → isolar em try/except com graceful degradation
- Dados de lead enviados ao CRM sem validação prévia → validar antes de sincronizar
- CRM sem retry em caso de falha de rede → implementar retry com backoff

## Output Esperado
- Abstração `CRMProvider` com interface comum
- Implementações para HubSpot, ActiveCampaign e RD Station
- Factory para seleção do provider via env var
- Sincronização automática de lead após conversão
- Graceful degradation (falha de CRM não falha a conversão)

## Completion Criteria
- [ ] Interface CRMProvider definida
- [ ] CRM do cliente implementado (HubSpot OU ActiveCampaign OU RD Station)
- [ ] Sincronização de campos: email, nome, telefone, UTM params, URL da LP
- [ ] Tags aplicadas no momento da conversão
- [ ] Pipeline/deal criado automaticamente (se CRM suportar)
- [ ] Graceful degradation: falha de CRM não quebra conversão de lead
- [ ] Retry com backoff para falhas de rede
- [ ] Teste de sincronização com lead real verificado no CRM
