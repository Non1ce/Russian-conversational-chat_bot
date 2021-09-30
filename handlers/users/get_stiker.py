# -*- coding: utf-8 -*-


from utils.misc.throttling import rate_limit
from aiogram import types
from loader import dp


"""

    Created on 10.09.2021
    
    @author: Nikita


"""


@rate_limit(5, 'sticker')
@dp.message_handler(content_types=types.ContentTypes.STICKER)
async def bot_start(message: types.Message):

    """

    The function is designed to process the sticker.

    """

    await types.ChatActions.typing()

    sticker_id = message.sticker.file_id

    await message.answer_sticker(
        sticker=sticker_id)
