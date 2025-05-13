import telegram
from dotenv import load_dotenv
import os


def main():
    load_dotenv()

    tg_bot_token = os.getenv('TG_TOKEN')
    bot = telegram.Bot(token=tg_bot_token)

    chat_id = os.getenv('CHAT_ID')
    message_id = bot.send_message(chat_id=chat_id, text='Hi, members!')


if __name__ == '__main__':
    main()
