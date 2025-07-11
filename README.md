
# 📇 Contacts Manager

Python asosida yozilgan oddiy, lekin kengaytirilgan kontaktlar boshqaruv dasturi.

---

## ✨ Xususiyatlar
✅ Kontaktlarni ko‘rish  
✅ Kontakt qo‘shish (telefon raqami validatsiyasi bilan)  
✅ Kontaktni qidirish (ism, email yoki telefon bo‘yicha)  
✅ Kontaktni o‘chirish  
✅ Kontaktni yangilash  
✅ Kontaktlarni alfavit bo‘yicha saralash  
✅ Ma’lumotlarni `contacts.json` ga saqlash va yuklash

---

## 🛠️ Texnologiyalar
- Python 3.x
- `json` moduli (ma’lumotlarni saqlash uchun)
- fayllar bilan ishlash
- funksiya, sikl, shart operatorlari
- modulga ajratilgan kod (`helpers.py`)

---

## 🚀 Ishga tushirish

1️⃣ Reponi klonlash:
```bash
git clone https://github.com/OktamTurgun/contacts_manager.git
cd contacts_manager
```

2️⃣ Ishga tushirish:
```bash
python main.py
```

---

## 📂 Papka tuzilishi
```text
contacts-manager/
├── main.py                # Asosiy dastur kodi
├── data/
│   └── contacts.json      # Kontaktlar saqlanadi
├── utils/
│   └── helpers.py         # Yordamchi funksiyalar
├── README.md              # Loyihaning tavsifi
├── .gitignore             # Git sozlamalari
```

---

## 📄 Telefon raqami validatsiyasi
📌 Telefon raqam faqat raqamlar va boshida `+` bo‘lishi mumkin.  
📌 Bo‘sh joylar va `-` belgilar avtomatik olib tashlanadi.

✅ To‘g‘ri:
```text
+998901234567
998901234567
90 123 45 67
90-123-45-67
```

🚫 Noto‘g‘ri:
```text
90abc123
```

---

## 👨‍💻 Muallif
💻 OktamTurgun  
🌐 GitHub: [OktamTurgun](https://github.com/OktamTurgun)

---

## 🔗 Loyiha
📂 Repo: [contacts_manager](https://github.com/OktamTurgun/contacts_manager)

---

## 📜 Litsenziya
[MIT](LICENSE)