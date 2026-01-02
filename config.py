# bot_tg/config.py
import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass
class Settings:
    BOT_TOKEN: str = os.getenv("TG_BOT_TOKEN", "")


settings = Settings()
