from flask import Blueprint, jsonify, request

import requests
from bs4 import BeautifulSoup

pergamum = Blueprint("pergamum", __name__, url_prefix="/pergamum")

@pergamum.route("/login", methods=["POST"])
