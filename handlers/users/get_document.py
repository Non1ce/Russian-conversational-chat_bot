# -*- coding: utf-8 -*-

from Jobs.chat_server_aiogram.middlewares.throttling import rate_limit
from Jobs.chat_server_aiogram.loader import dp

from aiogram import types

import asyncio
import logging
import os


"""

    Created on 10.09.2021
    
    @author: Nikita


"""


@rate_limit(5, 'document')
@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def bot_start(message: types.Message):

    """

    The function is designed to welcome a new bot user.

    """

    logging.info(f'Handler = {os.path.basename(__file__)}')

    await types.ChatActions.typing()

    doc = message.document
    filename = doc.file_name

    await message.answer(text=filename[::-1])

    await asyncio.sleep(1)

    await message.answer_sticker(
        sticker='CAACAgIAAxkBAAIEnWFCAzRDD0iWcjsKtAYZ1GY417JlAAKbDQAComVgStTV03Zsw0QpIAQ')
