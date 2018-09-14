from flask import Blueprint, jsonify, request

import requests
from bs4 import BeautifulSoup

from utils.urls import pergamum_urls
from utils.messages import success, error

pergamum = Blueprint("pergamum", __name__, url_prefix="/pergamum")


@pergamum.route("/login", methods=["POST"])
def login():
    user = {"rs": "ajax_valida_acesso_novo", "rsargs": ["", ""]}

    auth = requests.request("POST", pergamum_urls["auth"], data=user)
    headers_raw = dict((key, value) for key, value in auth.cookies.items())
    print(headers_raw)

    return success(
        message="Login realizado com sucesso", token=headers_raw["PHPSESSID"]
    )


@pergamum.route("/home", methods=["GET"])
def home():
    phpsessid = request.headers.get("phpsessid")
    headers = {"cookie": f"PHPSESSID={phpsessid};"}

    home_page = requests.get(pergamum_urls["home"], headers=headers)

    print(home_page.content)

    return success(message="Meu pergamum capturado com sucesso!", token=phpsessid)
