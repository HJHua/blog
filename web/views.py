from flask import Blueprint, request, render_template, redirect, url_for,session

from back.models import Article

web_blueprint = Blueprint('web',__name__)

@web_blueprint.route('/index/',methods=['GET'])
def web_index():
    if request.method == 'GET':
        articles = Article.query.limit(14).all()
        return render_template('web/index.html',articles=articles)

@web_blueprint.route('/info/<int:id>/',methods=['GET'])
def web_info(id):
    if request.method == 'GET':
        article = Article.query.get(id)
        return render_template('web/info.html',article=article)

@web_blueprint.route('/about/', methods=['GET'])
def web_about():
    if request.method == 'GET':
        return render_template('web/about.html')

@web_blueprint.route('/list/', methods=['GET'])
def list():
    if request.method == 'GET':
        articles = Article.query.limit(5).all()
        return render_template('web/list.html',articles=articles)