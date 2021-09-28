# -*- coding: utf-8 -*-


from aiogram import types


"""


Created on 10.09.2021

@author: Nikita


"""


async def set_default_commands(dp):

    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("dice", "Подбросить кубик"),
            types.BotCommand("horoscope", "Вывести гороскоп на сегодня"),
            types.BotCommand("weather", "Вывести прогноз погоды"),
        ]
    )
