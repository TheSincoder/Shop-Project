from flask import Blueprint

bp = Blueprint('api',__name__,url_prefix='/api')
# now have to go around and change url_for's

from .import routes 

