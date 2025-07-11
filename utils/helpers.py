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


def validate_phone(phone):
    phone = phone.replace(" ", "").replace("-", "")

    if phone.startswith('+'):
        phone = phone[1:]

    if not phone.isdigit():
        print("🚫 Telefon raqami noto‘g‘ri: faqat raqamlar va boshida + bo‘lishi mumkin.")
        return False
    return True


def sort_contacts(contacts):
    return sorted(contacts, key=lambda c: c['name'].lower())
