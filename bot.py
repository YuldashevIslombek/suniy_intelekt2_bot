import asyncio
import logging
from http.client import responses
from os import getenv

from aiogram.enums import ParseMode
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.client.session.aiohttp import AiohttpSession
from deepsek import generate_response

load_dotenv()
TOKEN = getenv("BOT_TOKEN")
AI_TOKEN = getenv("AI_TOKEN")
session = AiohttpSession(proxy="http://proxy.server:3128")
dp = Dispatcher()


# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
        await message.answer("Assalomu alaykum! Botga xush kelibsiz. Sizga qanday yordam bera olaman!")

@dp.message()
async def echo(message: Message) -> None:
    response = await generate_response(message.text, AI_TOKEN)
    await message.answer(f"{response}", parse_mode="Markdown")


# Run the bot
async def main() -> None:
    # bot = Bot(token=TOKEN)
    bot = Bot(token=TOKEN, session=session)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Starting bot...")
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    asyncio.run(main())

