from aiogram import types
from aiogram.dispatcher import FSMContext


async def cmd_start(message: types.Message, state: FSMContext):
	return message.answer('Example')
