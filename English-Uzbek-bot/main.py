import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from oxfordApi import getDefinitions
from googletrans import Translator
translator = Translator()

API_TOKEN = '1907317088:AAFwA3OMsTK5GqZFG7oJXl6-YMwlUPDr5S8'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	await message.reply(
		"Hi!\nThis bot is specially made for english dictionary\n\tWelcome to Dictionary Uz-Eng bot\nDo you need any help /help")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
	await message.reply(
		"Thanks for choosing Dictionary uz-eng bot.\n-Enter words in uzbek to know english meaning\n-Enter english words to know the definition ")


@dp.message_handler()
async def tarjimon(message: types.Message):
    print(message)
    lang = translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang == 'en' else 'en'
        await message.reply(translator.translate(message.text, dest).text)
    else:
        if lang=='en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text, dest='en').text

        lookup = getDefinitions(word_id)
        if lookup:
            await message.reply(f"Word: {word_id} \nDefinitions:\n{lookup['definitions']}")
            if lookup.get('audio'):
                await message.reply_voice(lookup['audio'])
        else:
            await message.reply("Bunday so'z topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)