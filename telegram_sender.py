import requests
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def send_telegram_message(name, email, message):
    """Отправляет сообщение в Telegram"""
    
    # Получаем настройки
    bot_token = getattr(settings, 'TELEGRAM_BOT_TOKEN', None)
    chat_id = getattr(settings, 'TELEGRAM_CHAT_ID', None)
    
    # Проверяем настройки
    if not bot_token or not chat_id:
        print("⚠️ Telegram bot token or chat id not set in settings.py")
        return False
    
    # Форматируем сообщение
    text = f"""
    📨 НОВОЕ СООБЩЕНИЕ ИЗ ПОРТФОЛИО
    
    👤 Имя: {name}
    📧 Email: {email}
    
    💬 Сообщение:
    {message}
    
    ---
    ✅ Сообщение сохранено в базе данных
    """
    
    # URL для отправки
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    # Параметры запроса
    params = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'HTML'
    }
    
    try:
        # Отправляем запрос
        response = requests.post(url, json=params, timeout=10)
        
        # Проверяем ответ
        if response.status_code == 200:
            print("✅ Сообщение отправлено в Telegram")
            return True
        else:
            print(f"❌ Ошибка Telegram API: {response.status_code}")
            print(f"Ответ: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка при отправке в Telegram: {e}")
        return False