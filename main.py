from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message
import asyncio
from integration import make_conversetion
from databases import create_databases, check_user
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot  = Bot(token=TOKEN)

dp = Dispatcher() 

def reply_definition_button():
    kbs_1 = [
        [types.KeyboardButton(text='Platinum')],[types.KeyboardButton(text='Gold')],[types.KeyboardButton(text='Premium')]
    ]
    
    btns_1 = types.ReplyKeyboardMarkup(keyboard=kbs_1, resize_keyboard=True)
    return btns_1

TARIF_ROYHATI = {
    "Platinum": "Siz Platinum ta'rifini tanladingiz. Bu tarif maxsus xizmatlarni o‘z ichiga oladi.",
    "Gold": "Siz Gold ta'rifini tanladingiz. Bu tarif o‘rtacha xizmatlar uchun mos.",
    "Premium": "Siz Premium ta'rifini tanladingiz. Bu tarif yuqori sifatli xizmatlarni taqdim etadi."
}

@dp.message(CommandStart())
async def start(message: Message):
    await message.reply(text=f'{message.from_user.first_name} What can I help with?')

@dp.message(lambda message: message.text == "Tariflarni ko'rish")
async def show_tariffs(message: Message):
    await message.reply("Ta'riflar:", reply_markup=reply_definition_button())  

@dp.message(lambda message: message.text in TARIF_ROYHATI)
async def definition(message: Message):
    await message.reply(TARIF_ROYHATI[message.text])

@dp.message(lambda message: message.text in TARIF_ROYHATI)
async def definition(message: Message):
    await message.reply(TARIF_ROYHATI[message.text])

@dp.message()
async def speak(message: Message):
    if not check_user(message.from_user.id):
        await message.reply("Sizda kunlik limit tugadi. Iltimos, kunlik obunani sotib oling.", reply_markup=reply_definition_button())
        return
    response_from_gemini = make_conversetion(message.text)
    await message.answer(response_from_gemini)

async def main():
    create_databases()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())