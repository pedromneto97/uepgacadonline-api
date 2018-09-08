from flask import jsonify


def success(**kwargs):
    return jsonify({"status": True, **kwargs})


def error(**kwargs):
    return jsonify({"status": False, **kwargs})
