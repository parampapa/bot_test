from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог'),
     KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Контакты')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт ниже'
)

inline_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog'),
     InlineKeyboardButton(text='Корзина', callback_data='cart')],
    [InlineKeyboardButton(text='Контакты', callback_data='contacts')],
    ]
)


back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='catalog'),]

])

cart = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Добавить в корзину',
                          callback_data='add_to_cart'),
     InlineKeyboardButton(text='Перейти к оплате',
                          callback_data='checkout')],
    [InlineKeyboardButton(text='Очистить корзину',
                          callback_data='clear_cart'),]
])


async def builder_catalog():
    brands = ['Adidas', 'Nike', 'Puma', 'New Balance']
    keyboard = InlineKeyboardBuilder()
    for brand in brands:
        keyboard.add(InlineKeyboardButton(text=brand,
                                          callback_data=f'item_{brand}'))
    return keyboard.adjust(2).as_markup()
