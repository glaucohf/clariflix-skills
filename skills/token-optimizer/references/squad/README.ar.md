<div align="center" dir="rtl">

# token-optimizer

![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge)
![Agents](https://img.shields.io/badge/agents-5-purple?style=for-the-badge)
![Tasks](https://img.shields.io/badge/tasks-5-orange?style=for-the-badge)
![Workflows](https://img.shields.io/badge/workflows-2-green?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-brightgreen?style=for-the-badge)
![AIOS](https://img.shields.io/badge/AIOS-≥2.1.0-red?style=for-the-badge)

**يحلل فرق AIOS الحالية وينتج تحسينات مرتبة حسب العائد على الاستثمار — الجودة، السرعة، وتوفير التوكنات.**

خط أنابيب تسلسلي من 5 وكلاء يقوم بالمسح، كشف anti-patterns، التخطيط، التنفيذ، والتدقيق باستخدام TOKEN-OPTIMIZATION-GUIDE.md كقاعدة معرفية.

`/sqopt`

</div>

---

## هل يستهلك فريقك 10 أضعاف التوكنات المطلوبة؟

لقد بنيت فريقاً يعمل. ينفّذ، يسلّم النتائج، يحل المشكلة. لكن كل تنفيذ يكلف **$0.28** وأنت تعلم أن نصف تلك التوكنات تُهدر في prompts متكررة، مخرجات مطوّلة لا يقرأها أحد، و Opus يقوم بعمل Haiku.

الأسوأ؟ لا تعرف **أين** تكمن الاختناقات. عشرات الملفات، وكلاء متعددون، workflows متسلسلة — وكل منها يخفي anti-patterns غير مرئية بالعين المجردة. Context Bloat، Double-Read، Ghost Tokens، Model Overkill. التكلفة تتراكم بصمت، تنفيذاً بعد تنفيذ.

ماذا لو أخبرتك أن **12 تقنية مثبتة** يمكنها خفض تكلفتك بنسبة تصل إلى 78%، ورفع جودة المخرجات بنسبة 34%، وكل ذلك يمكن تطبيقه تلقائياً — دون كسر أي شيء؟

---

## قبل وبعد

| | بدون تحسين | مع token-optimizer |
|---|---|---|
| **توكنات Opus** | 100% | 2-5% (Router Puro) |
| **التكلفة لكل تنفيذ** | $0.28 | $0.06 (-78%) |
| **جودة المخرجات** | 6.5/10 | 8.7/10 (+34%) |
| **Anti-patterns المكتشفة** | 0 | 100% مفهرسة |

---

## كيف يعمل

```
[/sqopt] --> [Scanner] --> [Detector] --> [Planner] --> [Executor] --> [Auditor] --> [Report]
```

يمر خط الأنابيب الكامل بـ 5 مراحل تسلسلية. كل وكيل يقرأ مخرجات السابق عبر ملف (Files as Contracts)، يعيد فقط `"Done: {path}"` إلى المنسّق، والوكيل التالي يستمر من حيث توقف السابق. صفر توكنات مهدرة في الانتقالات.

---

## لماذا token-optimizer؟

- **12 تقنية مثبتة** — ليس تخميناً. كل تحسين مربوط بقسم مرقّم في TOKEN-OPTIMIZATION-GUIDE.md، مع أساس تقني ومقاييس تأثير موثقة.

- **ترتيب حسب العائد على الاستثمار** — الجودة أولاً، السرعة ثانياً، التكلفة ثالثاً. يرتب المخطط الإجراءات حسب أعلى عائد حقيقي، وليس أسهل تخفيض. تحسّن المخرجات قبل خفض التكاليف.

- **كشف تلقائي لأكثر من 10 anti-patterns** — Context Bloat، Double-Read، Model Overkill، Compression Rebound، Ghost Tokens، Sequential Launch، Fat Orchestrator — كل منها بتقييم شدة 1-10 وتقدير للتوكنات المهدرة.

- **وضع audit-only** — تريد تشخيصاً فقط دون تعديل أي ملف؟ workflow الـ `squad_audit_only` يمسح، يكتشف، ويقدم تقريراً — صفر تغييرات، رؤية كاملة.

---

## الوكلاء

| | الاسم | النموذج الأصلي | الدور |
|---|---|---|---|
| | **SquadScanner** | Guardian | يقرأ ويفهرس البنية الكاملة لفريق مستهدف، منتجاً جرداً منظماً |
| | **AntiPatternDetector** | Guardian | يحدد anti-patterns التوكنات مع تقييمات الشدة والتأثير المقدّر |
| | **OptimizationPlanner** | Balancer | ينشئ خطة تحسين مرتبة حسب العائد، تربط anti-patterns بتقنيات مثبتة |
| | **OptimizationExecutor** | Builder | ينفذ الخطة، يعيد كتابة نسخ محسّنة من ملفات الفريق |
| | **QualityAuditor** | Guardian | يتحقق من الفريق المحسّن، يقارن المقاييس قبل/بعد، ويضمن compliance AIOS |

---

## المهام

| المهمة | الوكيل المسؤول | الطبقة الذرية |
|---|---|---|
| `scanSquad()` | SquadScanner | يمسح الفريق المستهدف وينتج squad-inventory.json |
| `detectAntiPatterns()` | AntiPatternDetector | يقاطع الجرد مع قائمة anti-patterns من الدليل |
| `planOptimization()` | OptimizationPlanner | يولّد خطة مرتبة حسب العائد بإجراءات ذرية |
| `executeOptimization()` | OptimizationExecutor | يطبق التحسينات وينتج ملفات في optimized/ |
| `auditQuality()` | QualityAuditor | يتحقق من compliance AIOS وينتج تقرير before/after |

---

## سير العمل

| الاسم | النمط | الوصف |
|---|---|---|
| `squad_optimization_pipeline` | Sequential Pipeline | خط أنابيب كامل: scan، detect، plan، execute، audit |
| `squad_audit_only` | Sequential Pipeline (shortcut) | تدقيق سريع: scan، detect، audit — بدون تعديل ملفات |

---

## الأوامر

| الأمر | ماذا يفعل |
|---|---|
| `/sqopt` | يبدأ خط الأنابيب التفاعلي مع جمع الإعدادات |
| `/sqopt:run` | تنفيذ مباشر بدون أسئلة |
| `*sqopt-scan` | يمسح الفريق المستهدف وينتج جرد JSON |
| `*sqopt-detect` | يكتشف anti-patterns وينتج تقرير الشدة |
| `*sqopt-plan` | يولّد خطة تحسين مرتبة حسب العائد |
| `*sqopt-execute` | يطبق التحسينات المخططة على ملفات الفريق |
| `*sqopt-audit` | يدقق الفريق المحسّن ويولّد تقرير المقاييس |

---

## المكدس التقني

| التقنية | الاستخدام |
|---|---|
| **Claude Code Agent Teams** | تنسيق متعدد الوكلاء مع توجيه Haiku/Sonnet/Opus |
| **AIOS 2.1+** | إطار الفرق — تنسيق قياسي لـ agents، tasks، workflows |
| **Markdown/YAML** | تعريف الوكلاء، المهام، سير العمل، والإعدادات |
| **JSON** | Files as Contracts — تواصل بين الوكلاء عبر ملفات منظمة |

---

<details>
<summary><strong>الأسئلة الشائعة</strong></summary>

### هل يعمل مع أي فريق؟

نعم. token-optimizer يحلل أي فريق بتنسيق AIOS القياسي. فقط وجّهه إلى مسار المجلد وسيقوم الماسح بفهرسة جميع agents، tasks، workflows، والإعدادات تلقائياً. لا يهم المجال — إذا اتبع تنسيق AIOS، يمكن تحسينه.

### هل يعدّل ملفاتي؟

يعتمد على الوضع المختار. في خط الأنابيب الكامل (`squad_optimization_pipeline`)، ينتج المنفذ نسخاً محسّنة في مجلد منفصل `optimized/` — ملفاتك الأصلية لا تُستبدل أبداً. في وضع `squad_audit_only`، هو 100% للقراءة فقط: تشخيص وتقرير فقط، صفر تغييرات.

### كم يوفر؟

بين 65% و98% تخفيض في التوكنات، حسب anti-patterns المكتشفة. الحالة الأكثر شيوعاً — فرق تعاني من Model Overkill و Context Bloat — عادةً تشهد تخفيضاً بنسبة 78% في التكلفة لكل تنفيذ. التقرير النهائي من QualityAuditor يعرض توقعات مفصلة للتوكنات، التكلفة، ووقت الاستجابة قبل/بعد.

</details>

---

<div align="center">

**أنشأه [NSCL Pipeline](https://github.com/nscl-pipeline)** · MIT License

`token-optimization` · `squad-analysis` · `anti-pattern-detection` · `cost-reduction` · `quality-improvement` · `aios`

[squads.sh](https://squads.sh)

</div>
