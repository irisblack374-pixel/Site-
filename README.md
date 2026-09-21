# <img src="https://cdn.simpleicons.org/discord/5865F2" width="30" alt="Discord"> Site-

<p align="center">
  <strong>بوت Discord بسيط باستخدام Python و discord.py</strong><br>
  شرح من الصفر حتى التشغيل — حتى لو ما عندك خبرة بالبرمجة
</p>

<p align="center">
  <img src="https://cdn.simpleicons.org/python/3776AB" width="26" alt="Python">
  &nbsp;
  <img src="https://cdn.simpleicons.org/discord/5865F2" width="26" alt="Discord">
  &nbsp;
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white" alt="Python 3.11+">
  <img src="https://img.shields.io/badge/discord.py-2.x-5865F2?logo=discord&logoColor=white" alt="discord.py 2.x">
</p>

---

## <img src="https://cdn.simpleicons.org/github/181717" width="21" alt="About"> ما هو Site-؟

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
البوت يرد
```

لا تحتاج أن تعرف البرمجة حتى تفهم فكرة المشروع أو تتبع خطوات تشغيله.

---

## <img src="https://cdn.simpleicons.org/discord/5865F2" width="21" alt="How"> كيف يعمل البوت؟

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

## <img src="https://cdn.simpleicons.org/discord/5865F2" width="21" alt="Commands"> ماذا يفعل كل أمر؟

### <img src="https://cdn.simpleicons.org/discord/5865F2" width="18" alt="Ping"> `/ping`

يختبر هل البوت يستجيب أم لا.

### <img src="https://cdn.simpleicons.org/serverless/FD5750" width="18" alt="Server"> `/server`

يعرض معلومات عن السيرفر.

### <img src="https://cdn.simpleicons.org/github/181717" width="18" alt="User"> `/user`

يعرض معلومات عن المستخدم.

### <img src="https://cdn.simpleicons.org/googlephotos/4285F4" width="18" alt="Avatar"> `/avatar`

يعرض صورة المستخدم.

### <img src="https://cdn.simpleicons.org/readthedocs/8CA1AF" width="18" alt="Help"> `/help`

يعرض قائمة الأوامر الموجودة في البوت.

---

## <img src="https://cdn.simpleicons.org/python/3776AB" width="21" alt="Tech"> ما هي الأشياء المستخدمة؟

### <img src="https://cdn.simpleicons.org/python/3776AB" width="18" alt="Python"> Python

لغة البرمجة المستخدمة لكتابة البوت.

### <img src="https://cdn.simpleicons.org/discord/5865F2" width="18" alt="discord.py"> discord.py

مكتبة تجعل Python قادرة على التعامل مع Discord.

### <img src="https://cdn.simpleicons.org/dotenv/ECD53F" width="18" alt=".env"> `.env`

ملف خاص لحفظ المعلومات السرية مثل **Bot Token**.

> لا تشارك التوكن مع أي شخص.

---

## <img src="https://cdn.simpleicons.org/files/4A90E2" width="21" alt="Files"> شرح ملفات المشروع

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

**أهم ملف في المشروع.**

يحتوي على كود البوت والأوامر وطريقة عمله.

### `requirements.txt`

يخبر Python بالمكتبات التي يحتاجها المشروع.

### `.env.example`

ملف مثال يوضح الإعدادات التي يحتاجها المشروع.

### `.gitignore`

يخبر GitHub عن الملفات التي لا نريد رفعها، مثل `.env`.

### `README.md`

صفحة شرح المشروع التي تقرأها الآن.

---

## <img src="https://cdn.simpleicons.org/python/3776AB" width="21" alt="Install"> طريقة تشغيل البوت من الصفر

### قبل البداية

ستحتاج إلى:

- جهاز كمبيوتر
- Python 3.11 أو أحدث
- حساب Discord
- Bot Token
- ملفات المشروع

> إذا كنت تستخدم الجوال فقط، فالتشغيل يحتاج إلى منصة استضافة تدعم Python.

### 1 — تثبيت Python

بعد تثبيت Python، افتح Terminal أو CMD واكتب:

```bash
python --version
```

إذا ظهر مثل:

```
Python 3.11.x
```

فـ Python مثبت بشكل صحيح.

### 2 — افتح مجلد المشروع

ضع ملفات Site- داخل مجلد واحد.

### 3 — تثبيت المكتبات

داخل مجلد المشروع اكتب:

```bash
pip install -r requirements.txt
```

هذا يعني: **ثبّت المكتبات التي يحتاجها البوت.**

### 4 — إنشاء ملف `.env`

انسخ `.env.example` إلى ملف جديد باسم:

```
.env
```

ثم ضع داخله:

```env
DISCORD_TOKEN=YOUR_BOT_TOKEN
```

واستبدل `YOUR_BOT_TOKEN` بالتوكن الحقيقي.

### 5 — تشغيل البوت

```bash
python bot.py
```

إذا بدأ البوت بالاتصال بـ Discord، فالمشروع يعمل.

---

## <img src="https://cdn.simpleicons.org/discord/5865F2" width="21" alt="Bot"> Bot Token

تحصل عليه من **Discord Developer Portal**:

```
Discord Developer Portal
        ↓
التطبيق
        ↓
Bot
        ↓
Token
```

التوكن مثل **كلمة مرور البوت**.

لا تضعه في GitHub أو Discord أو أي مكان عام.

إذا انكشف، قم بتغييره فورًا من إعدادات البوت.

---

## <img src="https://cdn.simpleicons.org/letsencrypt/003A70" width="21" alt="Security"> أخطاء شائعة

### `python` غير معروف

تأكد من تثبيت Python وإضافته إلى PATH.

### مكتبة غير موجودة

شغّل:

```bash
pip install -r requirements.txt
```

### البوت لا يعمل

تأكد من:

1. التوكن صحيح.
2. ملف `.env` موجود.
3. اسم المتغير هو `DISCORD_TOKEN`.
4. شغّلت `python bot.py`.

---

## <img src="https://cdn.simpleicons.org/github/181717" width="21" alt="GitHub"> GitHub للمبتدئين

**Repository** = مكان يحفظ ملفات المشروع.

**README** = صفحة شرح المشروع.

**Commit** = حفظ تغيير جديد.

**Clone** = تنزيل نسخة من المشروع على جهازك.

---

## <img src="https://cdn.simpleicons.org/githubactions/2088FF" width="21" alt="Future"> ماذا يمكن إضافة للمشروع؟

يمكن تطوير Site- بإضافة:

- أوامر إدارة السيرفر
- نظام تذاكر
- أوامر ترفيهية
- نظام نقاط
- إحصائيات
- إعدادات خاصة لكل سيرفر
- سجلات Logs
- نظام ترحيب

---

## <img src="https://cdn.simpleicons.org/checkmarx/54B848" width="21" alt="Status"> حالة المشروع

**جاهز للتشغيل والتطوير.**

---

## <img src="https://cdn.simpleicons.org/github/181717" width="21" alt="Copyright"> حقوق المشروع

<p align="center">
  <strong>© 2026 irisblack374-pixel</strong><br>
  جميع الحقوق محفوظة.
</p>

يُمنع نسخ المشروع أو إعادة نشره أو نسبه إلى شخص آخر دون إذن صاحب المشروع.

<a href="https://github.com/irisblack374-pixel">
  <img src="https://img.shields.io/badge/GitHub-irisblack374--pixel-181717?logo=github&logoColor=white" alt="GitHub">
</a>

---

<p align="center">
  <img src="https://cdn.simpleicons.org/discord/5865F2" width="23" alt="Discord">
  <strong> Site-</strong><br>
  Built with Python & discord.py
</p>
