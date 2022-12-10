import TOKEN
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

TOKEN_API = TOKEN.TOKEN

bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer("Hello!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)