import logging
import asyncio
import httpx
import torch
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from bot.handlers import setup_handlers
from utils.logger import configure_logging
from config import Config
from utils.cache import cache  # Додано для очищення кешу

# Вимкнути логування HTTP-запитів
httpx_logger = logging.getLogger("httpx")
httpx_logger.setLevel(logging.WARNING)

def main() -> None:
    # Налаштування логування
    configure_logging()
    logger = logging.getLogger(__name__)  # Отримуємо логер для поточного модуля
    logger.info("🚀 Запуск Crypto Analysis Bot")
    logger.info(f"PyTorch version: {torch.__version__}")
    logger.info(f"CUDA available: {torch.cuda.is_available()}")

    if torch.cuda.is_available():
        logger.info(f"🎮 GPU devices: {torch.cuda.device_count()}")
        logger.info(f"🎮 Current device: {torch.cuda.current_device()}")
        logger.info(f"🎮 Device name: {torch.cuda.get_device_name(0)}")
    else:
        logger.warning("⚠️ No GPU available, using CPU")
    
    # Очищення кешу при запуску
    cache.clear()
    logger.info("🧹 Кеш очищено при запуску")
    
    try:
        application = Application.builder().token(Config.TELEGRAM_TOKEN).build()
        
        # Видалено ручну ініціалізацію JobQueue
        setup_handlers(application)
        logger.info("🔄 Бот перейшов у режим очікування повідомлень")
        application.run_polling(
            allowed_updates=Update.ALL_TYPES,
            close_loop=False
        )
    except Exception as e:
        logger.critical(f"⛔ Критична помилка: {e}", exc_info=True)
        raise

if __name__ == "__main__":
    asyncio.run(main())