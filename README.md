# 🤖 Site- Discord Bot

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/discord.py-2.x-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="discord.py">
  <img src="https://img.shields.io/github/license/irisblack374-pixel/Site-?style=for-the-badge" alt="License">
</p>

<p align="center">
  <strong>بوت Discord بسيط ومرتب مبني باستخدام Python و discord.py.</strong><br>
  مناسب كبداية لمشروع بوت قابل للتطوير وإضافة أوامر جديدة.
</p>

---

## ✨ ما هو Site-؟

**Site-** هو مشروع بوت Discord بسيط يحتوي على مجموعة أوامر مفيدة للتجربة والتطوير.

الفكرة ببساطة:

```text
👤 المستخدم
   │
   ▼
💬 يكتب الأمر
   │
   ▼
🤖 Site- Bot
   │
   ▼
🐍 Python + discord.py
   │
   ▼
📨 البوت يرسل النتيجة
```

---

## 🧩 الأوامر

| الأمر | الوظيفة |
|---|---|
| `/ping` | 🏓 فحص استجابة البوت |
| `/server` | 🏠 عرض معلومات السيرفر |
| `/user` | 👤 عرض معلومات المستخدم |
| `/avatar` | 🖼️ عرض صورة المستخدم |
| `/help` | 📚 عرض قائمة المساعدة |

### 💡 مثال

```text
/user
      ↓
🤖 Site- يعرض معلومات المستخدم
```

---

## 🛠️ التقنيات

| التقنية | الاستخدام |
|---|---|
| 🐍 Python | لغة البرمجة |
| 💬 discord.py | التعامل مع Discord API |
| 🔐 .env | حفظ التوكن والإعدادات السرية |

---

## 📁 ملفات المشروع

```text
Site-/
│
├── 🤖 bot.py
│   └── الكود الرئيسي للبوت
│
├── 📦 requirements.txt
│   └── مكتبات Python المطلوبة
│
├── 🔐 .env.example
│   └── نموذج لإعدادات البيئة
│
├── 🚫 .gitignore
│   └── ملفات لا يجب رفعها إلى GitHub
│
└── 📖 README.md
    └── شرح المشروع
```

---

## 🚀 التشغيل خطوة بخطوة

### 1️⃣ تثبيت Python

استخدم **Python 3.11 أو أحدث**.

### 2️⃣ تثبيت المكتبات

من داخل مجلد المشروع:

```bash
pip install -r requirements.txt
```

### 3️⃣ إعداد ملف البيئة

انسخ:

```text
.env.example
```

إلى:

```text
.env
```

ثم ضع توكن البوت:

```env
DISCORD_TOKEN=YOUR_BOT_TOKEN
```

### 4️⃣ تشغيل البوت

```bash
python bot.py
```

إذا بدأ البوت بشكل صحيح، سيعمل ويتصل بـ Discord.

---

## 🔐 مهم جدًا — حماية التوكن

**لا ترفع ملف `.env` إلى GitHub.**

توكن البوت مثل كلمة مرور البوت، لذلك لا تشاركه مع أي شخص.

إذا ظهر التوكن في GitHub أو تم نشره بالخطأ، قم بتغييره من **Discord Developer Portal**.

---

## 🧠 كيف تطور المشروع؟

يمكنك لاحقًا إضافة:

- 🛡️ أوامر إدارة
- 🎫 نظام تذاكر
- 🎉 أوامر ترفيهية
- 📊 نظام إحصائيات
- 🎁 نظام نقاط ومكافآت
- ⚙️ إعدادات خاصة بكل سيرفر

---

## 📌 حالة المشروع

```text
🟢 المشروع قابل للتشغيل
🟢 أوامر أساسية موجودة
🟢 جاهز للتطوير
```

---

<p align="center">
  <strong>🤖 Site- • Built with Python & discord.py</strong><br>
  ⭐ إذا أعجبك المشروع، يمكنك عمل Star للمستودع
</p>
