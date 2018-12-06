from flask import Blueprint, jsonify, request

import requests
from bs4 import BeautifulSoup

from utils.urls import pergamum_urls
from utils.response import success, error

from app.repositories import pergamum_repository

pergamum_blueprint = Blueprint("pergamum", __name__, url_prefix="/pergamum")


@pergamum_blueprint.route("/login", methods=["POST"])
def login():
    login = request.form.get('login')
    password = request.form.get('password')

    token = pergamum_repository.authenticate(login, password)

    return success(
        message="Login realizado com sucesso", token=token
    )


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

    print(books_raw)

    return success(message="Livros retornados com sucesso!", token=phpsessid)
