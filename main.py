import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = ''


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


bosh_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Matematika 🔢"),
            
        ],
        [
            KeyboardButton(text="Fizika 🛢️"),
            KeyboardButton(text="Trud 🪵")  
        ],
        [
            KeyboardButton(text="Ximiya 💩"),
        ],
    ],
    resize_keyboard=True
)



Matematika_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Первый вопрос"),
            KeyboardButton(text="Второй вопрос"),            
        ],
        [
            KeyboardButton(text="Третий вопрос"),
            KeyboardButton(text="Четвертый вопрос"),
        ],
        [
            KeyboardButton(text="Пятый вопрос"),
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)

 
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hello", reply_markup=bosh_menu)

 
@dp.message_handler(text="Matematika 🔢")
async def send_welcome(message: types.Message):
    await message.reply("Mana", reply_markup=Matematika_keyboards)



@dp.message_handler(text="Orqaga")
async def send_welcome(message: types.Message):
    await message.reply("Orqaga", reply_markup=bosh_menu)



@dp.message_handler(text="Первый вопрос")
async def send_welcome(message: types.Message):
   await message.answer_poll(
        question="1+1= ?",
        options=["2569", "4326", "86543", "2345676", "2"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
   



@dp.message_handler(text="Второй вопрос")
async def send_welcome(message: types.Message):
   await message.answer_poll(
        question="матема...?",
        options=["тика", "фига", "привет", "как ты ?", "ЯДЕРНАЯ СТАНЦИЯ"],
        is_anonymous=False,
        correct_option_id=0 ,
        type="quiz"
    )
#    await asyncio.sleep(3)


@dp.message_handler(text="Третий вопрос")
async def send_welcome(message: types.Message):
   await message.answer_poll(
        question="2*2= ?",
        options=["3", "4326", "4", "7", "2"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz"
    )
   



@dp.message_handler(text="Четвертый вопрос")
async def send_welcome(message: types.Message):
   await message.answer_poll(
        question="1+3?",
        options=["автомат", "5", "?", "ахааххаха", "нет правильного ответа"],
        is_anonymous=False,
        correct_option_id=0 ,
        type="quiz"
    )
   



@dp.message_handler(text="Пятый вопрос")
async def send_welcome(message: types.Message):
   await message.answer_poll(
        question="1*1",
        options=["а", "б", "в", "мрекшгп", "гитлер"],
        is_anonymous=False,
        correct_option_id=4 ,
        type="quiz"
    )

















if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
