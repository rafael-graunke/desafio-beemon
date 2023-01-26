import requests
import csv
import logging
import pandas as pd
from bs4 import BeautifulSoup

def main():
    logging.basicConfig(filename="log.txt", level=logging.INFO)

    base_url = "http://quotes.toscrape.com"
    current_page = "/page/1"
    quotes = []

    logging.info("Iniciando busca")
    while current_page != None:
        logging.info(f"Buscando página {current_page}")
        body = requests.get(f"{base_url}{current_page}").text
        soup = BeautifulSoup(body, 'lxml')
        logging.info(f"Buscando frases")
        raw_quotes = get_quotes(soup)
        logging.info(f"{len(raw_quotes)} frases recuperadas")
        quotes += parse_quotes(raw_quotes)
        current_page = next_page(soup)

    df = quotes_to_df(quotes)
    df_to_csv(df, "output.csv")
    logging.info("Busca finalizada")


def get_quotes(soup):
    return soup.find_all("div", {"class": "quote"})

def parse_quotes(raw_quotes):
    parsed_quotes = []

    for quote in raw_quotes:        
        text = quote.find("span", {"class": "text"}).get_text()
        author = quote.find("small", {"class": "author"}).get_text()
        parsed_quotes.append([text, author])

    return parsed_quotes

def quotes_to_df(quotes):
    return pd.DataFrame(quotes, columns=["text", "author"])

def next_page(soup):
    next_button = soup.find("li", {"class": "next"})
    return next_button.a["href"] if next_button != None else None

def df_to_csv(df, path):
    with open(path, "w") as file:
        df.to_csv(file)

main()