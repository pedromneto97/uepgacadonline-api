from flask import Blueprint, request

import requests
from bs4 import BeautifulSoup

import json

from app.models.grade import Grade
from app.models.perfil import Perfil

from utils.urls import acadonline_urls
from utils.messages import success, error

acadonline = Blueprint("acadonline", __name__, url_prefix="/acadonline")


@acadonline.route("/login", methods=["POST"])
def index():
    if not request.json:
        return error(message="Requisição inválida!")

    data = request.get_json()

    fields = ["login", "password"]

    try:
        user = {field: data[field] for field in fields}

        index = requests.get(acadonline_urls["home"])
        headers_raw = dict((key, value) for key, value in index.cookies.items())
        print(headers_raw)
        headers = {"cookie": f'JSESSIONID={headers_raw["JSESSIONID"]};'}
        print(headers)

        auth = requests.post(acadonline_urls["auth"], user, headers=headers)

        return success(
            message="Login realizado com sucesso", token=headers_raw["JSESSIONID"]
        )
    except:
        return error(message="Falha ao realizar login!")


@acadonline.route("/perfil", methods=["GET"])
def get_perfil():
    jsession = request.headers.get("jsession")
    headers = {"cookie": f"JSESSIONID={jsession};"}

    perfil_page = requests.get(acadonline_urls["perfil_get"], headers=headers)
    perfil_raw = [
        value.find("td", "value").text
        for value in BeautifulSoup(perfil_page.content, features="lxml")("tr", "prop")
    ]

    perfil = Perfil(*[field for field in perfil_raw]).__dict__

    return success(
        message="Perfil capturado com sucesso!", token=jsession, perfil=perfil
    )


@acadonline.route("/perfil", methods=["POST"])
def set_perfil():
    pass


@acadonline.route("/photo", methods=["POST"])
def set_photo():
    pass


# censo


@acadonline.route("/password", methods=["POST"])
def set_password():
    jsession = request.headers.get("jsession")
    headers = {"cookie": f"JSESSIONID={jsession};"}

    return sucess()


@acadonline.route("/documents", methods=["GET"])
def get_documents():
    pass


@acadonline.route("/grades", methods=["GET"])
def get_grades():
    jsession = request.headers.get("jsession")
    headers = {"cookie": f"JSESSIONID={jsession};"}

    grades_page = requests.get(acadonline_urls["grades"], headers=headers)

    grades_raw = [
        [cell.text for cell in row("td")]
        for row in BeautifulSoup(grades_page.content, features="lxml")("tr")
    ][1:]
    grades = Grade(grades_raw).__dict__

    return success(
        message="Notas capturadas com sucesso!",
        token=jsession,
        grades=grades["disciplines"],
    )


@acadonline.route("/activities", methods=["GET"])
def get_additional_activities():
    pass


@acadonline.route("/imposition", methods=["GET"])
def imposition_of_degree():
    pass


@acadonline.route("/internship", methods=["GET"])
def internship():
    pass


@acadonline.route("/downloads", methods=["GET"])
def downloads():
    pass


@acadonline.route("/download", methods=["GET"])
def download():
    pass


@acadonline.route("/contact/prograd", methods=["POST"])
def contact_prograd():
    pass
