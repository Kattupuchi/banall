import os

class Config:
    TELEGRAM_TOKEN= "5498903953:AAG5tVpkwRnawWBqvIBq7pZuw4Qqw3xeD8Y"
    TELEGRAM_APP_HASH= "4e984ea35f854762dcde906dce426c2d"
    TELEGRAM_APP_ID= '6435225'
    
    if not TELEGRAM_TOKEN:
        raise ValueError('TELEGRAM BOT TOKEN not set')
    
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
