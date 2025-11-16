import os
import asyncio
from telegram.ext import Application

async def main():
    bot_token = os.getenv('BOT_TOKEN')
    if not bot_token:
        print("❌ BOT_TOKEN not set")
        return
    
    application = Application.builder().token(bot_token).build()
    print("✅ Bot initialized, starting polling...")
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
