import logging

from aiogram import Dispatcher

from Jobs.chat_server_aiogram.data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):

    for admin in ADMINS:

        try:
            await dp.bot.send_message(admin, "Бот Запущен")

        except Exception as err:
            logging.exception(err)
