from flask import Blueprint, jsonify, request

import requests
from bs4 import BeautifulSoup

import json

from utils.urls import acadonline_urls

acadonline = Blueprint("acadonline", __name__, url_prefix="/acadonline")


@acadonline.route("/login", methods=["POST"])
def index():
    if not request.json:
        return jsonify({"status": False, "message": "Requisição inválida!"})

    data = request.get_json()

    fields = ["login", "password"]

    # try:
    user = {field: data[field] for field in fields}

    index = requests.get(acadonline_urls["home"])
    headers_raw = dict((key, value) for key, value in index.cookies.items())
    print(headers_raw)
    headers = {"cookie": f'JSESSIONID={headers_raw["JSESSIONID"]};'}
    print(headers)

    auth = requests.post(acadonline_urls["auth"], headers=headers)

    return jsonify(
        {
            "status": True,
            "message": "Login realizado com sucesso!",
            "token": headers_raw["JSESSIONID"],
        }
    )

    # except:
    #    return jsonify({"status": False, "message": "Falha ao realizar login!"})
    # cookie = {'cookie': f'JSESSIONID={requests.utils.dict_from_cookiejar(session.cookies)["JSESSIONID"]}; __utma=241181661.1990841241.1518980587.1520085361.1520277780.4; __utmz=241181661.1518980587.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'}
    # auth = session.request("POST", url['auth'], user, headers=self.cookie)
