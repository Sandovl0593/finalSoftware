from flask import Flask
from models import *

BD: list[Cuenta] = []
BD.append()

app = Flask(__name__)

from app import models, routes
