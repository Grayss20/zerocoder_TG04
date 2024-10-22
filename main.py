import random
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from config import TOKEN
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import aiohttp
import keyboards

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())


@dp.callback_query(F.data == "news")
async def news(callback: CallbackQuery):
    await callback.answer("Новости подгружаются", show_alert=True)
    await callback.message.edit_text("Вот Новости", reply_markup=await keyboards.test_keyboard())

@dp.message(F.text == "🏠 Главное меню")
async def main_menu(message: Message):
    await message.answer("Главное меню", reply_markup=keyboards.inline_keyboard)


@dp.message(Command("photo"))
async def photo(message: Message):
    photo_list = [
        'https://t3.ftcdn.net/jpg/09/41/44/72/360_F_941447278_Bh1lLtR1kaVP3lcNh11MDNrCBRcG3bu7.jpg',
        'https://media.istockphoto.com/id/93210320/photo/young-siamese-sable-ferret-kit.jpg?s=612x612&w=0&k=20&c=8-_kkouFkllyrsexTFo82su-GbrO_V3z_LbL7MX5hTU=',
        'https://media.gettyimages.com/id/97086548/photo/pet-ferret.jpg?s=612x612&w=gi&k=20&c=xp7Hs15_YVMeuRIJhbeB-09X7Hv85EIGQDWdknTu92M='
    ]
    rand_photo = random.choice(photo_list)
    await message.answer_photo(photo=rand_photo, caption="Вот такая фотка")


@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)


@dp.message(F.text == "Что такое ИИ?")
async def aitext(message: Message):
    await message.answer(
        "Искусственный интеллект — это свойство искусственных интеллектуальных систем выполнять творческие функции, которые традиционно считаются прерогативой человека; наука и технология создания интеллектуальных машин, особенно интеллектуальных компьютерных программ")


@dp.message(Command("help"))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды: \n /start \n /help \n /weather \n /photo")


@dp.message(CommandStart())
async def start(message: Message):
    await message.reply("Hello! I am a bot", reply_markup=keyboards.inline_keyboard)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
