import telebot
from app.config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def send_alert(message):
    try:
        bot.send_message(TELEGRAM_CHAT_ID, message, parse_mode='Markdown')
    except Exception as e:
        print(f"Telegram Error: {e}")

# Example usage:
# send_alert('*Bullish Triangle* on LINK
Entry: 8.23
Stop: 7.91
Target: 9.15
Timeframe: 5min
Sentiment: Bullish')
