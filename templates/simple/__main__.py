# Основной файл для запуска бота
import logging

from aiogram import executor, types

from loader import dp
from handlers import example as handler_example, callbacks_example
from filters.example import IsExample
from middlewares.example import ExampleMiddleware
from cbdata import cb_back


async def on_startup(_):
	logging.info("Bot started")

# Middlewares
dp.middleware.setup(ExampleMiddleware())

# Filters
dp.filters_factory.bind(IsExample)

# Handlers
dp.register_callback_query_handler(callbacks_example.back_callback, cb_back.filter(), chat_type=types.ChatType.PRIVATE, state='*')

dp.register_message_handler(handler_example.cmd_start, commands=['start'], chat_type=types.ChatType.PRIVATE, state='*')


if __name__ == '__main__':
	logging.basicConfig(
		level=logging.INFO,
		filename='log_file.log',
		format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
	)

	logging.info('Start logger')
	print("Starting bot")

	executor.start_polling(dp, on_startup=on_startup)

	logging.info('Stop logger\n')
