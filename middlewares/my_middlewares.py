import logging

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler
from Jobs.chat_server_aiogram.data.config import ban_user


class ban_member(BaseMiddleware):

    # 1
    async def on_pre_process_update(self, update: types.Update, data: dict):
        logging.info("-------------Новый апдейт------------------")
        logging.info('1. Pre_process_update')
        data["middleware_data"] = 'Это пройдет до'

        if update.message:
            user_id = update.message.from_user.id

        elif update.callback_query:
            user_id = update.callback_query.from_user.id

        else:
            return

        if user_id in ban_user:
            raise CancelHandler()

    # 2
    async def on_process_update(self, update: types.Update, data: dict):
        logging.info(f'2. Process_update, {data=}')
        pass

    # 3
    async def on_pre_process_message(self, update: types.Update, data: dict):
        logging.info(f'3. Pre_process_message, {data=}')
        data['middleware_data'] = 'Это пройдет до'
        pass

    # 4 Filter

    # 5
    async def on_process_message(self, update: types.Message, data: dict):
        logging.info('5. Pre_process_message')
        data["middleware_data"] = "Это попадет в хендлер"

    # 6 Handler

    # 7
    async def on_post_process_message(self, update: types.Message, data_from_handler: list, data: dict):
        logging.info(f'7. Post_process_message, {data=}, {data_from_handler=}')

