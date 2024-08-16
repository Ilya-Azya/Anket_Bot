from aiogram import types
from aiogram.filters import callback_data
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def start_main() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(
        text="Начать работу",
        callback_data="/start"
    ))
    return kb.as_markup()


def get_yes_no_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Да")
    kb.button(text="Нет")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True, input_field_placeholder="Выберите ответ")


def start_questions() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Заполнить анкету")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True, input_field_placeholder="Выберите ответ")


def lang_of_teach() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Русский")
    kb.button(text="Украинский")
    kb.button(text="Белорусский")
    kb.adjust(3)
    return kb.as_markup(resize_keyboard=True, input_field_placeholder="Выберите ответ")


def form_of_teach() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Очная")
    kb.button(text="Онлайн")
    kb.button(text="HomeSchool")
    kb.adjust(3)
    return kb.as_markup(resize_keyboard=True, input_field_placeholder="Выберите ответ")


def send() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Все верно")
    kb.button(text="Заполнить заново")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True, input_field_placeholder="Выберите ответ")
