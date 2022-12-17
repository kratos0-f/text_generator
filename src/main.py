import TOKEN
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from aiogram.dispatcher.filters import Text, Command

import keyboards

TOKEN_API = TOKEN.TOKEN

bot = Bot(token=TOKEN_API, parse_mode="HTML")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.reply("Hello!", reply_markup=keyboards.greet_kb)

@dp.message_handler(commands=["Generate_text"])
async def text_generator(message: Message, command: Command):
    if command.args:
        await message.answer(f"Вы хотите сгенерировать текст из <b>{command.args}</b> слов")
    else:
        await message.answer("После команды \Generate_text введите количество слов.")

@dp.message_handler(commands=["Help"])
async def help(message: Message):
    await message.answer("...")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)