# -*- coding: utf-8 -*-


from Jobs.chatbot.utils.misc.throttling import rate_limit
from Jobs.chatbot.utils.misc.tg_html import mention_html
from Jobs.chatbot.loader import dp
from aiogram import types


"""

    Created on 10.09.2021
    
    @author: Nikita


"""


@rate_limit(10, 'start')
@dp.message_handler(commands='start')
async def bot_start(message: types.Message):

    """


    The function is designed to welcome a new bot user.


    """

    await types.ChatActions.typing()

    first_name = message.from_user.first_name

    devs_id = await mention_html("no_n1ce", "Nikita")

    await message.answer(
        text=f"Привет, {first_name}! Я создатель этого разговорного чат-бота 🤔."
             f" По всем вопросам, можешь написать мне {devs_id}!",
        parse_mode=types.ParseMode.HTML)
