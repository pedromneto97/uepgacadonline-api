from flask import Blueprint, request

from app.repositories import acadonline_repository

from utils.messages import success, error

acadonline_blueprint = Blueprint("acadonline", __name__, url_prefix="/acadonline")


@acadonline_blueprint.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    token = acadonline_repository.authenticate(data)

    return success(
        message="Login realizado com sucesso", token=token
    )


@acadonline_blueprint.route("/perfil", methods=["GET"])
def get_perfil():
    token = request.headers.get("x-api-token")

    perfil = acadonline_repository.get_perfil(token)

    return success(
        message="Perfil capturado com sucesso!", token=token, perfil=perfil
    )


@acadonline_blueprint.route("/perfil", methods=["POST"])
def set_perfil():
    data = request.get_json()
    token = request.headers.get("x-api-token")

    acadonline_repository.set_perfil(token, data)

    return success(
        message="Perfil atualizado com sucesso", token=token
    )


@acadonline_blueprint.route("/photo", methods=["POST"])
def set_photo():
    pass


@acadonline_blueprint.route("/password", methods=["POST"])
def set_password():
    data = request.get_json()
    token = request.headers.get("x-api-token")

    acadonline_repository.set_password(token, data)

    return success(
        message="Perfil atualizado com sucesso",
        token=token
    )


@acadonline_blueprint.route("/rememberpassword", methods=["POST"])
def remember_password():
    token = request.headers.get("x-api-token")

    acadonline_repository.remember_password(token)

    return error(message="Serviço ainda não finalizado")


@acadonline_blueprint.route("/documents", methods=["GET"])
def get_documents():
    pass


@acadonline_blueprint.route("/grades", methods=["GET"])
def get_grades():
    token = request.headers.get("x-api-token")

    grades = acadonline_repository.get_grades(token)

    return success(
        message="Notas capturadas com sucesso!",
        token=token,
        grades=grades["disciplines"],
    )


@acadonline_blueprint.route("/activities", methods=["GET"])
def get_additional_activities():
    token = request.headers.get("x-api-token")

    activities = acadonline_repository.get_additional_activities(token)

    return success(
        message="Atividades capturadas com sucesso!",
        token=token,
        activities=activities,
    )


@acadonline_blueprint.route("/imposition", methods=["GET"])
def imposition_of_degree():
    pass


@acadonline_blueprint.route("/internship", methods=["GET"])
def internship():
    pass


@acadonline_blueprint.route("/downloads", methods=["GET"])
def downloads():
    pass


@acadonline_blueprint.route("/download", methods=["GET"])
def download():
    pass


@acadonline_blueprint.route("/contact/prograd", methods=["POST"])
def contact_prograd():
    pass
