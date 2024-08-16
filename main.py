import logging
import asyncio
import configparser
# import pip
# pip.main(['install','https://github.com/aiogram/aiogram/archive/refs/heads/dev-3.x.zip'])

from background import keep_alive

from aiogram import Bot, Dispatcher, types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import startquestion

config = configparser.ConfigParser()
config.read("./config.ini", encoding='utf-8-sig')

TOKEN = config.get('CHS_bot', 'bot_token')


class Anket(StatesGroup):
    name = State()
    date_of_birth = State()
    grade = State()
    town_and_country = State()
    average_marks = State()
    best_subj = State()
    worst_subj = State()
    motivation = State()
    language_of_teach = State()
    form_of_teach = State()
    exp_from_teach = State()
    main_subj = State()
    type_contact = State()
    send = State()


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    dp.include_router(startquestion.router)

    keep_alive()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, non_stop=True, interval=0)


if __name__ == "__main__":
    asyncio.run(main())
