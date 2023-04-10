from typing import Union

import aiogram
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware


class ExampleMiddleware(BaseMiddleware):

	example: dict = {}

	def __init__(self, latency: Union[int, float] = 0.01):
		self.latency = latency
		super().__init__()

	async def on_process_message(self, message: types.Message, data: dict):
		pass

	async def on_post_process_message(self, message: types.Message, result: dict, data: dict):
		pass
