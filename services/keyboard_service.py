from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton,
                           WebAppInfo)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def makeInlineOption(options):
    keyboard = InlineKeyboardBuilder()
    for key in options:
        keyboard.add(InlineKeyboardButton(text=key, callback_data=options[key]))
    return keyboard.as_markup()

def makeInlineLink(text, link):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=text, web_app=WebAppInfo(url=link))]
        ]
    )
