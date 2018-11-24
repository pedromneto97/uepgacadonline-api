from flask import jsonify


def success(**kwargs):
    return jsonify({"status": True, **kwargs})


def error(**kwargs):
    return jsonify({"status": False, **kwargs})


def conditional_response(condition, success_response, error_response):
    return success_response if condition else error_response
