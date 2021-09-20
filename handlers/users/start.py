import logging
import os
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from Jobs.chat_server_aiogram.loader import dp
from Jobs.chat_server_aiogram.middlewares.throttling import rate_limit
from Jobs.chat_server_aiogram.filters.eng_symbols import eng_symbols


@rate_limit(5, 'start')
@dp.message_handler(CommandStart(), eng_symbols())
async def bot_start(message: types.Message, filter):

    logging.info(f'4. Handler = {os.path.basename(__file__)}')
    await message.answer(f"Привет, {message.from_user.full_name}! \n {filter=}")

    return {'from_handler': 'Данные из handler'}
