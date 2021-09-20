import asyncio
import logging
from aiogram import types, Dispatcher
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import Throttled
from Jobs.chat_server_aiogram.loader import dp
from Jobs.chat_server_aiogram.data.config import ban_user


def rate_limit(limit: int, key=None):

    """

    Decorator for configuring rate limit and key in different functions.
    :param limit:
    :param key:
    :return:

    """

    def decorator(func):

        setattr(func, 'throttling_rate_limit', limit)

        if key:
            setattr(func, 'throttling_key', key)

        return func

    return decorator


class ThrottlingMiddleware(BaseMiddleware):

    """

    Simple middleware

    """

    def __init__(self, limit=DEFAULT_RATE_LIMIT, key_prefix='antiflood_'):
        self.rate_limit = limit
        self.prefix = key_prefix
        super(ThrottlingMiddleware, self).__init__()

    async def on_pre_process_update(self, update: types.Update, data: dict):

        logging.info("-------------Новый апдейт------------------")
        logging.info('1. Pre_process_update')
        # data["middleware_data"] = 'Это пройдет до'

        if update.message:
            user_id = update.message.from_user.id

        elif update.callback_query:
            user_id = update.callback_query.from_user.id

        else:
            return

        if user_id in ban_user:
            raise CancelHandler()

    # # 2
    # async def on_process_update(self, update: types.Update, data: dict):
    #     logging.info(f'2. Process_update, {data=}')
    #     pass
    #
    # # 3
    # async def on_pre_process_message(self, update: types.Update, data: dict):
    #     logging.info(f'3. Pre_process_message, {data=}')
    #     data['middleware_data'] = 'Это пройдет до'
    #     pass

    # 4 Filters

    # 5
    async def on_process_message(self, message: types.Message, data: dict):

        logging.info('2. Pre_process_message')
        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()

        if handler:

            limit = getattr(handler, "throttling_rate_limit", self.rate_limit)
            key = getattr(handler, "throttling_key", f"{self.prefix}_{handler.__name__}")

        else:

            limit = self.rate_limit
            key = f"{self.prefix}_message"

        # Use Dispatcher.throttle method.
        try:
            await dispatcher.throttle(key, rate=limit)

        except Throttled as t:

            await self.message_throttled(message, t)
            raise CancelHandler()

    async def message_throttled(self, message: types.Message, throttled: Throttled):

        """

        Notify user only on first exceed and notify about unlocking only on last exceed

        :param message:
        :param throttled:

        """

        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()

        if handler:
            key = getattr(handler, 'throttling_key', f"{self.prefix}_{handler.__name__}")

        else:
            key = f"{self.prefix}_message"

        # Calculate how many time is left till the block ends
        delta = throttled.rate - throttled.delta

        # Prevent flooding
        if throttled.exceeded_count <= 2:
            await message.reply('Too many requests!')

        # Sleep.
        await asyncio.sleep(delta)

        # Check lock status
        thr = await dispatcher.check_key(key)

        # If current message is not last with current key - do not send message
        if thr.exceeded_count == throttled.exceeded_count:
            await message.reply('Unlocked.')


# @dp.message_handler(commands=['start'])
# @rate_limit(5, 'start')  # this is not required but you can configure throttling manager for current handler using it
# async def cmd_test(message: types.Message):
#
#     # You can use this command every 5 seconds
#     await message.reply('Test passed! You can use this command every 5 seconds.')
