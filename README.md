## uepgacadonline

Interface desenvolvida para facilitar acesso aos serviços da Universidade Estadual de Ponta Grossa. Projeto desenvolvido durante o projeto mobile sendo feito de maneira independente (ainda não concluído).

As rotas podem ser importadas no postman através do arquivo (acadonline.postman_collection). É possível utilizar o próprio servidor ou o exemplo acessível em: https://uepgacadonline.herokuapp.com

Algumas rotas (o todo pode ser encontrado no arquivo postman):

*@POST https://uepgacadonline.herokuapp.com/acadonline/login*
\@request body
```json
{
	"login": "{login}",
	"password": "{password}"
}
```

\@response
```json
{
    "message": "Login realizado com sucesso",
    "status": true,
    "token": "43E03EC5562A0C86F5540F5EE2B72CBF"
}
```

O token retornado na resposta deve ser utilizado nas próximas requisições no header.

*@GET https://uepgacadonline.herokuapp.com/acadonline/grades*
\@request header
jsession: {token}

\@response
```json
{
    "grades": [
        {
            "absences": "0",
            "className": "T",
            "cod": "203076",
            "frequency": "100",
            "grade1": "",
            "grade2": "",
            "gradeE": "",
            "mean": "0",
            "name": "Orientação de Trabalho de Conclusão de Curso",
            "status": "R",
            "year": "2018"
        },
        {
            "absences": "0",
            "className": "A",
            "cod": "203069",
            "frequency": "100",
            "grade1": "9",
            "grade2": "8",
            "gradeE": "",
            "mean": "8.5",
            "name": "Empreendedorismo",
            "status": "A",
            "year": "2018-1"
        },
        {
            "absences": "6",
            "className": "A",
            "cod": "203070",
            "frequency": "88",
            "grade1": "10",
            "grade2": "9",
            "gradeE": "",
            "mean": "9.5",
            "name": "Computadores e Sociedade",
            "status": "A",
            "year": "2018-1"
        },
        {
            "absences": "4",
            "className": "A",
            "cod": "203082",
            "frequency": "94",
            "grade1": "8.5",
            "grade2": "8.5",
            "gradeE": "",
            "mean": "8.5",
            "name": "Robótica",
            "status": "A",
            "year": "2018-1"
        },
        {
            "absences": "3",
            "className": "A",
            "cod": "203083",
            "frequency": "95",
            "grade1": "9.1",
            "grade2": "9.1",
            "gradeE": "",
            "mean": "9.1",
            "name": "Modelagem e Simulação",
            "status": "A",
            "year": "2018-1"
        },
        {
            "absences": "12",
            "className": "A",
            "cod": "404055",
            "frequency": "82",
            "grade1": "9.4",
            "grade2": "9.4",
            "gradeE": "",
            "mean": "9.4",
            "name": "Economia",
            "status": "A",
            "year": "2018-1"
        },
        {
            "absences": "0",
            "className": "A",
            "cod": "203127",
            "frequency": "100",
            "grade1": "",
            "grade2": "",
            "gradeE": "",
            "mean": "0",
            "name": "Estágio Supervisionado",
            "status": "R",
            "year": "2018-2"
        }
    ],
    "message": "Notas capturadas com sucesso!",
    "status": true,
    "token": "43E03EC5562A0C86F5540F5EE2B72CBF"
}
```
