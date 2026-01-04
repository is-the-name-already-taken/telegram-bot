from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler
from telegram.ext._handlers.commandhandler import CommandHandler

import modules
import traceback

def main():
    user_filter = filters.User(user_id=modules.ALLOWED_USERS)
    
    app = ApplicationBuilder().token(modules.TOKEN).post_init(modules.set_commands).build()
    
    app.add_handler(CommandHandler("start", modules.start_cmd, filters=user_filter))
    app.add_handler(CommandHandler("k", modules.keyboard_cmd, filters=user_filter))
    app.add_handler(CommandHandler("ik", modules.inkeyboard_cmd, filters=user_filter))
    app.add_handler(CommandHandler("delete_this", modules.delete_this_cmd, filters=user_filter))
    
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND & user_filter, modules.reply))
    
    app.add_handler(CallbackQueryHandler(modules.button_callback))
    

    print("Bot is running...")

    try:
        app.run_polling()
    except Exception as e:
        traceback.print_exc()


if __name__ == "__main__":
    main()
