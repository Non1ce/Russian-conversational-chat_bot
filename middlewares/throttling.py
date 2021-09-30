# -*- coding: utf-8 -*-


from aiogram.dispatcher.handler import CancelHandler, current_handler
from utils.db_api.set_ban_members import ban_members
from utils.db_api.unban_members import unban_member
from data.config import ban_time, exceeded_count
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.utils.exceptions import Throttled
from aiogram import types, Dispatcher
import asyncio


"""


    Created on 26.09.2021
    
    @author: Nikita


"""


class ThrottlingMiddleware(BaseMiddleware):

    def __init__(self, limit=DEFAULT_RATE_LIMIT, key_prefix='antiflood_'):

        self.rate_limit = limit
        self.prefix = key_prefix

        super(ThrottlingMiddleware, self).__init__()

    async def on_pre_process_update(self, update: types.Update, data: dict):

        if update.message:
            user_id = update.message.from_user.id

        elif update.callback_query:
            user_id = update.callback_query.from_user.id

        else:
            return

        if user_id in await unban_member(user_id=user_id, ban_time=ban_time):

            raise CancelHandler()

    async def on_process_message(self, message: types.Message, data: dict):

        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()

        if handler:

            limit = getattr(handler, "throttling_rate_limit", self.rate_limit)
            key = getattr(handler, "throttling_key", f"{self.prefix}_{handler.__name__}")

        else:

            limit = self.rate_limit
            key = f"{self.prefix}_message"

        try:
            await dispatcher.throttle(key, rate=limit)

        except Throttled as t:

            await self.message_throttled(message, t)
            raise CancelHandler()

    async def message_throttled(self, message: types.Message, throttled: Throttled):

        """


        Notify user only on first exceed and notify about unlocking only on last exceed


        """

        # Prevent flooding
        if throttled.exceeded_count == exceeded_count:

            await message.reply('Слишком много запросов 😤!')

            await ban_members(user_id=throttled.user,
                              time_out=throttled.called_at)

            await message.reply(f'Вы были заблокированы, на {ban_time} секунд!')

            await asyncio.sleep(ban_time)

            await message.reply('Вас разблокировали, теперь Вы снова можете пообщаться со мной 🧐!')
