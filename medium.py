from bs4 import BeautifulSoup
import requests
import pandas as pd

def ama(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1"
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = []

    page = soup.find_all('div', class_='sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28')
    for laptops in page:
        anchor = laptops.find('a')
        link = 'https://www.amazon.in' + anchor.get('href')
        s = requests.get(link, headers=headers)
        porridge = BeautifulSoup(s.text, 'html.parser')

        prod_name = porridge.find(id='productTitle').text.strip()

        main_table = porridge.find('div', class_='column col1').find('table')

        try:
            prod_price = porridge.find(id='priceblock_ourprice').text
        except:
            prod_price= 'N/A'
        try:
            prod_mdr = main_table.find('td', text='Maximum Display Resolution').find_next('td').text if True else main_table.find('td', text='Resolution').find_next('td').text
        except:
            prod_mdr = 'N/A'

        try:
            prod_proc = main_table.find('td', text='Processor Type').find_next('td').text
        except:
            prod_proc = 'N/A'

        try:
            prod_DD = main_table.find('td', text='Memory Technology').find_next('td').text
        except:
            prod_DD = 'N/A'

        product = {
            'Name': prod_name,
            'Price': prod_price,
            'Screen Size': prod_mdr,
            'Processor Type': prod_proc,
            'Memory Technology': prod_DD
        }
        table.append(product)
    return table


data = ama('https://www.amazon.in/s?i=computers&bbn=1375424031&rh=n%3A976392031%2Cn%3A976393031%2Cn%3A1375424031%2Cp_89%3AHP%2Cp_n_feature_thirteen_browse-bin%3A12598162031%7C12598163031%7C16757430031%2Cp_n_operating_system_browse-bin%3A7350855031%2Cp_n_pattern_browse-bin%3A8609969031%2Cp_n_feature_browse-bin%3A1485945031%2Cp_n_feature_fourteen_browse-bin%3A2917527031&dc&fst=as%3Aoff&qid=1589031568&rnid=2917524031&ref=sr_nr_p_n_feature_fourteen_browse-bin_2')

#'https://www.amazon.in/s?bbn=4364642031&rh=n%3A976392031%2Cn%3A%211499764031%2Cn%3A%211499766031%2Cn%3A4364642031%2Cp_89%3ADell&dc&fst=as%3Aoff&qid=1588687953&rnid=3837712031&ref=lp_4364642031_nr_p_89_0')

df = pd.DataFrame(data)
df.to_csv('AmazonDell3.csv')
df.to_excel('AmazonHp1.xlsx')
print("Saved!")