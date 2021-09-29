# -*- coding: utf-8 -*-


from Jobs.chatbot.utils.misc.throttling import rate_limit
from Jobs.chatbot.loader import dp
from aiogram import types


"""

    Created on 10.09.2021
    
    @author: Nikita


"""


@rate_limit(5, 'sticker')
@dp.message_handler(content_types=types.ContentTypes.STICKER)
async def bot_start(message: types.Message):

    """

    The function is designed to welcome a new bot user.

    """

    await types.ChatActions.typing()

    sticker_id = message.sticker.file_id

    await message.answer_sticker(
        sticker=sticker_id)
