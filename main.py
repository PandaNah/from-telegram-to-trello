from aiogram import executor
import datetime
from aiogram import Dispatcher

from settings import envSettings
from loader import dp


async def on_startup(dp: Dispatcher):
    current_time = datetime.datetime.now().strftime('%d.%m %H:%M')
    for admin in envSettings.ADMIN_LIST:
        await dp.bot.send_message(chat_id=admin,
                                  text=f'Bot starts on {current_time}')


async def on_shutdown(dp: Dispatcher):
    for admin in envSettings.ADMIN_LIST:
        await dp.bot.send_message(chat_id=admin,
                                  text=f'Bot stop work')

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown)