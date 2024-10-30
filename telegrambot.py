from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '7613413804:AAFS9CQ0gNVguHEH0OBtQ398R98O1dnjP6w'

# Define the start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! I am your Polize Doge bot. Report any scams or ask questions.")

# Define the report command for reporting scams
async def report(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        report_message = ' '.join(context.args)
        await update.message.reply_text(f"Thank you for reporting. We'll investigate: {report_message}")
    else:
        await update.message.reply_text("Please include details in your report. Usage: /report [details]")

# Define a help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Use /start to begin. Use /report to report scams. Use /help for this message.")

# Main function to start the bot
def main():
    # Initialize the bot application
    application = Application.builder().token(BOT_TOKEN).build()

    # Register commands
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("report", report))
    application.add_handler(CommandHandler("help", help_command))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()

