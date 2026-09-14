"""
سیٹنگز فائل - تمام کنفیگریشن یہاں ہے
Configuration File - All settings here
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ===== BINANCE API کی معلومات =====
BINANCE_API_KEY = os.getenv('BINANCE_API_KEY', 'آپ کی API KEY')
BINANCE_API_SECRET = os.getenv('BINANCE_API_SECRET', 'آپ کی SECRET KEY')

# ===== ٹریڈنگ سیٹنگز =====
TRADING_PAIR = 'BTCUSDT'  # کون سی چیز کی ٹریڈنگ کریں؟
# مثالیں: BTCUSDT, ETHUSDT, BNBUSDT, ADAUSDT

TRADING_AMOUNT = 100  # کتنے USDT سے ٹریڈ کریں
MAX_TRADES_PER_DAY = 5  # ایک دن میں زیادہ سے زیادہ ٹریڈز

# ===== Moving Average سٹریٹیجی =====
SHORT_MA_PERIOD = 10  # چھوٹی اوسط (دن)
LONG_MA_PERIOD = 30   # لمبی اوسط (دن)

# اگر SHORT MA > LONG MA → خریدیں (BUY)
# اگر SHORT MA < LONG MA → بیچیں (SELL)

# ===== منافع اور نقصان =====
TAKE_PROFIT_PERCENT = 2.0  # 2% منافع پر بیچ دیں
STOP_LOSS_PERCENT = 1.0    # 1% نقصان ہو تو رک جائیں

# ===== وقت کی سیٹنگز =====
CHECK_INTERVAL = 300  # ہر 5 منٹ میں چیک کریں (سیکنڈ میں)
CANDLE_INTERVAL = '1h'  # 1 گھنٹے کی موم بتی

# ===== لاگنگ =====
LOG_FILE = 'trading_bot.log'
DEBUG_MODE = True

# ===== ڈیٹا بیس =====
DB_FILE = 'trades.json'

print("✅ کنفیگریشن لوڈ ہو گئی!")
