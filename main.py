import asyncio

from aiogram import Bot, Dispatcher
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, FSInputFile, CallbackQuery
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import CommandStart, Command
import aiogram.utils.markdown as fmt
from aiogram.utils.keyboard import InlineKeyboardBuilder
from handlers.language_router import router as language_router

bot = Bot(token='7600812283:AAEfK2lQGELfyzvCucCNAksasBak9a0dA84')
dp = Dispatcher()

# async def send_message(user_id, text):
#     await bot.send_message(chat_id=user_id, text=text)

dp.include_router(language_router)

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
