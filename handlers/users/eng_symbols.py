# -*- coding: utf-8 -*-


from utils.misc.throttling import rate_limit
from aiogram import types
from loader import dp
import asyncio


"""

    Created on 10.09.2021

    @author: Nikita


"""


@rate_limit(5, 'eng_symbols')
@dp.message_handler(regexp=r'^[a-zA-Z\W]+$')
async def bot_message(message: types.Message):

    """

    The function is designed for processing messages
    containing english symbols.

    """

    await types.ChatActions.typing()
    await asyncio.sleep(1)

    await message.answer("Извините, на данный момент, я не разговариваю на английском языке. 🤐")
