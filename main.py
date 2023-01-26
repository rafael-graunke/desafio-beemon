import requests
import csv
import logging
import pandas as pd
from bs4 import BeautifulSoup
from database import db

# Executa configuracao base do 'logging'
def config_log():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

# Loop principal de execução
def main():
    config_log()

    base_url = "http://quotes.toscrape.com"
    current_page = "/page/1"
    quotes = []

    logging.info("Iniciando busca")

    while current_page != None:
        logging.info(f"Buscando página {current_page}")
        body = requests.get(f"{base_url}{current_page}").text
        logging.info(f"Página {current_page} retornada com sucesso")

        soup = BeautifulSoup(body, 'lxml')

        logging.info(f"Buscando frases e autores")
        raw_quotes = get_quotes(soup)
        logging.info(f"Frases recuperadas: {len(raw_quotes)}")

        quotes += parse_quotes(raw_quotes)
        current_page = next_page(soup)

    logging.info("Busca finalizada")
    logging.info(f"Total de frases: {len(quotes)}")

    logging.info("Convertendo saída para CSV")
    df = quotes_to_df(quotes)
    df_to_csv(df, "./data/output.csv")
    logging.info("CSV com dados salvo")

    logging.info("Salvando frases no banco de dados")
    quotes_to_sqlite(quotes)
    logging.info("Frases salvas com sucesso")

# Busca frases a partir do HTML
def get_quotes(soup):
    return soup.find_all("div", {"class": "quote"})

# Converte as tags do soup para o formato desejado em lista
def parse_quotes(raw_quotes):
    parsed_quotes = []

    for quote in raw_quotes:        
        text = quote.find("span", {"class": "text"}).get_text()
        text = text.strip('\u201c')
        text = text.strip('\u201d')
        author = quote.find("small", {"class": "author"}).get_text()
        parsed_quotes.append([text, author])

    return parsed_quotes

# Converte a lista de frases em um dataframe Pandas
def quotes_to_df(quotes):
    return pd.DataFrame(quotes, columns=["text", "author"])

# Busca o link da praxima pagina
def next_page(soup):
    next_button = soup.find("li", {"class": "next"})
    return next_button.a["href"] if next_button != None else None

# Salva um dataframe como CSV
def df_to_csv(df, path):
    with open(path, "w") as file:
        df.to_csv(file)

# Executa query adicionando as frases e autores no banco SQLite
def quotes_to_sqlite(quotes):
    for quote in quotes:
        db.add_quote(text=quote[0], author_name=quote[1])

if __name__ == "__main__":
    main()