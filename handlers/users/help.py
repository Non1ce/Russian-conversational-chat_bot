# -*- coding: utf-8 -*-


from aiogram.dispatcher.filters.builtin import CommandHelp
from Jobs.chatbot.loader import dp
from aiogram import types


"""


Created on 10.09.2021

@author: Nikita


"""


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/dice - Подкинуть кубик",
            "/horoscope - Получить гороскоп")
    
    await message.answer("\n".join(text))
