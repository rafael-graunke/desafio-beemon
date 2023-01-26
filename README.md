# Desafio beeMôn

Projeto desenvolvido para o desafio da beeMôn.

## Pré-Requisitos

- Python >3.9

## Instalação

### Sem Docker

Para executar o projeto basta clonar esse repositório e instalar as dependências do mesmo:

```
git clone https://github.com/rafael-graunke/desafio-beemon
cd desafio-beemon
pip install -r requirements.txt
```

Talvez seja necessário instalar a biblioteca do BeaultifulSoup4 para Python através do gerenciador de pacotes do seu sistema operacional. Por exemplo:

- Ubuntu

  ```
  sudo apt-get install -y python3-bs4
  ```

- Arch

  ```
  sudo pacman -S python-beautifulsoup4
  ```

Após feita a instalação das dependências, basta executar o arquivo main.py:

```
python main.py
```

### Usando Docker

Para executar o projeto utilizando Docker, basta executar o seguinte comando:

```
docker-compose up -d
```

## Saída

O programa gera duas saídas:

- **stdout** : loga as informações da execução do script, incluindo data e hora. Caso o projeto esteja sendo executado via Docker, basca utilizar `docker logs <container>` para visualizar o log de execução.

- **data/output.csv** : contém a saída dos dados extraídos no formato CSV.
