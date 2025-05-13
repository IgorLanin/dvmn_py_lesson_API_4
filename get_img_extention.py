from urllib.parse import unquote, urlsplit
import os


def get_img_extention(link):
    parsed_link = urlsplit(link)

    unquoted_path = unquote(parsed_link[2])

    img_name = os.path.split(unquoted_path)[1]

    img_extention = os.path.splitext(img_name)[1]

    return img_extention
