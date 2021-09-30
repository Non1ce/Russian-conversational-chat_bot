# -*- coding: utf-8 -*-


from utils.misc.throttling import rate_limit
from aiogram import types
from loader import dp
import asyncio


"""

    Created on 10.09.2021

    @author: Nikita


"""


@rate_limit(5, 'unknown_symbol')
@dp.message_handler(regexp=r'^[\W]+$')
async def bot_message(message: types.Message):

    """

    The function is designed for processing messages
    consist of only symbols punctuation, empty symbols and etc.

    """

    await types.ChatActions.typing()

    await message.answer("Упс...")
    await asyncio.sleep(2)
    await message.answer("Что-то я Вас не понял, попробуйте сформулировать мысль яснее 🧐")
