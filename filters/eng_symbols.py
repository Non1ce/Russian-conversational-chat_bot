import logging

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.handler import ctx_data


class eng_symbols(BoundFilter):

    async def check(self, message: types.Message):
        data = ctx_data.get()
        logging.info(f'3. Filter {data=}')

        return {'filter': "Данные из фильтра"}
