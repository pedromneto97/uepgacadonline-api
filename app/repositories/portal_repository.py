from app.services import portal_service


def news_item(date):
    return portal_service.news_item(date)

def news_item_mock():
    return {
        "date": "Fri, 10 Oct 2014 00:00:00 GMT",
        "news": [
            {
                "cod": "6714",
                "time": "18h21",
                "title": "‘Os Saltimbancos’ terá encenação no Parque Ambiental domingo"
            },
            {
                "cod": "6713",
                "time": "17h26",
                "title": "UEPG regulamenta prestação de serviços em tecnologia e inovação"
            },
            {
                "cod": "6712",
                "time": "17h09",
                "title": "JOIA 2014 inicia neste final de semana com 1,5 mil atletas"
            },
            {
                "cod": "6710",
                "time": "13h32",
                "title": "UEPG participa de Workshop sobre Tecnologia de Redes"
            },
            {
                "cod": "6709",
                "time": "11h57",
                "title": "Mácula exibe Flor da Neve e o Leque Secreto"
            },
            {
                "cod": "6708",
                "time": "11h42",
                "title": "Semana de Geografia da UEPG inicia programação na segunda"
            },
            {
                "cod": "6707",
                "time": "10h22",
                "title": "CNPq abre inscrições para três concursos"
            },
            {
                "cod": "6706",
                "time": "09h52",
                "title": "Professor da UEPG lança livro com o tema ‘Física do Cotidiano’"
            },
            {
                "cod": "6704",
                "time": "08h55",
                "title": "PIBIC Júnior recebe propostas de orientadores até 31 de outubro"
            },
            {
                "cod": "6703",
                "time": "07h52",
                "title": "Presidente da Fenaj defende regulamentação da mídia"
            }
        ]
    }


def news(cod):
    return portal_service.news(cod)
