import requests


def translate_it(text, from_lang, to_lang, api_key):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param api_key:
    :param name_translate_file:
    :param path_text_file:
    :param from_lang:
    :param to_lang:
    :return:
    """
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    params = {
        'key': api_key,
        'text': text,
        'lang': from_lang.format(to_lang),
    }

    response = requests.get(URL, params=params)
    return response.json()

