from telegram_bot import build_signal
from config import SYMBOLSimport os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 به Pourya Trader Bot خوش آمدید.\n\n"
        "بات با موفقیت اجرا شده است.\n"
        "به زودی قابلیت تحلیل بازار و ارسال سیگنال فعال می‌شود."
    )


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot Online")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = ""

    for symbol in SYMBOLS:

        text += build_signal(symbol)

        text += "\n\n------------------------\n\n"

    await update.message.reply_text(text)
def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN environment variable not found.")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ping", ping))

    print("Pourya Trader Bot Started...")

    app.run_polling()


if __name__ == "__main__":
    main()
