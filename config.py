import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

class Config:
    # Telegram
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if not TELEGRAM_TOKEN:
        raise ValueError("⛔ TELEGRAM_BOT_TOKEN не встановлено у .env файлі")
    
    # Binance
    BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
    BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")
    
    # Шляхи
    BASE_DIR = Path(__file__).resolve().parent.parent
    LOG_DIR = BASE_DIR / "logs"
    MODEL_DIR = BASE_DIR / "ai_models"
    CACHE_DIR = BASE_DIR / "cache"
    
    # Налаштування моделі ШІ
    AI_MODEL_NAME = "crypto_predictor.pth"
    AI_SEQUENCE_LENGTH = 60
    AI_EPOCHS = 100
    AI_HIDDEN_SIZE = 128
    AI_NUM_LAYERS = 3
    AI_TRAIN_SYMBOL = "BTCUSDT"  # Основна пара для навчання
    
    # Налаштування кешу
    CACHE_TTL = 300  # 5 хвилин
    
    # Налаштування логування
    LOG_LEVEL = "INFO"
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

LOG_LEVEL = "DEBUG"

# Створення директорій
for directory in [Config.LOG_DIR, Config.MODEL_DIR, Config.CACHE_DIR]:
    directory.mkdir(parents=True, exist_ok=True)