import requests
from bs4 import BeautifulSoup

def scrape_zonaprop(tipo_unidad, localidad, metros_cuadrados):
    url = f'https://www.zonaprop.com.ar/{tipo_unidad}-en-{localidad}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 403:
        raise Exception(f"Error durante el scraping: {response.status_code}")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    propiedades = []
    for prop in soup.find_all('div', class_='property-card'):
        try:
            precio = int(prop.find('span', class_='price').text.strip().replace('$', '').replace('.', ''))
            detalles = prop.find('div', class_='details').text.strip()
            if 'm²' in detalles:
                if int(detalles.split('m²')[0].strip()) >= metros_cuadrados:
                    propiedades.append({'precio': precio})
        except Exception as e:
            continue
    
    return propiedades
