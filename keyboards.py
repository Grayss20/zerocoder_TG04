from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏠 Главное меню"),
        ],
        [
            KeyboardButton(text="тестовая кнопка 2"),
            KeyboardButton(text="тестовая кнопка 3")
        ]
    ],
    resize_keyboard=True
)

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Video", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
            InlineKeyboardButton(text="Каталог", callback_data="catalog")
        ],
        [
            InlineKeyboardButton(text="Новости", callback_data="news"),
            InlineKeyboardButton(text="Профиль", callback_data="person")
        ]
    ]
)

test = ["кнопка 1", "кнопка 2", "кнопка 3", "кнопка 4"]


async def test_keyboard():
    keyboard = InlineKeyboardBuilder()
    for key in test:
        keyboard.add(InlineKeyboardButton(text=key, url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
    return keyboard.adjust(2).as_markup()
