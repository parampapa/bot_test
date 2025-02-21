import asyncio

from aiogram import Router, F, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.enums import ChatAction

import app.keyboards as kb


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id, action=ChatAction.TYPING)
    await asyncio.sleep(0.5)
    await message.answer('Ты нажал /start', reply_markup=ReplyKeyboardRemove())


@router.message(Command('hello'))
async def cmd_hello(message: Message):
    await message.answer(f'Привет! {message.from_user.first_name}', reply_markup=kb.inline_main)




@router.message(Command('adminlist'))
async def adminlist(message: Message):
    admins = await message.bot.get_chat_administrators(chat_id=-100)
    admin_list = '\n'.join([f'Полное имя 👤 - {admin.user.full_name}, username - @{admin.user.username}' for admin in admins])
    await message.answer(f'Администраторы чата:\n{admin_list}')




@router.message(Command("pin"))
async def pin_custom_message(message: Message, bot: Bot):
    chat_id = -100  # Юзернейм или ID канала
    # Получаем текст после команды "/pin"
    command_parts = message.text.split(maxsplit=1)
    if len(command_parts) < 2:
        await message.answer("❌ Ошибка! Напишите текст после /pin.\nПример: `/pin Важное сообщение`")
        return
    pin_text = command_parts[1] # Берем текст после /pin
    # Бот отправляет сообщение с этим текстом
    sent_message = await bot.send_message(chat_id=chat_id, text=pin_text)
    # Бот закрепляет это сообщение
    await bot.pin_chat_message(chat_id=chat_id, message_id=sent_message.message_id)

    await message.answer("✅ Сообщение закреплено!")



