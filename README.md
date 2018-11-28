## uepgacadonline

Interface desenvolvida para facilitar acesso aos serviços da Universidade Estadual de Ponta Grossa. Projeto desenvolvido durante o projeto mobile sendo feito de maneira independente (ainda não concluído).

As rotas podem ser importadas no postman através do arquivo (acadonline.postman_collection). É possível utilizar o próprio servidor ou o exemplo acessível em: https://uepgacadonline.herokuapp.com

Algumas rotas (o todo pode ser encontrado no arquivo postman):

*@POST /acadonline/login*
```json
{
	"login": "{login}",
	"password": "{password}"
}
```


```json
{
    "message": "Login realizado com sucesso",
    "status": true,
    "token": "43E03EC5562A0C86F5540F5EE2B72CBF"
}
```

O token é retornado no cabeçado da resposta (e temporariamente no body) que deve ser utilizado nas próximas requisições como cabeçalho.

Rotas disponíveis atualmente:

*@POST <b>/acadonline/login</b>*: Login no sistema acadêmico e retorna o x-api-token de acesso, para futuras requisições.

*@GET <b>/acadonline/grades</b>*: Retorna as notas do usuário e permite computar algumas informações extras, como média total, etc...

*@GET <b>/acadonline/perfil</b>*: Retorna o perfil do usuário, nome, cidade, ra, endereço, etc...
 
*@POST <b>/acadonline/perfil</b>*: Requisição para alterar dados de perfil do usuário.

*@POST <b>/acadonline/password</b>*: Requisição para alterar senha do usuário.

*@GET <b>/acadonline/activities</b>*: Retorna as atividades de hora complementar do usuário.

*@GET <b>/pergamum/login</b>*: Login no sistema da biblioteca pergamum e retorna o phpsessid de acesso, para futuras requisições.

*@GET <b>/pergamum/home</b>*: Retorna os dados básicos da tela inicial de determinado usuário.

*@GET <b>/pergamum/search</b>*: Retorna a busca de livros de determinada query.

*@GET <b>/portal/newsitem</b>*: Retorna a lista de notícias estruturadas de determinado ano/mês do portal da uepg.

*@GET <b>/portal/news</b>*: Retorna determinada notícia através do código.

*@GET <b>/ru/menu</b>*: Retorna cardápio semanal do ru de determinado campus.

### Qual intenção dessa api?

A ideia é criar o ambiente de extração de dados para desenvolvimento de aplicações mobile, web, desktop, terminal etc... Já que a universidade não possui uma API e provavelmente nem terá nos próximos anos.

Segue um exemplo:

A rota de cardápio do ru por exemplo, retorna um json formatado da seguinte forma:

```json
{
    "message": "Cardápio retornado com sucesso",
    "status": true,
    "weekly_menu": {
        "daily_menus": [
            {
                "date": "Tue, 27 Nov 2018 00:00:00 GMT",
                "day": "Terça-feira",
                "food": [
                    "Arroz",
                    "Feijão",
                    "Pepino",
                    "Strogonoff de frango",
                    "Batata palha"
                ]
            },
            {
                "date": "Wed, 28 Nov 2018 00:00:00 GMT",
                "day": "Quarta-feira",
                "food": [
                    "Arroz",
                    "Feijão",
                    "Escarola",
                    "Bisteca assada",
                    "Farofa de legumes",
                    "Banana"
                ]
            },
            {
                "date": "Thu, 29 Nov 2018 00:00:00 GMT",
                "day": "Quinta-feira",
                "food": [
                    "Arroz",
                    "Feijão",
                    "Beterraba",
                    "Bife ao molho de tomate",
                    "Polenta",
                    "Gelatina"
                ]
            },
            {
                "date": "Fri, 30 Nov 2018 00:00:00 GMT",
                "day": "Sexta-feira",
                "food": [
                    "Arroz",
                    "Feijão",
                    "repolho com cenoura",
                    "Linguiça Assada",
                    "Macarrão",
                    "Pêssego"
                ]
            }
        ]
    }
}
```

De fácil renderização como uma API tradicional.
