import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from tinydb import TinyDB

# ───── load env ─────
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ───── database ─────
db = TinyDB("db.json")  # this file is gitignored

# ───── handlers ─────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, world!")

# ───── main ─────
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Bot is up!")
    app.run_polling()
