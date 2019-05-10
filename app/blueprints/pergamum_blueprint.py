from flask import Blueprint, jsonify, request

import requests
from bs4 import BeautifulSoup

from app import endpoints
from utils.urls import pergamum_urls
from utils.response import success, error

from app.repositories import pergamum_repository

pergamum_blueprint = Blueprint("pergamum", __name__, url_prefix="/pergamum")


@pergamum_blueprint.route("/login", methods=["POST"])
def login():
    login = request.form.get('login')
    password = request.form.get('password')

    token = pergamum_repository.authenticate(login, password)

    return success(message="Login realizado com sucesso", token=token)


@pergamum_blueprint.route("/home", methods=["GET"])
def home():
    phpsessid = request.headers.get("phpsessid")
    headers = {"cookie": f"PHPSESSID={phpsessid};"}

    home_page = requests.get(pergamum_urls["home"], headers=headers)

    return success(message="Meu pergamum capturado com sucesso!", token=phpsessid)


@pergamum_blueprint.route("/search", methods=["GET"])
def search():
    phpsessid = request.headers.get("phpsessid")
    headers = {"cookie": f"PHPSESSID={phpsessid};"}

    params = {
        "rs": "ajax_resultados",
        "rsargs[]": ["20", "3", "L", "carl", "palavra", "L", "obra", "5ba7c0ba402ab"],
    }

    search_page = requests.get(pergamum_urls["search"], params=params, headers=headers)

    books_raw = BeautifulSoup(search_page.content, features="lxml")("table")

    return success(message="Livros retornados com sucesso!", token=phpsessid)


@pergamum_blueprint.route("/books", methods=["GET"])
def books():
    token = request.headers.get("phpsessid")

    # loans = pergamum_repository.books(token)
    loans = pergamum_repository.books_mock()

    return success(
        message="Livros retornados com sucesso", token=token, loans=loans
    )


@pergamum_blueprint.route("/book", methods=["GET"])
def book():
    book = request.args.get('collection')

    book_page = requests.get(
        endpoints.pergamum.collection.format(book=book)
    )

    return success(
        message="Livro retornado com sucesso", book=str(book_page.content)
    )


@pergamum_blueprint.route("/renew", methods=["POST"])
def renew():
    book = request.form.get('book')
    token = request.headers.get("phpsessid")

    pergamum_repository.renew(token, book)

    return success(
        message="Livro renovado com sucesso", token=token
    )
