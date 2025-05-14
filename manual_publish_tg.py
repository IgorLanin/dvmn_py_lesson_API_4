import telegram
from dotenv import load_dotenv
import os
import argparse
import random


def create_parser():
    parser = argparse.ArgumentParser(
            description='''Публикует фотографию в Telegram-канал.
            Принимает необязательный аргумент - название фотографии из папки images.
            Если название не указано, публикует случайную фотографию из папки images.''',
            prog='Автоматическая публикация фотографий в Telegram-канал.')

    parser.add_argument('img_name', help='Название картинки для публикации.', nargs='?')

    return parser


def main():
    load_dotenv()

    tg_bot_token = os.getenv('TG_TOKEN')
    bot = telegram.Bot(token=tg_bot_token)
    chat_id = os.getenv('CHAT_ID')

    parser = create_parser()
    user_input = parser.parse_args()

    photos_from_dir = os.listdir(os.path.join('images'))

    if not user_input.img_name or user_input.img_name not in photos_from_dir:
        random_img_name = random.choice(photos_from_dir)
        bot.send_document(chat_id=chat_id, document=open(f'images/{random_img_name}', 'rb'))
    else:
        bot.send_document(chat_id=chat_id, document=open(f'images/{user_input.img_name}', 'rb'))


if __name__ == '__main__':
    main()
