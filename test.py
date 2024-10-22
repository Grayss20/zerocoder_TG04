import random
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from config import TOKEN
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Тестовый словарь с опциями и текстами
test = {
    "Опция 1": "Текст опции 1. Здесь могла бы быть ваша реклама",
    "Опция 2": "Текст опции 2. Здесь могла бы быть ваша реклама"
}

# Команда /dynamic: Показываем кнопку "Показать больше"
@dp.message(Command("dynamic"))
async def show_more_button(message: Message):
    # Создаем клавиатуру с кнопкой "Показать больше"
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Показать больше", callback_data="show_more"))

    # Отправляем сообщение с кнопкой "Показать больше"
    await message.answer("Нажмите кнопку, чтобы увидеть опции", reply_markup=keyboard.as_markup())

# Обработка нажатия на кнопку "Показать больше"
@dp.callback_query(F.data == "show_more")
async def show_options(call: CallbackQuery):
    # Создаем клавиатуру с двумя кнопками: "Опция 1" и "Опция 2"
    keyboard = InlineKeyboardBuilder()
    for key in test.keys():
        # callback_data будет содержать ключ, например, "option:Опция 1"
        keyboard.add(InlineKeyboardButton(text=key, callback_data=f"option:{key}"))

    # Редактируем сообщение, заменяя кнопку "Показать больше" на новые кнопки
    await call.message.edit_reply_markup(reply_markup=keyboard.adjust(2).as_markup())
    await call.answer()  # Подтверждаем нажатие на кнопку

# Обработка нажатия на кнопки "Опция 1" или "Опция 2"
@dp.callback_query(F.data.startswith("option:"))
async def option_selected(call: CallbackQuery):
    # Извлекаем название опции из callback_data
    option_key = call.data.split(":")[1]
    # Отправляем сообщение с текстом, соответствующим выбранной опции
    await call.message.answer(test[option_key])
    await call.answer()  # Подтверждаем нажатие на кнопку

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
