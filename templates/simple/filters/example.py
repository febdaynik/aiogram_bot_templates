from aiogram.dispatcher.filters import BoundFilter
from typing import Union
from aiogram import types


class IsExample(BoundFilter):
	key = "is_example"

	def __init__(self, is_example: str):
		self.is_example = is_example

	async def check(self, obj: Union[types.Message, types.CallbackQuery]):
		return self.is_example is True
