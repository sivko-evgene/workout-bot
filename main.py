# main.py
import os
import asyncio
from telegram.ext import Application

def main():
    bot_token = os.getenv('BOT_TOKEN')
    if not bot_token:
        print("❌ BOT_TOKEN not set")
        return
    
    application = Application.builder().token(bot_token).build()
    print("✅ Bot initialized, starting polling...")
    
    # Простой запуск для Render
    application.run_polling()

if __name__ == "__main__":
    main()
