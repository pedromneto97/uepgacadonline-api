from flask import Blueprint, request

import requests
from bs4 import BeautifulSoup
import re

import json

from app.models.grade import Grade
from app.models.perfil import Perfil
from app.models.activity import Activity

from utils.urls import acadonline_urls
from utils.messages import success, error

acadonline = Blueprint("acadonline", __name__, url_prefix="/acadonline")


@acadonline.route("/login", methods=["POST"])
def login():
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
        value.find("td", "value")
        .text.replace("\r", "")
        .replace("\n", "")
        .replace("\t", "")
        .replace("/\s\s+/", "")
        .strip()
        for value in BeautifulSoup(perfil_page.content, features="lxml")("tr", "prop")
    ]

    perfil = Perfil(*[field for field in perfil_raw]).__dict__

    return success(
        message="Perfil capturado com sucesso!", token=jsession, perfil=perfil
    )


@acadonline.route("/perfil", methods=["POST"])
def set_perfil():
    jsession = request.headers.get("jsession")
    headers = {"cookie": f"JSESSIONID={jsession};"}

    if not request.json:
        return error(message="Requisição inválida!")

    data = request.get_json()

    fields = [
        "bairro",
        "cep",
        "cidade",
        "complemento",
        "ddd",
        "email",
        "id",
        "logradouro",
        "numeroTelefone",
        "numero_residencia",
        "uf",
        "url_lattes",
    ]

    # try:
    perfil = {field: data[field] for field in fields}
    perfil["id"] = "72403"
    perfil["_action_update"] = "Alterar"

    update_perfil = requests.post(
        acadonline_urls["perfil_set"], perfil, headers=headers
    )

    return success(message="Perfil atualizado com sucesso", token=jsession)
    # except:
    # return error(message="Falha ao realizar atualização!")


@acadonline.route("/photo", methods=["POST"])
def set_photo():
    pass


# censo


@acadonline.route("/password", methods=["POST"])
def set_password():
    jsession = request.headers.get("jsession")
    headers = {"cookie": f"JSESSIONID={jsession};"}

    if not request.json:
        return error(message="Requisição inválida!")

    data = request.get_json()

    fields = ["senha1", "senha2"]

    password = {field: data[field] for field in fields}
    password["id"] = "72403"
    password["_action_update"] = "Alterar"
    password["_method"] = "PUT"

    update_perfil = requests.post(
        acadonline_urls["password"], password, headers=headers
    )

    return success(message="Perfil atualizado com sucesso", token=jsession)


@acadonline.route("/rememberpassword", methods=["POST"])
def remember_password():
    jsession = request.headers.get("jsession")
    headers = {"cookie": f"JSESSIONID={jsession};"}

    params = {"_action_passo2": "OK", "registroAcademico": "14147326"}

    request_remember_page = request.post(
        acadonline_urls["remember_password"], params, headers=headers
    )

    # return success(message="Senha enviada por email com sucesso", token=jsession)
    return error(message="Serviço ainda não finalizado")


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
    jsession = request.headers.get("jsession")
    headers = {"cookie": f"JSESSIONID={jsession};"}

    activities_page = requests.get(acadonline_urls["activities"], headers=headers)

    activities_raw = [
        [cell.text for cell in row("td")]
        for row in BeautifulSoup(activities_page.content, features="lxml")("tr", "even")
    ]

    activities = [
        Activity(*[field for field in activity_raw]).__dict__
        for activity_raw in activities_raw
    ]

    return success(
        message="Atividades capturadas com sucesso!",
        token=jsession,
        activities=activities,
    )


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
