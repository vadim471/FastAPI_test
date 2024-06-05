import requests
from . import schemas
def get_product_from_wb(id:int) -> dict:
    url = f'https://card.wb.ru/cards/v2/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm={id}'

    headers = {
        'Accept' : '*/*',
        'Accept-Language' : 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection' : 'keep-alive',
        'Origin' : 'https://www.wildberries.ru',
        'Referer' : 'https://www.wildberries.ru/catalog/205062863/detail.aspx',
        'Sec-Fetch-Dest' : 'empty',
        'Sec-Fetch-Mode' : 'cors',
        'Sec-Fetch-Site' : 'cross-site',
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'sec-ch-ua' : '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile' : '?0',
        'sec-ch-ua-platform' : '"macOS"',
    }
    response = requests.get(url = url, headers = headers)
    return response.json()

def parse_product(response:dict) -> schemas.Product:

    prod_raw = response['data']['products'][0]

    product = schemas.Product(nm_id=prod_raw['id'], name=prod_raw['name'], brand=prod_raw['brand'],
                              brand_id=prod_raw['brandId'],
                              site_brand_id=prod_raw['siteBrandId'], supplier_id=prod_raw['supplierId'], 
                                rating=prod_raw['rating'], feedbacks=prod_raw['feedbacks'])
    
    for i in range(len(prod_raw['sizes'])):
        if 'price' in prod_raw['sizes'][i]:
            product.price = prod_raw['sizes'][i]['price']['basic']
            product.sale_price = prod_raw['sizes'][i]['price']['total']
    
    for color_raw in prod_raw['colors']:
        color = schemas.Color(id=color_raw['id'], name=color_raw['name'])
        product.colors.append(color)

    return product
