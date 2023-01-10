import TOKEN
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message, message
from aiogram.dispatcher.filters import Text, Command
import sqlite3
import keyboards
import logging

TOKEN_API = TOKEN.TOKEN

bot = Bot(token=TOKEN_API, parse_mode="HTML")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()

# создаем базу данных
sqlite_connection = sqlite3.connect('sqlite_python.db')
cursor = sqlite_connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(user_id INTEGER, block INTEGER);""")
sqlite_connection.commit()


@dp.message_handler(commands=['start'])
async def start(message: Message):
    cursor.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
    result = cursor.fetchone()

    if result is None:
        cursor.execute(f'''SELECT * FROM users WHERE (user_id="{message.from_user.id}")''')
        entry = cursor.fetchone()
        if entry is None:
            cursor.execute(f'''INSERT INTO users VALUES ('{message.from_user.id}', '0')''')
            sqlite_connection.commit()
            await message.reply("Hello!", reply_markup=keyboards.greet_kb)
    else:
        await message.reply("your block Value is " + str(result[0]), reply_markup=keyboards.greet_kb)


@dp.message_handler(commands=["Generate_text"])
async def text_generator(message: Message, command: Command):
    if command.args:
        await message.answer(f"Вы хотите сгенерировать текст из <b>{command.args}</b> слов")
    else:
        await message.answer("После команды \Generate_text введите количество слов.")


@dp.message_handler(commands=["Help"])
async def help(message: Message):
    await message.answer("...")


@dp.message_handler(commands=["Stat"])
async def stat(message: Message, command: Command):
    print("statistics")
    cursor.execute('''select * from users''')
    results = cursor.fetchall()
    await message.answer(f'Людей которые когда либо заходили в бота: {len(results)}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
