# <img src="https://cdn.simpleicons.org/discord/5865F2" width="30" alt="Discord"> Site-

<p align="center">
  <strong>بوت Discord بسيط باستخدام Python و discord.py</strong><br>
  شرح من الصفر حتى التشغيل — حتى لو ما عندك خبرة بالبرمجة
</p>

<p align="center">
  <img src="https://cdn.simpleicons.org/python/3776AB" width="28" alt="Python">
  &nbsp;
  <img src="https://cdn.simpleicons.org/discord/5865F2" width="28" alt="Discord">
  &nbsp;
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white" alt="Python 3.11+">
  <img src="https://img.shields.io/badge/discord.py-2.x-5865F2?logo=discord&logoColor=white" alt="discord.py 2.x">
</p>

---

## <img src="https://cdn.simpleicons.org/github/181717" width="22" alt="About"> ما هو Site-؟

ببساطة:

**Site- هو برنامج يعمل داخل Discord.**

أنت تكتب أمرًا مثل `/ping`، والبوت يستقبل الأمر ثم ينفذ المطلوب ويرسل لك النتيجة.

مثال:

```
أنت
 ↓
/ping
 ↓
Site-
 ↓
🏓 البوت يرد
```

لا تحتاج أن تعرف البرمجة حتى تفهم فكرة المشروع أو تتبع خطوات تشغيله.

---

## <img src="https://cdn.simpleicons.org/rocket/EA4B71" width="22" alt="How"> كيف يعمل البوت؟

هناك 3 أشياء أساسية:

### 1. Discord
هو المكان الذي يوجد فيه البوت والسيرفر.

### 2. Python
هي لغة البرمجة التي كُتب بها البوت.

يمكن اعتبار Python هي **اللغة التي يفهم بها الكمبيوتر تعليمات البوت**.

### 3. discord.py
هذه مكتبة تساعد Python على التواصل مع Discord.

بشكل مبسط:

```
Discord
   ↕
discord.py
   ↕
Python
   ↕
bot.py
```

---

## <img src="https://cdn.simpleicons.org/discord/5865F2" width="22" alt="Commands"> ماذا يفعل كل أمر؟

### `/ping`

يختبر هل البوت يستجيب أم لا.

**مثال:**

```
/ping
↓
🏓 البوت يرد
```

---

### `/server`

يعرض معلومات عن السيرفر الذي تستخدم فيه الأمر.

---

### `/user`

يعرض معلومات عن المستخدم.

---

### `/avatar`

يعرض صورة المستخدم.

---

### `/help`

يعرض قائمة الأوامر الموجودة في البوت.

---

## <img src="https://cdn.simpleicons.org/python/3776AB" width="22" alt="Tech"> ما هي الأشياء المستخدمة؟

### 🐍 Python

لغة البرمجة المستخدمة لكتابة البوت.

### Discord.py

مكتبة تجعل Python قادرة على التعامل مع Discord.

### `.env`

ملف خاص لحفظ المعلومات السرية مثل **Bot Token**.

> لا تشارك التوكن مع أي شخص.

---

## <img src="https://cdn.simpleicons.org/files/4A90E2" width="22" alt="Files"> شرح ملفات المشروع

```
Site-/
│
├── bot.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

### `bot.py`

⭐ **أهم ملف في المشروع.**

يحتوي على كود البوت والأوامر وطريقة عمله.

---

### `requirements.txt`

يخبر Python بالمكتبات التي يحتاجها المشروع.

بدل تثبيت كل مكتبة واحدة واحدة، تستخدم:

```bash
pip install -r requirements.txt
```

---

### `.env.example`

ملف مثال يوضح الإعدادات التي يحتاجها المشروع.

منه تنشئ ملف:

```
.env
```

---

### `.gitignore`

يخبر GitHub عن الملفات التي لا نريد رفعها للمستودع.

ومن أهم الأشياء التي يجب ألا تظهر على GitHub:

```
.env
```

---

### `README.md`

هذا الملف الذي تقرأه الآن.

وظيفته شرح المشروع وطريقة تشغيله.

---

## <img src="https://cdn.simpleicons.org/rocket/EA4B71" width="22" alt="Install"> طريقة تشغيل البوت من الصفر

### قبل البداية

ستحتاج إلى:

- جهاز كمبيوتر
- Python 3.11 أو أحدث
- حساب Discord
- Bot Token
- ملفات المشروع

> إذا كنت تستخدم الجوال فقط، فالتشغيل يعتمد على منصة استضافة تدعم Python؛ وجود الملفات وحده لا يشغل البوت.

---

### الخطوة 1 — تثبيت Python

ثبّت **Python 3.11 أو أحدث** على الكمبيوتر.

بعد التثبيت، افتح Terminal أو CMD واكتب:

```bash
python --version
```

إذا ظهر رقم مثل:

```
Python 3.11.x
```

فهذا يعني أن Python مثبت بشكل صحيح.

---

### الخطوة 2 — افتح مجلد المشروع

ضع ملفات Site- داخل مجلد واحد.

يجب أن ترى شيئًا قريبًا من:

```
Site-/
├── bot.py
├── requirements.txt
├── .env.example
└── README.md
```

---

### الخطوة 3 — تثبيت المكتبات

افتح Terminal داخل مجلد المشروع واكتب:

```bash
pip install -r requirements.txt
```

هذا الأمر يعني:

**"ثبّت كل المكتبات التي يحتاجها البوت."**

انتظر حتى ينتهي التثبيت.

---

### الخطوة 4 — إنشاء ملف .env

خذ:

```
.env.example
```

وانسخه أو أعد تسميته إلى:

```
.env
```

ثم افتحه.

ضع داخله توكن البوت بالشكل التالي:

```env
DISCORD_TOKEN=YOUR_BOT_TOKEN
```

استبدل:

```
YOUR_BOT_TOKEN
```

بالتوكن الحقيقي الخاص بالبوت.

---

## <img src="https://cdn.simpleicons.org/discord/5865F2" width="22" alt="Bot"> من أين أحصل على Bot Token؟

من **Discord Developer Portal**.

بشكل عام:

```
Discord Developer Portal
        ↓
اختر تطبيق البوت
        ↓
Bot
        ↓
Token
```

⚠️ التوكن **سري جدًا**.

لا ترسله في:

- GitHub
- Discord
- Screenshots
- رسائل عامة
- أي مكان يراه الآخرون

إذا انكشف التوكن، قم بتغييره فورًا من إعدادات البوت.

---

## <img src="https://cdn.simpleicons.org/terminal/4D4D4D" width="22" alt="Start"> الخطوة 5 — تشغيل البوت

بعد تجهيز كل شيء، اكتب:

```bash
python bot.py
```

إذا لم تظهر مشكلة وبدأ البوت بالاتصال بـ Discord، فالمشروع يعمل.

---

## <img src="https://cdn.simpleicons.org/letsencrypt/003A70" width="22" alt="Security"> 🔐 أخطاء شائعة

### المشكلة: `python` غير معروف

قد يكون Python غير مثبت أو غير مضاف إلى PATH.

### المشكلة: المكتبة غير موجودة

جرّب:

```bash
pip install -r requirements.txt
```

### المشكلة: البوت لا يعمل

تأكد من:

1. التوكن صحيح.
2. ملف `.env` موجود.
3. اسم المتغير هو:

```
DISCORD_TOKEN
```

4. شغّلت:

```bash
python bot.py
```

---

## <img src="https://cdn.simpleicons.org/github/181717" width="22" alt="GitHub"> GitHub للمبتدئين

إذا كنت لا تعرف GitHub، فببساطة:

**Repository / مستودع** = مكان يحفظ ملفات المشروع.

**README** = صفحة شرح المشروع.

**Commit** = حفظ تغيير جديد في المشروع.

**Clone** = تنزيل نسخة من المشروع على جهازك.

---

## <img src="https://cdn.simpleicons.org/githubactions/2088FF" width="22" alt="Future"> ماذا يمكن إضافة للمشروع؟

يمكن تطوير Site- لاحقًا بإضافة:

- أوامر إدارة السيرفر
- نظام تذاكر
- أوامر ترفيهية
- نظام نقاط
- إحصائيات
- إعدادات خاصة لكل سيرفر
- سجلات Logs
- نظام ترحيب للأعضاء

---

## <img src="https://cdn.simpleicons.org/checkmarx/54B848" width="22" alt="Status"> حالة المشروع

**🟢 جاهز للتشغيل والتطوير**

هذا المشروع مناسب أيضًا كقاعدة تتعلم منها طريقة بناء بوت Discord.

---

## <img src="https://cdn.simpleicons.org/github/181717" width="22" alt="Contribution"> المساهمة

إذا كنت مطورًا وتريد تطوير المشروع:

1. انسخ المشروع.
2. عدّل الكود.
3. اختبر التعديلات.
4. يمكنك اقتراح تحسينات للمشروع.

---

<p align="center">
  <img src="https://cdn.simpleicons.org/discord/5865F2" width="24" alt="Discord">
  <strong> Site-</strong><br>
  Built with Python & discord.py
</p>
