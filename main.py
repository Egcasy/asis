from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = "5775859"

async def start(update: Update, context):
    await update.message.reply_text("Hello! I'm your bot. How can I assist you?")

async def help_command(update: Update, context):
    await update.message.reply_text("Send me any message, and I'll echo it back!")

async def echo(update: Update, context):
    await update.message.reply_text(update.message.text)

# Main function to run the bot
def main():
    app = Application.builder().token(TOKEN).build()
    
    # Command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    
    # Message handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # Start the bot
    app.run_polling()

if __name__ == "__main__":
    main()
