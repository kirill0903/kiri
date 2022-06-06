import flask
from flask import request
from datetime import datetime

from core import config
from crud.articles import article_crud

article_api = flask.Blueprint('article_api', __name__)

@article_api.get(config.API_ROUTE_PREFIX + 'articles')
def get_articles():
	return flask.jsonify({
			'code': 0,
			'message': 'OK',
			'data': article_crud.get_all()
		})


@article_api.get(config.API_ROUTE_PREFIX + 'articles/<id>')
def get_article(id):
	return flask.jsonify({
			'code': 0,
			'message': 'OK',
			'data': article_crud.get_one(id)
		})


@article_api.post(config.API_ROUTE_PREFIX + 'articles')
def create_article():
	if 'title' not in request.json or 'content' not in request.json or 'author' not in request.json:
		return flask.jsonify({
				'code': 9,
				'message': 'Title, content, author являются обязательными полями',
				'data': None
			})
	request.json['created_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	return flask.jsonify({
			'code': 0,
			'message': 'OK',
			'data': article_crud.create(request.json)
		})

@article_api.delete(config.API_ROUTE_PREFIX + 'articles/<id>')
def delete_article(id):
	global article
	if len(article) >= id:
		article.pop(id - 1)
		return flask.jsonify({
			'code': 0,
			'message': 'article deleted!'
		})
	return flask.jsonify({
			'code': 3,
			'message': 'article not found!'
		})

@article_api.put(config.API_ROUTE_PREFIX + 'articles/<id>')
def update_article(id):
	try:
		article = Article(id=str(id), title=request.json.get('title'), content=request.json.get('content'), author=request.json.get('author'))
	except ValidationError as e:
		return e.json()
	data = article_crud.update(article.dict(), id)
	if data is None:
		return flask.jsonify({
				'code': 9,
				'message': 'Статья не найдена',
				'data': None
			})
	return flask.jsonify({
			'code': 0,
			'message': 'OK',
			'data': None
		})

@article_api.delete(config.API_ROUTE_PREFIX + 'articles/<id>')
def delete_article(id):
	return flask.jsonify({
			'code': 0,
			'message': 'OK',
			'data': article_crud.delete(id)
		})


