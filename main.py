from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from keyboards import markup_vol

from config import TOKEN, accept_users
from volume import volume_plus, volume_minus, volume_set, google_start, yt_fullscreen, yt_pause, google_clstr



bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(msg: types.Message):
    user_id = msg.from_user.id
    if user_id in accept_users:
        await msg.reply("Привет!", reply_markup=markup_vol)


@dp.message_handler()
async def echo_message(msg: types.Message):
    user_id = msg.from_user.id
    if user_id in accept_users:
        print(user_id)
        if msg.text == 'Громче':
            volume_plus()
            await bot.send_message(user_id, 'Уровень звука увеличен!')
        elif msg.text == 'Тише':
            volume_minus()
            await bot.send_message(user_id, 'Уровень звука уменьшен!')
        elif msg.text.isdigit() is True:
            if int(msg.text) > 100:
                volume_set(int(100))
                await bot.send_message(user_id, f'Уровень звука установлен на 100')
            else:
                volume_set(int(msg.text))
                await bot.send_message(user_id, f'Уровень звука установлен на {msg.text}')
        elif 'http' in msg.text:
            google_start(msg.text)
            await bot.send_message(user_id, f'Открываю браузер')
        elif 'Полноэкранный YT' in msg.text:
            yt_fullscreen()
        elif 'Пауза' in msg.text:
            yt_pause()
        elif 'Закрыть вкладку' in msg.text:
            google_clstr()


if __name__ == '__main__':
    executor.start_polling(dp)
