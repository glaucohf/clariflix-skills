<div align="center">

# token-optimizer

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge)
![Agents](https://img.shields.io/badge/agents-5-purple?style=for-the-badge)
![Tasks](https://img.shields.io/badge/tasks-5-orange?style=for-the-badge)
![Workflows](https://img.shields.io/badge/workflows-2-green?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-brightgreen?style=for-the-badge)
![AIOS](https://img.shields.io/badge/AIOS-≥2.1.0-red?style=for-the-badge)

**मौजूदा AIOS squads का विश्लेषण करता है और ROI के अनुसार प्राथमिकता वाले अनुकूलन प्रदान करता है — गुणवत्ता, गति, और टोकन बचत।**

5 एजेंट का अनुक्रमिक pipeline जो TOKEN-OPTIMIZATION-GUIDE.md को ज्ञान आधार के रूप में उपयोग करते हुए स्कैन, anti-patterns का पता लगाना, योजना बनाना, निष्पादन और ऑडिट करता है।

`/sqopt`

</div>

---

## क्या आपका squad जरूरत से 10 गुना ज्यादा टोकन खर्च कर रहा है?

आपने एक काम करने वाला squad बनाया है। यह चलता है, परिणाम देता है, समस्या हल करता है। लेकिन हर निष्पादन की लागत **$0.28** है और आप जानते हैं कि आधे टोकन दोहराए गए prompts, बेकार के विस्तृत रिटर्न जो कोई पढ़ता नहीं, और Opus द्वारा Haiku का काम करने में बर्बाद हो रहे हैं।

सबसे बुरी बात? आप नहीं जानते कि **कहाँ** अड़चनें हैं। दर्जनों फाइलें, कई एजेंट, जुड़े हुए workflows — और हर एक में नंगी आँखों से अदृश्य anti-patterns छिपे हैं। Context Bloat, Double-Read, Ghost Tokens, Model Overkill। लागत चुपचाप बढ़ती रहती है, एक निष्पादन के बाद दूसरा।

क्या हो अगर मैं आपको बताऊँ कि **12 प्रमाणित तकनीकें** आपकी लागत को 78% तक कम कर सकती हैं, आउटपुट गुणवत्ता 34% बढ़ा सकती हैं, और यह सब स्वचालित रूप से लागू किया जा सकता है — बिना कुछ तोड़े?

---

## पहले और बाद में

| | अनुकूलन के बिना | token-optimizer के साथ |
|---|---|---|
| **Opus टोकन** | 100% | 2-5% (Router Puro) |
| **प्रति निष्पादन लागत** | $0.28 | $0.06 (-78%) |
| **आउटपुट गुणवत्ता** | 6.5/10 | 8.7/10 (+34%) |
| **पहचाने गए Anti-patterns** | 0 | 100% सूचीबद्ध |

---

## यह कैसे काम करता है

```
[/sqopt] --> [Scanner] --> [Detector] --> [Planner] --> [Executor] --> [Auditor] --> [Report]
```

पूरा pipeline 5 अनुक्रमिक चरणों से गुजरता है। प्रत्येक एजेंट पिछले एजेंट का आउटपुट फाइल के माध्यम से पढ़ता है (Files as Contracts), ऑर्केस्ट्रेटर को केवल `"Done: {path}"` लौटाता है, और अगला एजेंट वहीं से शुरू करता है जहाँ पिछला रुका था। ट्रांजिशन में शून्य टोकन बर्बाद।

---

## token-optimizer क्यों?

- **12 प्रमाणित तकनीकें** — अनुमान नहीं। प्रत्येक अनुकूलन TOKEN-OPTIMIZATION-GUIDE.md के एक क्रमांकित खंड से मैप किया गया है, तकनीकी तर्क और प्रलेखित प्रभाव मेट्रिक्स के साथ।

- **ROI-प्रथम प्राथमिकता** — पहले गुणवत्ता, दूसरे गति, तीसरे लागत। प्लानर कार्यों को सबसे अधिक वास्तविक रिटर्न के अनुसार क्रमबद्ध करता है, सबसे आसान कटौती के अनुसार नहीं। आप लागत घटाने से पहले आउटपुट सुधारते हैं।

- **10+ anti-patterns का स्वचालित पता लगाना** — Context Bloat, Double-Read, Model Overkill, Compression Rebound, Ghost Tokens, Sequential Launch, Fat Orchestrator — प्रत्येक को 1-10 की गंभीरता स्कोरिंग और अनुमानित बर्बाद टोकन के साथ।

- **Audit-only मोड** — केवल निदान चाहते हैं बिना किसी फाइल को बदले? `squad_audit_only` workflow स्कैन करता है, पता लगाता है, और रिपोर्ट करता है — शून्य परिवर्तन, पूर्ण दृश्यता।

---

## एजेंट

| | नाम | Archetype | भूमिका |
|---|---|---|---|
| | **SquadScanner** | Guardian | लक्ष्य squad की पूरी संरचना पढ़ता और सूचीबद्ध करता है, एक संरचित सूची बनाता है |
| | **AntiPatternDetector** | Guardian | टोकन anti-patterns की पहचान करता है, गंभीरता स्कोर और अनुमानित प्रभाव के साथ |
| | **OptimizationPlanner** | Balancer | ROI के अनुसार प्राथमिकता वाली अनुकूलन योजना बनाता है, anti-patterns को प्रमाणित तकनीकों से जोड़ता है |
| | **OptimizationExecutor** | Builder | योजना को निष्पादित करता है, squad फाइलों के अनुकूलित संस्करण लिखता है |
| | **QualityAuditor** | Guardian | अनुकूलित squad को मान्य करता है, पहले/बाद मेट्रिक्स की तुलना करता है, AIOS compliance सुनिश्चित करता है |

---

## कार्य

| Task | जिम्मेदार एजेंट | Atomic Layer |
|---|---|---|
| `scanSquad()` | SquadScanner | लक्ष्य squad को स्कैन करता है और squad-inventory.json बनाता है |
| `detectAntiPatterns()` | AntiPatternDetector | सूची को गाइड की anti-pattern सूची से क्रॉस-रेफरेंस करता है |
| `planOptimization()` | OptimizationPlanner | ROI के अनुसार प्राथमिकता वाली योजना बनाता है, atomic क्रियाओं के साथ |
| `executeOptimization()` | OptimizationExecutor | अनुकूलन लागू करता है और optimized/ में फाइलें बनाता है |
| `auditQuality()` | QualityAuditor | AIOS compliance मान्य करता है और before/after रिपोर्ट बनाता है |

---

## Workflows

| नाम | पैटर्न | विवरण |
|---|---|---|
| `squad_optimization_pipeline` | Sequential Pipeline | पूरा pipeline: scan, detect, plan, execute, audit |
| `squad_audit_only` | Sequential Pipeline (shortcut) | त्वरित ऑडिट: scan, detect, audit — फाइलों में कोई बदलाव नहीं |

---

## कमांड

| कमांड | क्या करता है |
|---|---|
| `/sqopt` | कॉन्फ़िगरेशन संग्रह के साथ इंटरैक्टिव pipeline शुरू करता है |
| `/sqopt:run` | बिना सवालों के सीधा निष्पादन |
| `*sqopt-scan` | लक्ष्य squad को स्कैन करता है और JSON सूची बनाता है |
| `*sqopt-detect` | Anti-patterns का पता लगाता है और गंभीरता रिपोर्ट बनाता है |
| `*sqopt-plan` | ROI के अनुसार प्राथमिकता वाली अनुकूलन योजना बनाता है |
| `*sqopt-execute` | squad फाइलों पर नियोजित अनुकूलन लागू करता है |
| `*sqopt-audit` | अनुकूलित squad का ऑडिट करता है और मेट्रिक्स रिपोर्ट बनाता है |

---

## Tech Stack

| प्रौद्योगिकी | उपयोग |
|---|---|
| **Claude Code Agent Teams** | Haiku/Sonnet/Opus रूटिंग के साथ मल्टी-एजेंट ऑर्केस्ट्रेशन |
| **AIOS 2.1+** | Squad फ्रेमवर्क — agents, tasks, workflows के लिए मानक प्रारूप |
| **Markdown/YAML** | एजेंट, कार्य, workflow, और कॉन्फ़िगरेशन परिभाषाएँ |
| **JSON** | Files as Contracts — संरचित फाइलों के माध्यम से अंतर-एजेंट संचार |

---

<details>
<summary><strong>अक्सर पूछे जाने वाले प्रश्न</strong></summary>

### क्या यह किसी भी squad के साथ काम करता है?

हाँ। token-optimizer मानक AIOS प्रारूप में किसी भी squad का विश्लेषण करता है। बस डायरेक्टरी पथ की ओर इंगित करें और स्कैनर स्वचालित रूप से सभी agents, tasks, workflows, और configs को सूचीबद्ध करता है। डोमेन कोई मायने नहीं रखता — अगर यह AIOS प्रारूप का पालन करता है, तो इसे अनुकूलित किया जा सकता है।

### क्या यह मेरी फाइलें बदलता है?

चुने गए मोड पर निर्भर करता है। पूरे pipeline (`squad_optimization_pipeline`) में, executor अलग `optimized/` डायरेक्टरी में अनुकूलित संस्करण बनाता है — आपकी मूल फाइलें कभी ओवरराइट नहीं होतीं। `squad_audit_only` मोड में, यह 100% read-only है: केवल निदान और रिपोर्ट, शून्य परिवर्तन।

### कितनी बचत होती है?

पाए गए anti-patterns के आधार पर 65% से 98% टोकन कमी। सबसे सामान्य मामला — Model Overkill और Context Bloat वाले squads — आमतौर पर प्रति निष्पादन लागत में 78% की कमी दिखाता है। QualityAuditor की अंतिम रिपोर्ट टोकन, लागत, और विलंबता के लिए विस्तृत पहले/बाद अनुमान दिखाती है।

</details>

---

<div align="center">

**[NSCL Pipeline](https://github.com/nscl-pipeline) द्वारा निर्मित** · MIT License

`token-optimization` · `squad-analysis` · `anti-pattern-detection` · `cost-reduction` · `quality-improvement` · `aios`

[squads.sh](https://squads.sh)

</div>
