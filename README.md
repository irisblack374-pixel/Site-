<div align="center">
<img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="76" alt="Site icon">
<h1>Site-</h1>
<p><b>Discord Bot • Python • discord.py</b></p>
<p>بوت ديسكورد بسيط وسهل التعديل، يحتوي على أوامر معلومات وإدارة أساسية.</p>
</div>

---

## <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="28" align="absmiddle"> ما هو البوت؟

**Site-** هو بوت Discord مكتوب بلغة **Python** باستخدام مكتبة **discord.py**.

الفكرة بسيطة: تشغّل البوت، تضيفه إلى سيرفرك، وبعدها تظهر لك أوامر Slash تبدأ بـ `/` مثل:

```
/ping
/server
/user
/avatar
/help
/clear
/kick
/ban
/unban
```

لا تحتاج تعرف برمجة حتى تشغله. كل خطوات التشغيل موجودة بالأسفل.

---

## <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/commands.svg" width="28" align="absmiddle"> الأوامر بالتفصيل

### <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/commands.svg" width="20" align="absmiddle"> `/ping` — سرعة البوت

يعرض سرعة استجابة البوت بالـ milliseconds.

مثال:

```
/ping
↓
Pong! 82ms
```

كلما كان الرقم أقل، فهذا يعني أن استجابة البوت في تلك اللحظة أسرع.

---

### <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="20" align="absmiddle"> `/server` — معلومات السيرفر

يعرض معلومات أساسية عن السيرفر الذي استخدمت فيه الأمر:

- اسم السيرفر
- عدد الأعضاء
- ID السيرفر

يعمل داخل السيرفر فقط.

---

### <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/cat.svg" width="20" align="absmiddle"> `/user` — معلومات عضو

يعرض معلومات العضو الذي تختاره.

إذا لم تختَر عضوًا، يعرض معلوماتك أنت.

يعرض:

- اسم العرض
- ID العضو
- تاريخ انضمامه للسيرفر عندما تكون المعلومة متاحة

مثال:

```
/user
```

أو تختار عضوًا من خانة **member**.

---

### <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="20" align="absmiddle"> `/avatar` — صورة العضو

يعرض رابط صورة الحساب للعضو الذي تختاره.

إذا لم تحدد عضوًا، يستخدم حسابك أنت.

مثال:

```
/avatar
```

---

### <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/ai.svg" width="20" align="absmiddle"> `/help` — قائمة الأوامر

يعرض لك قائمة مختصرة بأوامر البوت الموجودة حاليًا.

إذا نسيت أمرًا، استخدم:

```
/help
```

---

### <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/commands.svg" width="20" align="absmiddle"> `/clear` — حذف رسائل

يستخدم لحذف عدد محدد من الرسائل في القناة.

مثال:

```
/clear amount: 20
```

يمكن حذف من **1 إلى 100 رسالة** في العملية الواحدة.

<img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="20" align="absmiddle"> الأمر مخصص لمن لديهم صلاحية **Manage Messages**.

---

### <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="20" align="absmiddle"> `/kick` — طرد عضو

يطرد عضوًا من السيرفر مع إمكانية كتابة سبب.

مثال:

```
/kick member: @User reason: مخالفة القوانين
```

<img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="20" align="absmiddle"> يحتاج المستخدم إلى صلاحية **Kick Members**.

---

### <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="20" align="absmiddle"> `/ban` — حظر عضو

يحظر عضوًا من السيرفر مع إمكانية كتابة سبب.

مثال:

```
/ban member: @User reason: مخالفة القوانين
```

<img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="20" align="absmiddle"> يحتاج المستخدم إلى صلاحية **Ban Members**.

---

### <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="20" align="absmiddle"> `/unban` — فك حظر

يفك حظر مستخدم باستخدام **User ID**.

مثال:

```
/unban user_id: 123456789012345678
```

<img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="20" align="absmiddle"> يحتاج المستخدم إلى صلاحية **Ban Members**.

---

## <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/python.svg" width="28" align="absmiddle"> ماذا يستخدم البوت؟

| التقنية | وظيفتها |
|---|---|
| <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/python.svg" width="20" align="absmiddle"> Python | لغة برمجة البوت |
| 🔷 discord.py | ربط Python مع Discord |
| <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="20" align="absmiddle"> python-dotenv | قراءة التوكن من ملف `.env` |
| <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/commands.svg" width="20" align="absmiddle"> Slash Commands | الأوامر التي تبدأ بـ `/` |

---

## <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="28" align="absmiddle"> ملفات المشروع

```
Site-/
│
├── bot.py
├── requirements.txt
├── .env
└── README.md
```

### <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="20" align="absmiddle"> `bot.py`

هذا هو **ملف البوت الرئيسي**.

داخله موجود:

- الاتصال بـ Discord
- أوامر البوت
- الصلاحيات المطلوبة للأوامر
- رسائل الاستجابة
- تشغيل البوت

### <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="20" align="absmiddle"> `requirements.txt`

هذا الملف يخبر Python بالمكتبات التي يحتاجها المشروع.

المشروع يستخدم:

```
discord.py
python-dotenv
```

### <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="20" align="absmiddle"> `.env`

هذا الملف مخصص لوضع **Bot Token**.

يكون بهذا الشكل:

```env
DISCORD_TOKEN=ضع_توكن_البوت_هنا
```

⚠️ **لا ترسل التوكن لأي شخص ولا ترفعه إلى GitHub.**

### <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="20" align="absmiddle"> `README.md`

هذا الملف هو الشرح الموجود في GitHub.

---

# <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="20" align="absmiddle"> تشغيل البوت للمبتدئين

إذا ما تعرف برمجة، اتبع الخطوات بالترتيب.

## <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/commands.svg" width="20" align="absmiddle"> ثبّت Python

حمّل Python من الموقع الرسمي:

https://www.python.org/downloads/

بعد التثبيت افتح Terminal أو CMD واكتب:

```bash
python --version
```

إذا ظهر رقم مثل:

```
Python 3.x.x
```

فـ Python جاهز.

---

## <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/commands.svg" width="20" align="absmiddle"> حمّل المشروع

من GitHub اضغط:

**Code → Download ZIP**

بعدها فك ضغط الملف في مكان واضح، مثل سطح المكتب.

ستجد مجلد:

```
Site-
```

---

## <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/commands.svg" width="20" align="absmiddle"> افتح Terminal داخل مجلد المشروع

افتح مجلد `Site-`.

ثم افتح Terminal/CMD داخل نفس المجلد.

يجب أن تكون الملفات أمامك مثل:

```
bot.py
requirements.txt
README.md
```

---

## <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/commands.svg" width="20" align="absmiddle"> ثبّت المكتبات

داخل Terminal اكتب:

```bash
pip install -r requirements.txt
```

انتظر حتى ينتهي التثبيت.

إذا ظهر:

```
Successfully installed
```

فهذا يعني أن المكتبات تم تثبيتها.

---

## <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/commands.svg" width="20" align="absmiddle"> أنشئ ملف `.env`

داخل مجلد `Site-` أنشئ ملفًا اسمه بالضبط:

```
.env
```

ثم ضع داخله:

```env
DISCORD_TOKEN=توكن_البوت_هنا
```

مثال شكلي فقط:

```env
DISCORD_TOKEN=YOUR_BOT_TOKEN
```

⚠️ لا تستخدم المثال نفسه. ضع **التوكن الحقيقي للبوت**.

---

# <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="20" align="absmiddle"> من أين أحصل على Bot Token؟

اذهب إلى **Discord Developer Portal** وأنشئ Application ثم Bot.

بعد إنشاء البوت:

**Bot → Token → Reset Token / Copy**

ثم ضع التوكن داخل `.env`.

⚠️ التوكن مثل كلمة مرور البوت. لا تنشره في GitHub أو Discord أو ترسله لأحد.

إذا انكشف التوكن، غيّره من Developer Portal فورًا.

---

# <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/ai.svg" width="20" align="absmiddle"> إضافة البوت إلى السيرفر

بعد إنشاء البوت، تحتاج إلى دعوته إلى السيرفر.

من **Discord Developer Portal**:

```
OAuth2
↓
URL Generator
```

اختر:

**Scopes**
- `bot`
- `applications.commands`

ثم اختر الصلاحيات التي يحتاجها البوت.

لأن المشروع يحتوي على أوامر إدارة مثل `clear`, `kick` و`ban`، يجب أن يحصل البوت على الصلاحيات المناسبة لتنفيذها.

بعدها انسخ رابط الدعوة وافتحه، ثم اختر السيرفر.

---

# <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="20" align="absmiddle"> تشغيل البوت

بعد تثبيت المكتبات ووضع التوكن، افتح Terminal داخل مجلد المشروع واكتب:

```bash
python bot.py
```

إذا اشتغل بشكل صحيح، ستظهر رسالة في Terminal شبيهة بـ:

```
Logged in as YOUR_BOT | Slash commands synced
```

الآن البوت **Online**.

---

# <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/commands.svg" width="20" align="absmiddle"> كيف أستخدمه في Discord؟

افتح السيرفر الذي أضفت إليه البوت.

اكتب:

```
/
```

ستظهر أوامر البوت.

ابدأ مثلًا بـ:

```
/help
```

ثم جرّب:

```
/ping
```

إذا رد البوت، فكل شيء يعمل.

---

# <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="20" align="absmiddle"> إذا الأوامر لا تظهر

جرّب هذه الأشياء بالترتيب:

### 1. 🔄 أعد تشغيل البوت

أوقفه ثم شغله:

```bash
python bot.py
```

### 2. 🔗 تأكد من دعوة البوت

تأكد أنك استخدمت:

```
bot
applications.commands
```

### 3. <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="20" align="absmiddle"> تأكد من الصلاحيات

أوامر الإدارة تحتاج صلاحيات Discord المناسبة.

### 4. 📁 تأكد من مكان `.env`

يجب أن يكون بجانب `bot.py`:

```
Site-/
├── bot.py
├── .env
└── requirements.txt
```

### 5. <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="20" align="absmiddle"> تأكد من التوكن

يجب أن يكون اسم المتغير بالضبط:

```
DISCORD_TOKEN
```

---

# <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="20" align="absmiddle"> أشهر الأخطاء

### `DISCORD_TOKEN غير موجود في ملف .env`

السبب: البوت لم يجد التوكن.

الحل:

تأكد من وجود:

```
.env
```

وفي داخله:

```env
DISCORD_TOKEN=توكنك
```

---

### `ModuleNotFoundError`

يعني أن مكتبة مطلوبة غير مثبتة.

جرّب:

```bash
pip install -r requirements.txt
```

---

### <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="20" align="absmiddle"> البوت Online لكن أمر الإدارة لا يعمل

تأكد من:

- صلاحيات البوت في السيرفر.
- صلاحيات حسابك.
- ترتيب الـRole الخاص بالبوت إذا كان يتعامل مع أعضاء لديهم رتبة أعلى.

---

# <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/ai.svg" width="20" align="absmiddle"> كيف يعمل البوت من الداخل؟

الفكرة الأساسية:

```
.env
 │
 │ Token
 ▼
bot.py
 │
 │ اتصال Discord
 ▼
Discord API
 │
 ├── /ping
 ├── /server
 ├── /user
 ├── /avatar
 ├── /help
 ├── /clear
 ├── /kick
 ├── /ban
 └── /unban
```

عند تشغيل `bot.py`:

**1. <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="20" align="absmiddle">** يقرأ التوكن من `.env`  
**2. 🔌** يتصل بـ Discord  
**3. 🔄** يعمل مزامنة للأوامر  
**4. <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/commands.svg" width="20" align="absmiddle">** يستقبل أوامر Slash  
**5. <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="20" align="absmiddle">** ينفذ الأمر  
**6. 📩** يرسل النتيجة إلى Discord

---

# <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/python.svg" width="20" align="absmiddle"> هل أحتاج أعرف البرمجة؟

**لا.**

لتشغيل المشروع فقط تحتاج تعرف:

1. تنزيل المشروع.
2. تثبيت Python.
3. تثبيت المكتبات.
4. وضع Bot Token في `.env`.
5. تشغيل:

```bash
python bot.py
```

أما تعديل الأوامر أو إضافة ميزات جديدة، فهذا يحتاج معرفة بسيطة بـ Python، ويمكنك تطويره لاحقًا.

---

# <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="20" align="absmiddle"> أمان مهم جدًا

🚨 **لا تضع Bot Token داخل `bot.py`.**

🚨 **لا تنشر ملف `.env`.**

🚨 **لا تضع التوكن في README.**

🚨 **لا ترسل التوكن في Discord.**

إذا تم تسريب التوكن، قم بتغييره من Discord Developer Portal.

---

## <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="28" align="absmiddle"> للمطور: استخدام المشروع من الآخرين

إذا قام شخص آخر بتشغيل نسخة Site- الخاصة به، يمكنك تفعيل نظام اختياري لمعرفة الاستخدام العام واستقبال الملاحظات.

النظام لا يرسل Discord User ID أو أسماء المستخدمين أو محتوى الرسائل. عند تفعيله، يرسل إحصائيات مجمعة مثل عدد السيرفرات وعدد مرات استخدام الأوامر، بالإضافة إلى الرسائل التي يرسلها المستخدم عبر `/feedback`.

### الإعداد

أضف إلى `.env`:

```env
TELEMETRY_ENABLED=true
TELEMETRY_WEBHOOK_URL=YOUR_DISCORD_WEBHOOK_URL
```

إذا بقي `TELEMETRY_ENABLED=false` أو لم يتم وضع Webhook، فلن يتم إرسال أي Telemetry.

> إذا كنت توزع المشروع على الآخرين، وضّح لهم أن Telemetry اختيارية قبل تفعيلها، ولا تستخدم Webhook خاصًا بك دون إخبارهم.

### ماذا تحصل عليه؟

- عدد السيرفرات التي يعمل فيها البوت وقت التقرير.
- عدد استخدامات الأوامر منذ آخر تقرير.
- مدة تشغيل البوت.
- Feedback يرسله المستخدم عبر `/feedback`.

التقارير الدورية محدودة زمنيًا، ولا يتم جمع User ID أو Server ID ضمن التقرير.

---

## <img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="28" align="absmiddle"> QUICK START

```bash
# 1 — تثبيت المكتبات
pip install -r requirements.txt

# 2 — وضع التوكن داخل .env
DISCORD_TOKEN=YOUR_BOT_TOKEN

# 3 — تشغيل البوت
python bot.py
```

<div align="center">
<img src="https://raw.githubusercontent.com/irisblack374-pixel/Site-/main/assets/icons/site.svg" width="46">
<br><br>
<b>BUILD • TEST • EVOLVE</b>
<br>
Simple Discord Bot · Python · discord.py · 2026
</div>