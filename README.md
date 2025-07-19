
# 📇 Contacts Manager

Python asosida yozilgan oddiy, lekin kengaytirilgan kontaktlar boshqaruv dasturi. Bu dastur kontaktlarni saqlash, qidirish, yangilash va boshqarish imkoniyatlarini taqdim etadi.

---

## ✨ Xususiyatlar

### 🔍 Asosiy funksiyalar
- ✅ **Kontaktlarni ko'rish** - barcha kontaktlarni ro'yxat ko'rinishida ko'rsatish
- ✅ **Kontakt qo'shish** - yangi kontakt qo'shish (telefon raqami validatsiyasi bilan)
- ✅ **Kontaktni qidirish** - ism, email yoki telefon bo'yicha qidirish
- ✅ **Kontaktni o'chirish** - tanlangan kontaktni o'chirish
- ✅ **Kontaktni yangilash** - mavjud kontakt ma'lumotlarini tahrirlash
- ✅ **Kontaktlarni saralash** - alfavit bo'yicha saralash
- ✅ **Ma'lumotlarni saqlash** - `contacts.json` faylida avtomatik saqlash

### 🛡️ Xavfsizlik va validatsiya
- 📱 **Telefon raqami validatsiyasi** - faqat raqamlar va + belgisi ruxsat etiladi
- 💾 **Avtomatik saqlash** - har bir o'zgarish avtomatik saqlanadi
- 🔄 **Xatolarni boshqarish** - noto'g'ri ma'lumotlar kiritilganda ogohlantirish

---

## 🛠️ Texnologiyalar

- **Python 3.x** - asosiy dasturlash tili
- **JSON** - ma'lumotlarni saqlash uchun
- **OS moduli** - fayllar bilan ishlash
- **Modullar** - kodni tashkil qilish uchun (`utils/helpers.py`)

---

## 🚀 O'rnatish va ishga tushirish

### 1️⃣ Loyihani yuklab olish
```bash
git clone https://github.com/OktamTurgun/contacts_manager.git
cd contacts_manager
```

### 2️⃣ Dasturni ishga tushirish
```bash
python main.py
```

### 3️⃣ Talablar
- Python 3.6 yoki undan yuqori versiya
- Standart Python kutubxonalari (qo'shimcha o'rnatish talab qilinmaydi)

---

## 📂 Loyiha tuzilishi

```
contacts_manager/
├── 📄 main.py              # Asosiy dastur kodi
├── 📁 data/
│   └── 📄 contacts.json    # Kontaktlar ma'lumotlari
├── 📁 utils/
│   └── 📄 helpers.py       # Yordamchi funksiyalar
├── 📄 README.md            # Loyiha tavsifi
├── 📄 LICENSE              # Litsenziya fayli
└── 📄 .gitignore           # Git sozlamalari
```

---

## 📱 Foydalanish bo'yicha ko'rsatmalar

### Kontakt qo'shish
1. Dastur menyusida `2` ni tanlang
2. Ismni kiriting
3. Telefon raqamini kiriting (validatsiya avtomatik amalga oshiriladi)
4. Email manzilini kiriting

### Kontaktni qidirish
1. Dastur menyusida `3` ni tanlang
2. Qidirilayotgan qiymatni kiriting (ism, email yoki telefon)
3. Natijalar ko'rsatiladi

### Kontaktni yangilash
1. Dastur menyusida `5` ni tanlang
2. Yangilamoqchi bo'lgan kontakt raqamini tanlang
3. Yangi ma'lumotlarni kiriting (bo'sh qoldirilsa eskisi saqlanadi)

---

## 📄 Telefon raqami validatsiyasi

### ✅ Qabul qilinadigan formatlar
```text
+998901234567    # + bilan boshlanadi
998901234567     # + siz
90 123 45 67     # bo'sh joylar bilan
90-123-45-67     # chiziqcha bilan
```

### ❌ Qabul qilinmaydigan formatlar
```text
90abc123         # harflar bilan
90@123#456       # maxsus belgilar bilan
```

### 🔧 Validatsiya qoidalari
- Faqat raqamlar va `+` belgisi ruxsat etiladi
- Bo'sh joylar va `-` belgilar avtomatik olib tashlanadi
- `+` belgisi faqat boshida bo'lishi mumkin

---

## 🎯 Dastur xususiyatlari

### 💡 Interfeys
- 🎨 **Emoji bilan boyitilgan** - foydalanuvchi uchun qulay
- 📋 **Aniq menyu** - barcha funksiyalar raqam bilan belgilangan
- 🔄 **Sikl** - dastur to'xtamasdan ishlaydi

### 💾 Ma'lumotlarni saqlash
- **JSON format** - o'qish va tahrirlash uchun qulay
- **Avtomatik saqlash** - har bir o'zgarish darhol saqlanadi
- **Xatolarni boshqarish** - fayl mavjud emas bo'lsa yangi yaratiladi

---

## 🧪 Sinov ma'lumotlari

Dasturda allaqachon 4 ta namuna kontakt mavjud:
- **Ahmad** - +998977564321
- **Botir** - 998990155433  
- **Olim** - +998988789889
- **Vali** - +998905678944

---

## 🔧 Rivojlantirish

### Loyihani kengaytirish uchun tavsiyalar:
- 📧 Email validatsiyasi qo'shish
- 📱 Qo'shimcha telefon formatlari qo'llab-quvvatlash
- 🗂️ Kategoriyalar bilan kontaktlarni tashkil qilish
- 📤 CSV/Excel formatida eksport qilish
- 🔍 Kengaytirilgan qidiruv funksiyalari

---

## 👨‍💻 Muallif

**💻 OktamTurgun**  
🌐 **GitHub**: [OktamTurgun](https://github.com/OktamTurgun)  
📧 **Email**: [GitHub profildan ko'ring](https://github.com/OktamTurgun)

---

## 🔗 Loyiha havolalari

📂 **Repository**: [contacts_manager](https://github.com/OktamTurgun/contacts_manager)  
📄 **Litsenziya**: [MIT](LICENSE)

---

## 🤝 Hissa qo'shish

Loyihani yaxshilash uchun hissa qo'shmoqchimisiz?

1. 🍴 Fork qiling
2. 🌿 Yangi branch yarating (`git checkout -b feature/yangi-xususiyat`)
3. 💾 O'zgarishlarni commit qiling (`git commit -am 'Yangi xususiyat qo'shildi'`)
4. 📤 Branch-ni push qiling (`git push origin feature/yangi-xususiyat`)
5. 🔄 Pull Request yarating

---

## 📜 Litsenziya

Bu loyiha [MIT litsenziyasi](LICENSE) ostida tarqatiladi.

---

## ⭐ Yulduzcha bering

Agar bu loyiha sizga foydali bo'lsa, ⭐ yulduzcha bering va do'stlaringiz bilan ulashing!

---

*📝 Oxirgi yangilanish: 2024-yil*