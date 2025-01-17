import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import aiohttp
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

# Bot configuration
TELEGRAM_TOKEN = '7698977190:AAG08vvAS61KxtUtbUyBgnQ7f2o-ghH1QpU'
ALERT_CHAT_ID = '5049639969'

# Configuration for exchanges and pairs
EXCHANGES = {
    'binance': 'https://api.binance.com/api/v3/ticker/price?symbol=',
    'kraken': 'https://api.kraken.com/0/public/Ticker?pair=',
}

CRYPTO_PAIRS = ['BTCUSDT', 'ETHUSDT']
PRICE_RANGES = {
    'BTCUSDT': (10000, 100000),
    'ETHUSDT': (1000, 10000),
}
KRAKEN_PAIRS = {
    'BTCUSDT': 'XXBTZUSD',
    'ETHUSDT': 'XETHZUSD',
}

async def start(update: Update, context):
    await update.message.reply_text('Hello! I am your crypto bot.')

async def echo(update: Update, context):
    await update.message.reply_text(update.message.text)

async def main():
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    # Scheduler setup
    scheduler = AsyncIOScheduler()
    scheduler.start()

    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    await application.updater.idle()

if __name__ == '__main__': 
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())