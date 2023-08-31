# Crawler Imoveis Campinas

Crawler e ETL que armazena as informações de diversas casas a venda em campinas dentro de um arquivo json e manda para um banco de dados MongoDB

## Dependencias:

Certifique-se de ter o Python e o MongoDB instalados em seu sistema antes de executar o programa.

Scrapy
Python 3.x
MongoDB
Além disso, você precisará instalar algumas bibliotecas Python. Você pode fazer isso executando o seguinte comando:

```
pip install scrapy
```

```
pip install pymongo
```

### Configurar o MongoDB:

Certifique-se de que o MongoDB esteja em execução no seu sistema. Se necessário, ajuste as configurações de conexão no arquivo `settings.py`.

```
MONGODB_URI = "URL do seu banco de dados MONGODB ATLAS"
```

## Para executar o programa:

```
python3 myspider.py
```
