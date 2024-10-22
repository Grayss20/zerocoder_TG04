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
import hw_keyboards as hk

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())


# Команда /dynamic: Показываем кнопку "Показать больше"
@dp.message(Command("dynamic"))
async def show_more_button(message: Message):
    # Отправляем сообщение с кнопкой "Показать больше"
    await message.answer("Нажмите кнопку, чтобы увидеть опции", reply_markup=hk.keyboard_d.as_markup())

# Обработка нажатия на кнопку "Показать больше"
@dp.callback_query(F.data == "show_more")
async def show_options(call: CallbackQuery):
    # Редактируем сообщение, заменяя кнопку "Показать больше" на новые кнопки
    await call.message.edit_reply_markup(reply_markup=await hk.options_keyboard())
    await call.answer()  # Подтверждаем нажатие на кнопку


# Обработка нажатия на кнопки "Опция 1" или "Опция 2"
@dp.callback_query(F.data.startswith("option:"))
async def option_selected(call: CallbackQuery):
    # Извлекаем название опции из callback_data
    option_key = call.data.split(":")[1]
    # Отправляем сообщение с текстом, соответствующим выбранной опции
    await call.message.answer(hk.test[option_key])
    await call.answer()  # Подтверждаем нажатие на кнопку


@dp.message(Command("links"))
async def links(message: Message):
    await message.answer("Ссылки", reply_markup=hk.inline_keyboard_1)


@dp.message(F.text == "Привет")
async def hello(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}")


@dp.message(F.text == "Пока")
async def hello(message: Message):
    await message.answer(f"До свидания, {message.from_user.full_name}")


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Стартуем...", reply_markup=hk.main)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
