import logging
from main import Anket
from aiogram.dispatcher.router import Router
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.for_questions import *

router = Router()


@router.message(F.text == "/start")
async def cmd_start(message: Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} || {user_full_name}')
    msg_1 = '*Добрый день!*\nМы рады приветствовать вас в канале абитуриентов *Cambridge High School*.'
    msg_2 = 'Мы понимаем, что у вас много вопросов и готовы ответить на все.'
    msg_3 = 'Для того, чтобы мы смогли направить вас к тому специалисту, ' \
            'который сможет помочь вам наилучшим образом, ответьте на несколько вопросов.'
    await message.reply(msg_1, parse_mode="Markdown")
    await message.answer(msg_2, parse_mode="Markdown")
    await message.answer(msg_3, parse_mode="Markdown")
    await message.answer(
        "Нажмите на кнопку _'Заполнить анкету'_",
        reply_markup=start_questions(),
        parse_mode="Markdown"
    )


@router.message(F.text == "Заполнить анкету")
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Введите *имя ребенка*:",
        reply_markup=ReplyKeyboardRemove,
        parse_mode="Markdown"
    )
    await state.set_state(Anket.name)


@router.message(Anket.name)
async def cmd_start(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(
        "Введите *дату рождения ребенка*:",
        reply_markup=ReplyKeyboardRemove,
        parse_mode="Markdown"
    )
    await state.set_state(Anket.date_of_birth)


@router.message(Anket.date_of_birth)
async def cmd_start(message: Message, state: FSMContext):
    await state.update_data(date_of_birth=message.text)
    await message.answer(
        "В каком классе в настоящее время обучается ребенок?",
        reply_markup=ReplyKeyboardRemove,
        parse_mode="Markdown"
    )
    await state.set_state(Anket.grade)


@router.message(Anket.grade)
async def cmd_start(message: Message, state: FSMContext):
    await state.update_data(grade=message.text)
    await message.answer(
        "Укажите место жительства (страна, город):",
        reply_markup=ReplyKeyboardRemove,
        parse_mode="Markdown"
    )
    await state.set_state(Anket.town_and_country)


@router.message(Anket.town_and_country)
async def cmd_start(message: Message, state: FSMContext):
    await state.update_data(town_and_country=message.text)
    await message.answer(
        "Укажите *средний балл ребенка*:",
        reply_markup=ReplyKeyboardRemove,
        parse_mode="Markdown"
    )
    await state.set_state(Anket.average_marks)


@router.message(Anket.average_marks)
async def cmd_start(message: Message, state: FSMContext):
    await state.update_data(average_marks=message.text)
    await message.answer(
        "Укажите *любимый предмет*:",
        reply_markup=ReplyKeyboardRemove,
        parse_mode="Markdown"
    )
    await state.set_state(Anket.best_subj)


@router.message(Anket.best_subj)
async def cmd_start(message: Message, state: FSMContext):
    await state.update_data(best_subj=message.text)
    await message.answer(
        "Укажите *не любимый предмет*:",
        reply_markup=ReplyKeyboardRemove,
        parse_mode="Markdown"
    )
    await state.set_state(Anket.worst_subj)


@router.message(Anket.worst_subj)
async def cmd_start(message: Message, state: FSMContext):
    await state.update_data(worst_subj=message.text)
    await message.answer(
        "Укажите *мотивациЮ к обучению (по 10 бальной шкале)*:",
        reply_markup=ReplyKeyboardRemove,
        parse_mode="Markdown"
    )
    await state.set_state(Anket.motivation)


@router.message(Anket.motivation)
async def cmd_start(message: Message, state: FSMContext):
    await state.update_data(motivation=message.text)
    await message.answer(
        "Укажите *предпочтительный язык обучения*:",
        reply_markup=lang_of_teach(),
        parse_mode="Markdown"
    )
    await state.set_state(Anket.language_of_teach)


@router.message(Anket.language_of_teach)
async def cmd_start(message: Message, state: FSMContext):
    await state.update_data(lang_of_teach=message.text)
    await message.answer(
        "Укажите *предполагаемую форму обучения*:",
        reply_markup=form_of_teach(),
        parse_mode="Markdown"
    )
    await state.set_state(Anket.form_of_teach)


@router.message(Anket.form_of_teach)
async def cmd_start(message: Message, state: FSMContext):
    await state.update_data(form_of_teach=message.text)
    await message.answer(
        "Укажите *ожидания от обучения (образование, психологический комфорт)*:",
        reply_markup=ReplyKeyboardRemove,
        parse_mode="Markdown"
    )
    await state.set_state(Anket.exp_from_teach)


@router.message(Anket.exp_from_teach)
async def cmd_start(message: Message, state: FSMContext):
    await state.update_data(exp_from_teach=message.text)
    await message.answer(
        "Укажите *на какие предметы предполагается сделать основной упор?*:",
        reply_markup=ReplyKeyboardRemove,
        parse_mode="Markdown"
    )
    await state.set_state(Anket.main_subj)


@router.message(Anket.main_subj)
async def cmd_start(message: Message, state: FSMContext):
    await state.update_data(main_subj=message.text)
    await message.answer(
        "Укажите *предпочтительная форма связи (номер телефона, телеграмм)*:",
        reply_markup=ReplyKeyboardRemove,
        parse_mode="Markdown"
    )
    await state.set_state(Anket.type_contact)


@router.message(Anket.type_contact)
async def cmd_start(message: Message, state: FSMContext):
    await state.update_data(type_contact=message.text)
    await state.set_state(Anket.send)
    data = await state.get_data()
    await message.answer(
        "*Проверьте правильность данных*\n" \
        f"Имя ребенка: {data['name']}\n" \
        f"Дата рождения ребенка: {data['date_of_birth']}\n" \
        f"Класс обучения: {data['grade']}\n" \
        f"Место жительства: {data['town_and_country']}\n" \
        f"Средний балл: {data['average_marks']}\n" \
        f"Любимый предмет: {data['best_subj']}\n" \
        f"Не любимый предмет: {data['worst_subj']}\n" \
        f"Мотивация к обучению: {data['motivation']}\n" \
        f"Язык обучения: {data['lang_of_teach']}\n" \
        f"Форма обучения: {data['form_of_teach']}\n" \
        f"Ожидания от обучения: {data['exp_from_teach']}\n" \
        f"Основные предметы: {data['main_subj']}\n" \
        f"Данные для связи с вами: {data['type_contact']}",
        parse_mode="Markdown",
        reply_markup=send()
    )


@router.message(Anket.send, F.text == "Все верно")
async def cmd_start(message: Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(
        "Анкета отправлена, с вами свяжутся в ближайшее время.\n"
        "Спасибо за уделеное время!",
        parse_mode="Markdown",
        reply_markup=ReplyKeyboardRemove
    )
    await state.clear()


@router.message(Anket.send, F.text == "Заполнить заново")
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Введите *имя ребенка*:",
        reply_markup=ReplyKeyboardRemove,
        parse_mode="Markdown"
    )
    await state.set_state(Anket.name)
