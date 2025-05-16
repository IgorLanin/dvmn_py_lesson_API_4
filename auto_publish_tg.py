import telegram
import os
import argparse
import random
from dotenv import load_dotenv
from time import sleep
from tg_send_image import send_image


def create_parser():
    parser = argparse.ArgumentParser(
            description='''Автоматически публикует фотографии в Telegram-канал.
            Принимает необязательный аргумент - число часов между автопубликациями.
            По умолчанию, период между автопубликациями - 4 часа.''',
            prog='Автоматическая публикация фотографий в Telegram-канал.')

    parser.add_argument('hours', help='Количество часов между автопубликациями.', nargs='?', default=4)

    return parser


def main():
    load_dotenv()

    tg_bot_token = os.getenv('TG_TOKEN')
    bot = telegram.Bot(token=tg_bot_token)
    tg_chat_id = os.getenv('TG_CHAT_ID')

    parser = create_parser()
    postponement = parser.parse_args()

    photos_from_dir = os.listdir(os.path.join('images'))

    secs_delay = (int(postponement.hours) * 60 * 60)

    while True:
        for photo in photos_from_dir:
            img_path = f'images/{photo}'
            send_image(bot, img_path, tg_chat_id)
            sleep(secs_delay)

        random.shuffle(photos_from_dir)


if __name__ == '__main__':
    main()
