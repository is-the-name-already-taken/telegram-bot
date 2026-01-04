from telegram import (
    Update,
    BotCommand,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import ContextTypes


async def set_commands(app):
    await app.bot.set_my_commands([BotCommand("start", "Start")])
    return


async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello")
    return


async def delete_this_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="This command will be deleted")
    await update.message.delete()
    return

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"You said: {text}")
    return


async def keyboard_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["/start", "Show Recent Data"], ["Delete Data"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Please choose an option:", reply_markup=reply_markup
    )
    return


async def inkeyboard_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Fetch Data", callback_data="fetch"),
            InlineKeyboardButton("Help", callback_data="help"),
        ],
        [InlineKeyboardButton("Go to Google", url="https://google.com")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Select an action:", reply_markup=reply_markup)
    return


async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "fetch":
        await query.edit_message_text(text="Fetching data...")
    elif query.data == "help":
        await query.edit_message_text(text="Help section")
    return
