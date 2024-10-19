from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.enums.parse_mode import ParseMode
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import CommandStart
import aiogram.utils.markdown as fmt

from decentrathon.handlers.keyboards import languageChoiceKeyboard

class Language(StatesGroup):
    language = State()

router = Router()

@router.message(CommandStart())
async def language_choosing_state(message: Message, state: FSMContext):
    await state.set_state(Language.language)

    # keyboard_builder = InlineKeyboardBuilder()
    # keyboard_builder.button(text="kz", callback_data="kz")
    # keyboard_builder.button(text="en", callback_data="en")
    # keyboard_builder.button(text="ru", callback_data="ru")

    await message.answer("Choose your language:", reply_markup=languageChoiceKeyboard())

@router.callback_query(Language.language, F.data)
async def chosen_language(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(callback.data)
    await state.update_data(language=callback.data)
    language_data = await state.get_data()
    userName = callback.from_user.first_name
    startPhoto = FSInputFile(r"files/logo.jpg")

    if language_data["language"] == "kz":
        text = "Hirely ашу"
    elif language_data["language"] == "en":
        text = "open Hirely"
    elif language_data["language"] == "ru":
        text = "открыть Hirely"

    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=text, web_app=WebAppInfo(url='https://example.com'))]
        ]
    )

    if language_data["language"] == "kz":
        await callback.message.answer_photo(photo=startPhoto, caption=f'''
        🌟 Сәлем {fmt.hbold(userName)} және <b>Hirely!</b> сайтына қош келдіңіз! Мұнда сіз <b>өзіңізге сәйкес келетін жұмыстарды немесе қызметкерлерді оңай таба аласыз.</b> Жаңа мүмкіндіктерге саяхатты бірге бастайық! 🚀
        ''', reply_markup=markup, parse_mode=ParseMode.HTML)

    elif language_data["language"] == "en":
        await callback.message.answer_photo(photo=startPhoto, caption=f'''
    🌟 Hi {fmt.hbold(userName)} and welcome to <b>Hirely!</b> Here you can easily find a job or employees <b>that are right for you.</b> Let's start this journey to new opportunities together! 🚀
    ''', reply_markup=markup, parse_mode=ParseMode.HTML)

    elif language_data["language"] == "ru":
        await callback.message.answer_photo(photo=startPhoto, caption=f'''
    🌟 Привет {fmt.hbold(userName)} и добро пожаловать в <b>Hirely!</b> Здесь ты сможешь легко найти работу или сотрудников <b>которые подойдут именно тебе.</b> Давай начнём это путешествие к новым возможностям вместе! 🚀
    ''', reply_markup=markup, parse_mode=ParseMode.HTML)

    await state.clear()
