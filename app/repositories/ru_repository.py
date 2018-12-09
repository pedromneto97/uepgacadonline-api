from app.services import ru_service


def weekly_menu(campus, shift, next):
    data = {
        "campus": campus,
        "shift": shift,
        "next": next
    }

    return ru_service.weekly_menu(data)


def weekly_menu_mock():
    return [
        {
            "date": "Mon, 26 Nov 2018 00:00:00 GMT",
            "day": "Segunda-feira",
            "food": [
                "Arroz",
                "Feijão",
                "Pepino",
                "Lasanha de frango",
                "Batata palha"
            ]
        },
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
