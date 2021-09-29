# -*- coding: utf-8 -*-


from Jobs.chatbot.utils.misc.tg_html import mention_html
from Jobs.chatbot.data.config import ADMINS
from Jobs.chatbot.loader import dp, bot
from aiogram import types
import traceback
import logging
import sys


"""


    Created on 10.09.2021

    @author: Nikita


"""


@dp.errors_handler()
async def error(update: types.Update, exception):

    """

    The function is designed for processing errors.

    """

    if update.message or update.edited_message:

        text = "К сожалению произошла ошибка в момент обработки сообщения... " \
               "Мы уже работаем над этой проблемой. 🤔"

        await update.message.reply(text=text)

    trace = "".join(traceback.format_tb(sys.exc_info()[2]))
    payload = []

    if update.message.from_user:

        bad_user = await mention_html(update.message.from_user.id, update.message.from_user.first_name)
        payload.append(f' с пользователем {bad_user}')

    if update.channel_post or update.edited_channel_post:
        payload.append(f' внутри чата <i>{update.edited_channel_post}</i>')

        if update.channel_post.from_user.username:
            payload.append(f' (@{update.channel_post.from_user.username})')

    if update.poll:
        payload.append(f' с id опроса {update.poll.id}.')

    text = f"Ошибка <code>{exception}</code> случилась{''.join(payload)}. " \
           f"Полная трассировка:\n\n<code>{trace}</code>"

    for dev_id in ADMINS:

        await bot.send_message(chat_id=dev_id,
                               text=text,
                               parse_mode=types.ParseMode.HTML)

    logging.exception(f'Update: {update} \n{exception}')
