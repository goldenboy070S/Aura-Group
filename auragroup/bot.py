import requests
from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")
CHAT_ID = getenv("CHAT_ID")

def send_message(name, email, phone_number, description):
    text = f"📥 Yangi xabar:\n\n👤 Ism: {name}\n📧 Email: {email}\n📱 Tel: {phone_number}\n📝 Xabar:\n{description}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': text
    }

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        print("✅ Xabar Telegramga yuborildi")
    except Exception as e:
        print("❌ Xabar yuborishda xatolik:", e)

def send_service_request(company, phone, service, contact_name, description):
    API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    text = (
        f"🆕 Yangi xizmat so‘rovi:\n\n"
        f"🏢 Kompaniya: {company}\n"
        f"📞 Telefon: {phone}\n"
        f"🛠 Xizmat turi: {service}\n"
        f"👤 Ismi: {contact_name}\n"
        f"📝 Tavsif: {description}"
    )
    data = {
        'chat_id': CHAT_ID,
        'text': text,
        'parse_mode': 'HTML',
    }
    try:
        resp = requests.post(API_URL, data=data)
        resp.raise_for_status()
        print("✅ Telegramga yuborildi")
    except requests.RequestException as e:
        print(f"❌ Xatolik: {e}")
