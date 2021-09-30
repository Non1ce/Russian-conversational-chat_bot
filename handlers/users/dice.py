# -*- coding: utf-8 -*-


from utils.misc.throttling import rate_limit
from aiogram import types
from loader import dp
import asyncio


"""

    Created on 29.09.2021

    @author: Nikita


"""


@rate_limit(5, 'dice')
@dp.message_handler(commands='dice')
async def bot_message(message: types.Message):

    """

    The function is designed for tossing a dice.

    """

    await types.ChatActions.typing()

    user = await message.bot.send_dice(chat_id=message.chat.id)
    await asyncio.sleep(1)

    bot = await message.bot.send_dice(chat_id=message.chat.id)
    await asyncio.sleep(3)

    await asyncio.sleep(1)
    if user.dice.value > bot.dice.value:
        await message.answer(f"Выиграл {message.from_user.first_name}!")

    elif user.dice.value < bot.dice.value:
        bot_name = await message.bot.get_me()
        await message.answer(f"Выиграл {bot_name.first_name}!")

    else:
        await message.answer("Ничья!")
