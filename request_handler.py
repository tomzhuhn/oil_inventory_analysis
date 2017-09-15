import requests
from bs4 import BeautifulSoup

def eia_website_request_handler():

    eia_site_url = 'https://www.eia.gov/petroleum/supply/weekly/'
    # eia_page_url = "http://ir.eia.gov/wpsr/table1.csv"

    target_req =  requests.get(eia_site_url)

    target_soup = BeautifulSoup(target_req.content,'html.parser')

    # tables = target_soup.find_all('U.S. Petroleum Balance Sheet')

    print target_soup

eia_website_request_handler()