import requests
import json


def call_api(isbn: str) -> dict:
    url = 'https://api.openbd.jp/v1/get?isbn=' + isbn
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError
    return json.loads(response.text)


def convert_api_data(data) -> dict:
    response = dict()
    response['isbn'] = data['summary']['isbn']
    response['title'] = data['summary']['title']
    response['publisher'] = data['summary']['publisher']
    response['author'] = __clean_author(data['summary']['author'])
    response['cover'] = data['summary']['cover']
    response['pubdate'] = __modify_datetime(data['summary']['pubdate'])
    return response


def __modify_datetime(date: str) -> str:
    """
    format a publish date that get by OpenBD API.
    :param date: publish date
    :return: a formated publish date
    """
    return date.replace('c', '')


def __clean_author(author: str) -> str:
    """
    fix an author name that get by OpenBD API.
    :param author: an author name
    :return: a fixed author name
    """
    return author.replace('／著', '')