from app.services import pergamum_service


def authenticate(login, password):
    return pergamum_service.authenticate(login, password)


def home():
    return pergamum_service.home()


def search():
    return pergamum_service.search()


def books(token):
    return pergamum_service.books(token)


def books_mock():
    return [
        {
            "address": "https://sistemas.uepg.br/pergamum/biblioteca/index.php?codAcervo=193457",
            "currentRenewalsNumber": 2,
            "fine": "0",
            "limitDate": "Fri, 14 Dec 2018 00:00:00 GMT",
            "maxRenewalNumber": 6,
            "name": "Computação quântica e informação quântica / 2005 - Livros",
            "renew": 127440,
            "title": "NIELSEN, Michael A. <b> Computação quântica e informação quântica. </b>  Porto Alegre: Bookman, 2005. 733 p. ISBN 85-363-0554-1. "
        }
    ]


def renew(token, book):
    return pergamum_service.renew(token, book)
