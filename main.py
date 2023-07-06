def main():
    import requests
    from bs4 import BeautifulSoup as bs

    user_choose = input('Что ищем?'
                        '\n')

    url = ('https://www.avito.ru/krasnodarskiy_kray?q=' + user_choose)
    r = requests.get(url)
    soap = bs(r.text, 'html.parser')

    laptops = soap.find_all(class_='iva-item-title-py3i_')

    for laptop in laptops:
        name = laptop.text
        link = laptop.find('a')['href']
        print(f'{name} | https://www.avito.ru{link}')

if __name__ == '__main__':
    main()