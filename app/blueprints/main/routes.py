from .import bp as main #this makes it easier to know what's going on

from app.models import Item
from flask import render_template, request, flash, redirect, url_for
import requests
from flask_login import  login_required, current_user

@main.route('/', methods=['GET'])
@login_required
def index():
    return render_template('index.html.j2')

@main.route('/adventure', methods=['GET'])
@login_required
def adventure():
    return render_template('adventure.html.j2')