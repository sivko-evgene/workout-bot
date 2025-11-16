# main.py
import time
import os

print("Python version check...")

# Проверяем переменные окружения
bot_token = os.getenv('BOT_TOKEN')
supabase_url = os.getenv('SUPABASE_URL')

print("✅ Environment check:")
print(f"BOT_TOKEN: {'✅ Set' if bot_token else '❌ Missing'}")
print(f"SUPABASE_URL: {'✅ Set' if supabase_url else '❌ Missing'}")

print("🚀 Application is running...")

# Бесконечный цикл чтобы приложение не закрывалось
while True:
    print("🤖 Bot service is alive...")
    time.sleep(60)  # Ждет 60 секунд между сообщениями
