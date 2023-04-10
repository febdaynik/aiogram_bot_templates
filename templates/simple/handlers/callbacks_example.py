from aiogram import types
from aiogram.dispatcher import FSMContext


async def back_callback(call: types.CallbackQuery, state: FSMContext):
	await call.answer()
