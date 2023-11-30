from aiogram import Bot, Dispatcher, types, executor


TOKEN = "6567554082:AAGJXLiViuiBwWS7SjH460aJFrNhhZEqHvU"
MOVIES_CHANNEL = -1002052625693
movies = [2,3,4]

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start_answer(msg: types.Message):
    await msg.answer("botga hush kelibsiz")

@dp.message_handler()
async def echo(msg: types.Message):

    if int(msg.text) in movies:
        await bot.copy_message(chat_id=msg.from_user.id, from_chat_id=MOVIES_CHANNEL, message_id=int(msg.text))
    else:
        await msg.answer("bunday kino topilmadi")


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)