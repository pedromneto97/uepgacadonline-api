from flask import Blueprint, jsonify, request

import requests
from bs4 import BeautifulSoup

from utils.urls import pergamum_urls
from utils.messages import success, error

from app.models.book import Book

pergamum_blueprint = Blueprint("pergamum", __name__, url_prefix="/pergamum")


@pergamum_blueprint.route("/login", methods=["POST"])
def login():
    user = {"rs": "ajax_valida_acesso_novo"}

    auth = requests.request("POST", pergamum_urls["auth"], data=user)
    headers_raw = dict((key, value) for key, value in auth.cookies.items())
    print(headers_raw)

    return success(
        message="Login realizado com sucesso", token=headers_raw["PHPSESSID"]
    )


@pergamum_blueprint.route("/home", methods=["GET"])
def home():
    phpsessid = request.headers.get("phpsessid")
    headers = {"cookie": f"PHPSESSID={phpsessid};"}

    home_page = requests.get(pergamum_urls["home"], headers=headers)

    print(home_page.content)

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

    print(books_raw)

    return success(message="Livros retornados com sucesso!", token=phpsessid)
