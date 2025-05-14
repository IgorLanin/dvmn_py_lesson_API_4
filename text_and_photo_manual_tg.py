import telegram
from dotenv import load_dotenv
import os


def main():
    load_dotenv()

    tg_bot_token = os.getenv('TG_TOKEN')
    bot = telegram.Bot(token=tg_bot_token)

    chat_id = os.getenv('CHAT_ID')
    bot.send_message(chat_id=chat_id, text='Hi, members!')
    bot.send_document(chat_id=chat_id, document=open('images/nasa_apod_7.jpg', 'rb'))


if __name__ == '__main__':
    main()
