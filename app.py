# -*- coding: utf-8 -*-


from aiogram import executor

from loader import dp

import middlewares
import filters
import handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


"""


    Created on 15.09.2021

    @author: Nikita


"""


async def on_startup(dispatcher):

    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
