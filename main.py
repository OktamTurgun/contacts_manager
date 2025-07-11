import json
import os

DATA_FILE = 'data/contacts.json'


def load_contacts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []


def save_contacts(contacts):
    with open(DATA_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)


def show_contacts(contacts):
    if not contacts:
        print("📭 Kontaktlar yo'q.")
        return
    for idx, contact in enumerate(contacts, 1):
        print(
            f"{idx}. {contact['name']} | {contact['phone']} | {contact['email']}")


def add_contact(contacts):
    name = input("Ism: ")
    phone = input("Telefon: ")
    email = input("Email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("✅ Kontakt qo‘shildi.")


def search_contact(contacts):
    query = input("Qidirilayotgan ism: ").lower()
    found = [c for c in contacts if query in c['name'].lower()]
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


def main():
    contacts = load_contacts()

    while True:
        print("""
📇 Kontaktlar Menejeri
1. Kontaktlarni ko‘rish
2. Kontakt qo‘shish
3. Kontaktni qidirish
4. Kontaktni o‘chirish
5. Chiqish
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
            save_contacts(contacts)
            print("👋 Xayr!")
            break
        else:
            print("❌ Noto‘g‘ri tanlov.")


if __name__ == "__main__":
    main()
