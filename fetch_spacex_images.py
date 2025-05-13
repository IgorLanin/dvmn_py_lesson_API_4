import argparse
import requests
from pathlib import Path


def create_parser():
    parser = argparse.ArgumentParser(
            description='''Скрипт получает фотографии с запуска SpaceX.
            Если передан ID запуска, будут скачаны фотографии с этого запуска.
            Если ID запуска не передан, будут скачаны фотографии с последнего запуска.
            Если скрипт исполнился без ошибок, но фотографий в папке images нет, это значит,
            что в последний запуск/запуск по конкретному ID SpaceX не делали фотографии.
            Попробуйте скачать фотографии по ID другого запуска.''',
            prog='Скачивание фотографий с запуска SpaceX.')

    parser.add_argument('launch_id', help='ID запуска', nargs='?', default='latest')

    return parser


def fetch_spacex_last_launch(url):
    response = requests.get(url)
    response.raise_for_status()

    response_data = response.json()

    links = response_data["links"]["flickr"]["original"]
    spacex_filename = 'images/spacex{}.jpg'

    for link_number, link in enumerate(links, start=1):
        response = requests.get(link)
        response.raise_for_status()

        with open(spacex_filename.format(link_number), 'wb') as file:
            file.write(response.content)


def main():
    Path('images').mkdir(parents=True, exist_ok=True)

    parser = create_parser()
    user_input = parser.parse_args()

    spacex_url = "https://api.spacexdata.com/v5/launches/{}".format(user_input.launch_id)

    fetch_spacex_last_launch(spacex_url)


if __name__ == '__main__':
    main()
