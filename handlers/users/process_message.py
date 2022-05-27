# -*- coding: utf-8 -*-


from gpt_3.preprocessing import (encoding_text, 
                                 decoding_text, 
                                 get_text_gpt3)

from utils.misc.throttling import rate_limit
from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp
import asyncio


"""


    Created on 10.09.2021
    
    @author: Nikita


"""


async def zero_output(message: types.Message) -> types.Message:

    await message.answer(text="Упс...")

    await asyncio.sleep(1)

    await message.answer(text="Что-то я не смог сформулировать ответ, "
                              "попробуйте перефразировать сообщение 🙁")


@rate_limit(3, 'message')
@dp.message_handler()
async def processing_message(message: types.Message, state: FSMContext) -> types.Message:

    """

        The function is designed to receive messages in russian and generate a response.

    """

    await types.ChatActions.typing()

    data_storage = await state.get_data()
    text = message.text.lower()

    await state.update_data(history_text=text)
    await state.update_data(chat_id=message.chat.id)
    await state.update_data(first_name=message.from_user.first_name)

    input_text, check_question = encoding_text(text_encode=text)

    if text == data_storage.get('history_text'):

        await message.answer(text="Ой... Где-то я уже это видел! 🥱")

        # input_text = torch.cat([context.chat_data['output'][-1], input_text[0]], dim=0)
        # input_text = input_text.unsqueeze(0)

        return

    text_gpt3 = get_text_gpt3(text_gpt=input_text, check_question=check_question)
    output_text = decoding_text(text_decode=text_gpt3)

    if len(output_text.split()) < 1:

        await zero_output(message)

        return

    await message.answer(text=output_text)

    if 'input' in data_storage:

        await state.update_data(input=input_text)
        await state.update_data(output=text_gpt3)

        return

    data_history = {'input': [input_text],
                    'output': [text_gpt3]}

    await state.update_data(data_history)
