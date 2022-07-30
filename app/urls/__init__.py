
from flask import Blueprint

urls_bp = Blueprint('urls_bp', __name__)

from .views import *