# Crawler Imoveis Campinas

Este é um programa em Python que utiliza a biblioteca Scrapy para realizar a coleta de dados de imóveis na região de Campinas.
Os dados coletados são armazenados em um banco de dados MongoDB, facilitando uma posterior análise e processamento.

## Dependencias:

Certifique-se de ter o Python e o MongoDB instalados em seu sistema antes de executar o programa.

<p>Python 3.x</p>
<p>MongoDB</p>

Além disso, você precisará instalar algumas bibliotecas Python. <br /> Você pode fazer isso executando o seguinte comando:

```
pip install scrapy
```

```
pip install pymongo
```

### Configurar o MongoDB:

Certifique-se de que o MongoDB esteja em execução no seu sistema ou utilize a versão MongoDB Atlas. Se necessário, ajuste as configurações de conexão no arquivo `settings.py`.

```
MONGODB_URI = "URL do seu banco de dados MONGODB ATLAS"
```

## Para executar o programa:

```
python3 myspider.py
```
