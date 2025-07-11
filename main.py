from utils.helpers import (
    load_contacts,
    save_contacts,
    show_contacts,
    validate_phone,
    sort_contacts
)


def add_contact(contacts):
    name = input("Ism: ")
    phone = input("Telefon: ")
    if not validate_phone(phone):
        return
    email = input("Email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("✅ Kontakt qo‘shildi.")


def search_contact(contacts):
    query = input("Qidirilayotgan qiymat (ism/email/telefon): ").lower()
    found = [
        c for c in contacts
        if query in c['name'].lower() or
        query in c['email'].lower() or
        query in c['phone']
    ]
    if found:
        show_contacts(found)
    else:
        print("🚫 Kontakt topilmadi.")


def delete_contact(contacts):
    show_contacts(contacts)
    idx = int(input("O‘chiriladigan kontakt raqamini kiriting: ")) - 1
    if 0 <= idx < len(contacts):
        removed = contacts.pop(idx)
        print(f"🗑️ {removed['name']} o‘chirildi.")
    else:
        print("❌ Noto‘g‘ri raqam.")


def update_contact(contacts):
    show_contacts(contacts)
    idx = int(input("Yangilamoqchi bo‘lgan kontakt raqamini kiriting: ")) - 1
    if 0 <= idx < len(contacts):
        contact = contacts[idx]
        print(f"✍️ {contact['name']} ni yangilayapmiz.")
        name = input(f"Yangi ism [{contact['name']}]: ") or contact['name']
        phone = input(
            f"Yangi telefon [{contact['phone']}]: ") or contact['phone']
        if not validate_phone(phone):
            return
        email = input(
            f"Yangi email [{contact['email']}]: ") or contact['email']
        contact.update({"name": name, "phone": phone, "email": email})
        print("♻️ Kontakt yangilandi.")
    else:
        print("❌ Noto‘g‘ri raqam.")


def main():
    contacts = load_contacts()

    while True:
        print("""
📇 Kontaktlar Menejeri
1. Kontaktlarni ko‘rish
2. Kontakt qo‘shish
3. Kontaktni qidirish
4. Kontaktni o‘chirish
5. Kontaktni yangilash
6. Kontaktlarni saralash
7. Chiqish
""")
        choice = input("Tanlang: ")

        if choice == '1':
            show_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
            save_contacts(contacts)
        elif choice == '5':
            update_contact(contacts)
            save_contacts(contacts)
        elif choice == '6':
            contacts = sort_contacts(contacts)
            show_contacts(contacts)
        elif choice == '7':
            save_contacts(contacts)
            print("👋 Xayr!")
            break
        else:
            print("❌ Noto‘g‘ri tanlov.")


if __name__ == "__main__":
    main()
