import requests
from bs4 import BeautifulSoup

from app import endpoints
from app.models.perfil import Perfil


def authenticate(data):
    fields = [
        "login",
        "password"
    ]

    user = {field: data[field] for field in fields}

    headers, token = _get_cookies(requests.get(endpoints.acadonline.home))

    requests.post(endpoints.acadonline.auth, user, headers=headers)

    return token


def get_perfil(token):
    perfil_page = requests.get(
        endpoints.acadonline.perfil_get,
        headers=_get_headers(token)
    )

    perfil = _parse_perfil(perfil_page)

    return perfil


def set_perfil(token, data):
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

    perfil = {field: data[field] for field in fields}
    perfil["id"] = "72403"
    perfil["_action_update"] = "Alterar"

    update_perfil = requests.post(
        endpoints.acadonline.perfil_set,
        perfil,
        headers=_get_headers(token)
    )

    return update_perfil


def _parse_perfil(perfil_page):
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

    return perfil


def _get_cookies(response):
    headers_raw = dict((key, value) for key, value in response.cookies.items())
    headers = {"cookie": f'JSESSIONID={headers_raw["JSESSIONID"]};'}
    return headers, headers_raw["JSESSIONID"]


def _get_headers(jsession):
    return {"cookie": f"JSESSIONID={jsession};"}
