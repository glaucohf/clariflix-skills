# incident-response-squad

فريق متخصص في الاستجابة للحوادث لـ DevOps/SRE.

## نظرة عامة

**incident-response-squad** هو فريق كامل يغطي خط أنابيب الاستجابة للحوادث بالكامل:

1. **تحليل السجلات** — تجميع وتحليل السجلات من مصادر متعددة (CloudWatch، ELK، Splunk، Datadog)
2. **ربط السبب الجذري** — ربط الإشارات من 20-45 أداة مراقبة، تعيين نطاق التأثير
3. **تنفيذ دفاتر التشغيل** — دفاتر تشغيل آلية للتراجع والتوسع وإعادة التشغيل والمعالجة
4. **اتصال الحالة** — تحديث صفحات الحالة وإخطار أصحاب المصلحة
5. **تقرير ما بعد الحادث** — إنشاء وثائق بدون لوم مع جدول زمني وبنود عمل ودروس مستفادة

**نقطة الألم:** يُنفق 65% من وقت الحل في تشخيص السبب الجذري؛ تدير الشركات 20-45 أداة مراقبة.

## الوكلاء

| الوكيل | المعرّف | الدور |
|---|---|---|
| 📋 LogAnalyzer | `log-analyzer` | محلل سجلات متعدد المصادر |
| 🔍 Correlator | `root-cause-correlator` | مُرتبط السبب الجذري ومُعيّن نطاق التأثير |
| ⚡ RunbookExec | `runbook-executor` | منفذ دفاتر تشغيل المعالجة |
| 📢 StatusUpdater | `status-page-updater` | مدير الاتصال وصفحة الحالة |
| 📝 PostMortem | `postmortem-writer` | مُنشئ تقارير ما بعد الحادث بدون لوم |

## سير العمل

| سير العمل | الأمر | الوصف | المدة |
|---|---|---|---|
| استجابة كاملة للحوادث | `*respond-incident` | خط أنابيب كامل: من التنبيه إلى تقرير ما بعد الحادث | 30-90 دقيقة |
| فرز سريع | `*triage-incident` | فرز سريع: تحليل، سبب جذري، اتصال | 10-20 دقيقة |

## الأوامر المتاحة

| الأمر | الوكيل | الوصف |
|---|---|---|
| `*analyze-logs` | LogAnalyzer | تحليل سجلات الحادث |
| `*search-logs` | LogAnalyzer | البحث عن نمط محدد في السجلات |
| `*correlate-signals` | Correlator | ربط إشارات من مصادر متعددة |
| `*find-root-cause` | Correlator | تحديد السبب الجذري الأكثر احتمالاً |
| `*execute-runbook` | RunbookExec | تنفيذ دفتر تشغيل المعالجة |
| `*list-runbooks` | RunbookExec | سرد دفاتر التشغيل المتاحة |
| `*update-status` | StatusUpdater | تحديث صفحة الحالة |
| `*notify-stakeholders` | StatusUpdater | إخطار أصحاب المصلحة |
| `*write-postmortem` | PostMortem | إنشاء تقرير ما بعد الحادث بدون لوم |
| `*generate-timeline` | PostMortem | إنشاء الجدول الزمني للحادث |

## البداية السريعة

```
# تفعيل المُرتبط (المُنسق الرئيسي)
/irs:agents:root-cause-correlator

# خط أنابيب استجابة كاملة للحوادث
*respond-incident

# فرز سريع
*triage-incident

# تحليل السجلات فقط
*analyze-logs

# تقرير ما بعد الحادث فقط
*write-postmortem
```

## المستخدمون المستهدفون

- مهندسو موثوقية الموقع (SRE)
- مهندسو DevOps
- مهندسو الاستدعاء (on-call)
- المدراء التقنيون والقادة التقنيون

## المتطلبات

- الوصول إلى أدوات المراقبة (Datadog، Prometheus، Grafana)
- الوصول إلى منصات السجلات (ELK، Splunk، CloudWatch)
- الوصول إلى صفحة الحالة (Statuspage.io، Atlassian)
- قناة اتصال مُكوّنة (Slack #incidents)

## التأليف

Luiz Gustavo Vieira Rodrigues — Squad Protocol v5.
