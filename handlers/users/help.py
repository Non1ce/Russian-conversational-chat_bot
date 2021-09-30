# -*- coding: utf-8 -*-


from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram import types
from loader import dp


"""


    Created on 10.09.2021
    
    @author: Nikita


"""


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/dice - Подкинуть кубик")
    
    await message.answer("\n".join(text))
