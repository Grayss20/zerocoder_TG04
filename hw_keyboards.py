from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Привет"),
            KeyboardButton(text="Пока")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

inline_keyboard_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="новости", url="https://bbc.co.uk/news"),
            InlineKeyboardButton(text="музыка", url="https://freemusicarchive.org/home"),
            InlineKeyboardButton(text="видео", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        ]
    ]
)

# Создаем клавиатуру с кнопкой "Показать больше"
keyboard_d = InlineKeyboardBuilder()
keyboard_d.add(InlineKeyboardButton(text="Показать больше", callback_data="show_more"))




test = {"Опция 1": "Текст опции 1. Здесь могла бы быть ваша реклама",
        "Опция 2": "Текст опции 2. Здесь могла бы быть ваша реклама"}


async def options_keyboard():
    # Создаем клавиатуру с двумя кнопками: "Опция 1" и "Опция 2"
    keyboard = InlineKeyboardBuilder()
    for key in test.keys():
        # callback_data будет содержать ключ, например, "option:Опция 1"
        keyboard.add(InlineKeyboardButton(text=key, callback_data=f"option:{key}"))
    return keyboard.adjust(2).as_markup()
