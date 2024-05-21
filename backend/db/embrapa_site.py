import requests
from lxml import html

def get_field_1(url):
    page = requests.get(url)
    if page.status_code != 200:
        return
    data = html.fromstring(page.text)
    return data.xpath("//table[4]/tr/td[2]/div/div/table/tbody/tr/td[1]/text()")

def get_field_2(url):
    page = requests.get(url)
    if page.status_code != 200:
        return
    data = html.fromstring(page.text)
    return data.xpath("//table[4]/tr/td[2]/div/div/table/tbody/tr/td[2]/text()")

def get_field_3(url):
    page = requests.get(url)
    if page.status_code != 200:
        return
    data = html.fromstring(page.text)
    return data.xpath("//table[4]/tr/td[2]/div/div/table/tbody/tr/td[3]/text()")


