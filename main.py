import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers import commands, choosing_words
import os

load_dotenv()


async def main():
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher()

    dp.include_router(commands.router)
    dp.include_router(choosing_words.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
