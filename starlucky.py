from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = '7923815706:AAEl8rLofcz0ZY_OY0X7NYa1OYE_iPZum0M'

MINI_APP_URL = 'https://semyonmadyanov.github.io/StarLuckyMiniApp/'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Play game🌟", web_app={'url': MINI_APP_URL, 'fullscreen': True})]
    ])

    image_path = "msg_bg.png"

    if os.path.exists(image_path):
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open(image_path, 'rb'),
            caption="<b>⭐ Welcome to Star Lucky! ⭐</b>\n\n"
                    "<b>Star Lucky</b> is an exciting Telegram Mini App where you can spin the wheel and win amazing prizes!\n\n"
                    "🔥 Don't miss your chance to win big! Join players who have already discovered the magic of <b>Star Lucky</b>.\n\n"
                    "👉 Hurry up and press the button below to start playing!",
            parse_mode='HTML',
            reply_markup=keyboard
        )
    else:
        await update.message.reply_html(
            "<b>Ошибка:</b> Изображение не найдено. Пожалуйста, проверьте наличие файла msg_bg.png."
        )

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))

    application.run_polling()