# Utilizando Docker Para Um Projeto de biblioteca


Utilizei os comandos principais do docker e do docker-compose


```
docker-compose up --build

```

Ele vai gerar um servidor completo com todas as configurações do projeto já inclusas, criando particurlamente um container para o postgres e um container para o app

 _Caso precise iniciar o servidor novamente, utilize esse comando:_

 ```
 docker-compose up
 ```

# Populando banco de dados

Utilize esse comando para popular todas as tabelas

```
docker-compose run biblioteca python manage.py populate_db
```


Esse projeto é apenas um CRUD basico para inserir livros, de acordo com as rotas

# Partes do Projeto

- dotenv_files: É uma pasta onde tem os arquivos para inserir variaveis de ambiente, caso não tenha nada, ele continuará sendo utilizando, mas sugiro que povoe ele

```
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

```

O comando listado acima, irá gerar uma secret key automatica para o projeto


Exemplo de ENV para criar, antes de tudo, dentro da pasta crie um arquivo chamado: .env
Dentro dele terá algo como nesse exemplo:

```
SECRET_KEY="CHANGE-ME"

# 0 False, 1 True
DEBUG="1"

# Comma Separated values
ALLOWED_HOSTS="127.0.0.1, localhost"

DB_ENGINE="django.db.backends.postgresql"
POSTGRES_DB="CHANGE-ME"
POSTGRES_USER="CHANGE-ME"
POSTGRES_PASSWORD="CHANGE-ME"
POSTGRES_HOST="localhost"
POSTGRES_PORT="5455"

```

A porta do banco de dados foi alterada, para não gerar conflitos.


* biblioteca: Esse é o app onde tem todas as partes da api, rotas, entre outros

* Livros: Esse é o app onde tem os models, schemas e views



# Testes

Para testar as rotas, ele fornecerar o ip de: 0.0.0.0:8080, para fazer os testes das rotas, basta acessar:

* 0.0.0.0:8080/docs

Gerado pelo django ninja um swagger que pode testar todas as rotas.