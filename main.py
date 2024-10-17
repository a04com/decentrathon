import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton,WebAppInfo
from aiogram.filters import CommandStart, Command

bot = Bot(token='7526341893:AAFRdSMm4FtlN_V2-YaGl8MRljKhDd-Tm-o')
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello")

@dp.message(Command('getapp'))
async def get_app(message: Message):
    markup = InlineKeyboardMarkup(
        inline_keyboard = [
            [
                InlineKeyboardButton(
                    text="open",
                    web_app=WebAppInfo(url='https://235a-95-57-246-132.ngrok-free.app')
                )
            ]
        ]
    )

    await message.answer('open', reply_markup=markup)

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
