import requests
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def send_to_telegram(name, email, message):
    """
    Отправляет сообщение из контактной формы в Telegram
    """
    bot_token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID
    
    if not bot_token or not chat_id:
        logger.warning("Telegram bot token or chat id not set")
        return False
    
    # Форматируем сообщение
    text = f"📨 *Новое сообщение из портфолио*\n\n"
    text += f"👤 *Имя:* {name}\n"
    text += f"📧 *Email:* `{email}`\n"
    text += f"💬 *Сообщение:*\n{message}\n"
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    data = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'Markdown',
        'disable_web_page_preview': True,
    }
    
    try:
        response = requests.post(url, json=data, timeout=10)
        response.raise_for_status()
        logger.info(f"Message sent to Telegram successfully")
        return True
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to send message to Telegram: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return False