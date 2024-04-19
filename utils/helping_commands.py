from aiogram.types import BotCommand
from aiogram import Bot


async def setup_bot_commands(bot: Bot):
    bot_commands = [
        BotCommand(command="/joke", description="простой анекдот про штирлица"),
        BotCommand(command="/wordsjoke", description="анекдот с заданными словами"),
        BotCommand(command="/cancel", description="отменить действия")
    ]
    await bot.set_my_commands(bot_commands)