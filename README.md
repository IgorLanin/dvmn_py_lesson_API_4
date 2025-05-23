# Космический Телеграм

Программа скачивает фотографии, связанные с космосом, с трех источников: 
- [SpaceX](https://github.com/r-spacex/SpaceX-API): фото с запуска.
- [NASA APOD](https://api.nasa.gov/#apod): картинки дня.
- [NASA EPIC](https://api.nasa.gov/#epic): фото планеты Земля.

Скачанные фотографии сохраняются в локальную папку ```images```, которая создается автоматически при запуске модулей, скачивающих фотографии. 

Сохраненные фотографии из папки ```images``` можно публиковать в канале Telegram соответствующей тематики вручную или запустить автопубликацию.

## Как установить

Python3 должен быть уже установлен. Рекомендуется использовать версию [Python 3.8.9](https://www.python.org/downloads/release/python-389/). Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Для запуска программы понадобятся:
- Ключ API с сайта [NASA](https://api.nasa.gov/). Для его получения необходимо заполнить форму регистрации и нажать "Sign Up":

![image](https://github.com/user-attachments/assets/15e49c2b-da87-4291-ac24-1c5da0ff2231)

Ключ API придет на указанную при регистрации электронную почту:

![image](https://github.com/user-attachments/assets/03652398-fad4-4012-bb3a-228b81bb782f)

- Созданный бот в Telegram, API-токен бота.
Если бот пока не создан, понадобится создать бота и получить токен по [инструкции](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html).

- Свой Telegram-канал и созданный бот в качестве администратора канала.
Если Telegram-канала пока нет, создать по [инструкции](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/#01), [добавить](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/#03) созданного бота в Telegram-канал и сделать его администратором.

- id Telegram-канала.
Его можно узнать, перейдя в канал и нажав на название канала сверху. Откроется информация о канале и там же будет ссылка-приглашение вида ```https://t.me/example_name``` или ```t.me/example_name```. Нам нужна часть после ```t.me/```, к которой добавляем ```@``` и получаем id Telegram-канала в виде ```@example_name```.

Полученные данные необходимо сохранить в ```.env```-файл:
- Ключ API с сайта [NASA](https://api.nasa.gov/) положить в переменную ```NASA_API_KEY```.
- Токен Telegram-бота положить в переменную ```TG_TOKEN```.
- id Telegram-канала положить в переменную ```TG_CHAT_ID```.

## Описание работы модулей

Программа состоит из нескольких модулей.

### fetch_spacex_images.py : скачивает фото с запуска SpaceX
Модуль скачивает фото с запуска SpaceX. Можно указать id конкретного запуска. Если id не указан, модуль скачает фото с последнего запуска.

![image](https://github.com/user-attachments/assets/b810753d-4d43-44e0-9c33-d17fafa13ea3)

Важно: если фотографии не скачались, это значит, что во время последнего запуска/конкретного запуска по id, они не были сделаны. В таком случае, укажите id другого запуска и запустите скрипт повторно. Пример: во время запуска id ```5eb87d47ffd86e000604b38a``` фотографии были сделаны и модуль скачает их.

Команда для запуска модуля с id запуска: 
```
python fetch_spacex_images.py 5eb87d47ffd86e000604b38a
```

![image](https://github.com/user-attachments/assets/35db7e56-3716-4951-9e39-b575c7f79c08)

Результат запуска модуля:

![image](https://github.com/user-attachments/assets/6333f752-0814-4165-8ec4-f57f90e572f3)


### fetch_nasa_apod_images.py : скачивает картинки дня с [NASA APOD](https://api.nasa.gov/#apod)
Модуль скачивает 30 случайных картинок дня с [NASA APOD](https://api.nasa.gov/#apod).
Важно: модуль скачает меньше 30 картинок в случае, если, вместо картинки дня, например, ссылка на видео.

Результат запуска модуля:

![image](https://github.com/user-attachments/assets/e0a2adf5-4486-4550-9be8-2042c903b2cf)


### fetch_nasa_epic_images.py : скачивает фото планеты Земля с [NASA EPIC](https://api.nasa.gov/#epic)
Модуль скачивает 5 последних сделанных фото Земли с [NASA EPIC](https://api.nasa.gov/#epic).

Результат запуска модуля:

![image](https://github.com/user-attachments/assets/cc8ace12-ba1b-406f-a10a-80d35a2acd81)


### manual_publish_tg.py : публикует фотографию в Telegram-канал вручную
Модуль публикует одну фотографию из папки images в Telegram-канал. Если не указать название фотографии, модуль выберет случайную картинку из папки images и опубликует ее:

![image](https://github.com/user-attachments/assets/2adb3d66-9136-41ab-b2c9-4ec752278ea7)

Если указать название конкретной картинки, то опубликует выбранную картинку. 

Команда для запуска модуля: 
```
python manual_publish_tg.py nasa_apod_4.jpg
```

![image](https://github.com/user-attachments/assets/e042516d-c97a-41cd-a9d6-df820dd3e40b)

### auto_publish_tg.py : публикует фотографии в Telegram-канал автоматически
Модуль публикует фотографии из папки images автоматически с задержкой. По умолчанию, задержка между публикациями составит 4 часа:

![image](https://github.com/user-attachments/assets/a36dc470-5d06-499a-b0d7-d97b62151d9f)

Можно указать количество часов самостоятельно. Для этого понадобится написать количество часов в виде числа. Команда для запуска: 
```
python auto_publish_tg.py 5
```

![image](https://github.com/user-attachments/assets/86018891-54ba-4127-aee7-06d76dae2240)

### get_img_extention.py : определение формата файла
Вспомогательный модуль, который получает формат скачиваемой картинки для модуля ```fetch_nasa_apod_images.py```.
Это необходимо для правильного сохранения скачиваемых картинок, потому что ```fetch_nasa_apod_images.py``` может скачивать картинки в разных форматах.

### download_images.py : скачивает фотографии и сохраняет их в папку
Вспомогательный модуль, который скачивает фотографии и сохраняет их в папку ```images```. Нужен для работы модулей ```fetch_nasa_apod_images.py```, ```fetch_nasa_epic_images.py```, ```fetch_spacex_images.py```.

### tg_send_image.py : отправляет фото в Telegram-канал
Вспомогательный модуль, который отправляет фото в Telegram-канал. Нужен для работы модулей ```auto_publish_tg.py```, ```manual_publish_tg.py```.

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
