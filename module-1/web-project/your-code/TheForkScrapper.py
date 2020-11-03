import time
import gzip
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


# Parece que el %2C entre lat y long corresponden a la coma que separa ambos valores

# https://www.thefork.com.co/search/?coordinates=4.6436142%2C-74.0748072
# https://www.thefork.com.co/search/?coordinates=4.6436142%2C-74.0748072&p=2


# La idea es extraer el nombre, precio promedio y puntaje promedio


class TheForkExtractor:
    PLACE_SEARCH_BASE_URL = "https://www.thefork.com.co/search/?coordinates="
    NEXT_PAGE_TEXT_END = "&p="

    @staticmethod
    def get_places_list(lat, long, pag=1, iterate=True):
        lat = str(lat)
        long = str(long)
        url = f"{TheForkExtractor.PLACE_SEARCH_BASE_URL}{lat}%2C{long}"
        if pag > 1:
            url += TheForkExtractor.NEXT_PAGE_TEXT_END + str(pag)
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Dnt": "1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Chrome/83.0.4103.97",
        }
        request = Request(url, headers=headers)
        response = urlopen(request)
        pagedata = gzip.decompress(response.read())
        sopa = BeautifulSoup(pagedata, 'html.parser')
        # print(sopa)

        restaurant_list = sopa.find_all('div', {"data-tracking-region": "Restaurant list"})
        if len(restaurant_list) == 0:
            return None

        elementos = []
        for elemento in restaurant_list[0].find_all('div', {'class': 'content css-uotqam e6vs4hd0'}):
            nombre = elemento.find('a', {"target": "_blank"}).text.lower()
            try:
                tipo = elemento.find('p', {"data-testid": "tags-layout"}).text
            except:
                tipo = ""
            try:
                promedio = (elemento.find('p', {"class": "css-yodg87 ejesmtr0"}).find_all('span')[1]).text
            except:
                promedio = ""
            try:
                puntuacion = (elemento.find('span', {"class":"css-17f8ytt e1l48fgb0"}).find_all('span')[0]).text.replace(",",".")
                puntuacion /= 10
            except:
                puntuacion = ""

            #datos = elemento.text.replace("\n", "").split("         ")
            #elementos.append(datos)
            elementos.append([nombre, tipo, promedio, puntuacion])
        print(f"TheFork: Pagina {pag} estraida")


        if iterate:
            while True:
                time.sleep(3)
                pag += 1
                sub_elementos = TheForkExtractor.get_places_list(lat, long, pag, False)
                if sub_elementos is None:
                    break
                else:
                    elementos += sub_elementos

        return elementos
