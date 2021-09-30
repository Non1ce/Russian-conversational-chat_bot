# -*- coding: utf-8 -*-


from data.config import ADMINS
from aiogram import Dispatcher
import logging


"""


Created on 10.09.2021

@author: Nikita


"""


async def on_startup_notify(dp: Dispatcher):

    for admin in ADMINS:

        try:
            data_bot = await dp.bot.get_me()

            await dp.bot.send_message(admin,
                                      f"{data_bot.first_name} успешно запущен!")

        except Exception as err:
            logging.exception(err)
