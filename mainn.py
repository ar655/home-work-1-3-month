from aiogram import types
from aiogram.utils import executor
from config import bot,dp
from aiogram.types import ParseMode,InlineKeyboardMarkup,InlineKeyboardButton
import logging

@dp.message_handler(commands=['0'])
async def question_handler(message:types.Message):
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("NEXT", callback_data='button1')
    markup.add(button1)

    question = 'как перевести type с английского'
    answers = [
        'тип ','выбор','писать','привет'
    ]
    await bot.send_poll(
        chat_id= message.chat.id,
        question = question,
        options= answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='тип',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

@dp.callback_query_handler(lambda call:call.data=='button1')
async def question_handler2(call:types.CallbackQuery):


    question = 'как перевести if с английского '
    answers = [
        'если ','вчера','день','завтрак'
    ]
    await bot.send_poll(
        chat_id= call.message.chat.id,
        question = question,
        options= answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='если',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,

    )




@dp.message_handler(commands=['meme'])
async def meme_handler(message:types.Message):
    media1 = open('media/img.png','rb')
    await bot.send_photo(message.from_user.id,photo=media1)

@dp.message_handler()
async def echo(message:types.Message):
   print(message)

   if message.text.isnumeric():

       message.text= int(message.text)
       await bot.send_message(message.from_user.id, message.text **2)
   else:
       await bot.send_message(message.from_user.id,message.text)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp,skip_updates=True)