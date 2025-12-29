# API REST
A seguinte API foi desenvolvida como aplicação teste para o meu TCC ***UM ESTUDO COMPARATIVO ENTRE AS APIS PARA APLICAÇÕES WEB:
RESTFUL, GRAPHQL E GRPC***. Dentro do contexto fictício apresentado no trabalho, a API REST atuava como uma aplicação intermediária entre um site de divulgação de oportunidades (cursos, estágios e bolsas acadêmicas) e um servidor de banco de dados, o qual possuia as informações sobre tais oportunidades.

Caso tenha interesse em analisar as outras APIs construídas para o TCC abaixo tem-se o link para seus respectivos repositórios.

1. [API Graphql](https://github.com/samylesousa/apiGraphQL)
2. [API gRPC](https://github.com/samylesousa/apiGRPC)

### Bibliotecas usadas no projeto
* FastAPI
* SQLAlchemy
* Faker
* Python-Dotenv
* psutil 


### Como rodar o projeto
1. Crie uma máquina virtual
> python -m venv env
2. Ative a máquina virtual
> env/Scripts/Activate.ps1
3. Instale as bibliotecas através do arquivo requirements
> pip install requiriments.txt
4. Rode a aplicação
> uvicorn main:app --reload

