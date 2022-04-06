from flask import Flask

app = Flask(__name__)

"""
https://code.visualstudio.com/docs/supporting/faq - ссылка

https - протокол
code.visualstudio.com - домен
/docs/supporting/faq - путь (route)
"""

articles = [
	{
		'id': 1,
		'title': 'Article 1',
		'description': 'Description 1',
	},
	{
		'id': 2,
		'title': 'Article 2',
		'description': 'Description 2',
	},
	{
		'id': 3,
		'title': 'Article 3',
		'description': 'Description 3',
	},
]

users = [
	{
		'id': 234,
		'name':'Max',
		'age': 20,
	},
    {
		'id': 235,
		'name':'Artur',
		'age': 23,
	},
	{
		'id': 236,
		'name':'Alex',
		'age': 34,
	},
	{
		'id': 237,
		'name':'Ivan',
		'age': 40,
	},
]

@app.route('/')
def home_page():
	with open('html/index.html', 'r') as f:
		return f.read()


@app.route('/articles')
def get_all_articles():
	response = ''
	for article in articles:
		response += f'<a href="/article/{article["id"]}"><h1>{article["title"]}</h1></a><p>{article["description"]}</p>'
	return response


@app.route('/article/<int:id>')
def get_article(id: int):
	for article in articles:
		if article['id'] == id:
			return f'<h1>{article["title"]}</h1><p>{article["description"]}</p>'
	return '<p style="color:red;">Article not found</p>'


@app.route('/delete-article/<int:id>')
def delete_article(id: int):
	global articles
	index_for_delete = None
	for idx, article in enumerate(articles):
		if article['id'] == id:
			index_for_delete = idx
			break
	if index_for_delete is not None:
		del articles[index_for_delete]
		return 'Успешно удалено'
	else:
		return '<p style="color:red;">Article not found</p>'


@app.route('/<string:first>/<int:second>')
def get_sum(first: str, second: int):
	print(type(first), type(second))
	return first

@app.route('/users')
def get_all_users():
	global ALL_USERS
	response = ''
	for user in users:
		response += f'<a href="/user/{user["id"]}"><h1>{user["name"]},{user["id"]}</h1></a><p>{user["age"]}</p>'
	return response

@app.route('/users/<int:id>')
def get_users_id(id: int):
	for user in users:
		if user['id'] == id:
			return f'<h1>{user["name"]}</h1><p>{user["age"]}</p>'
	return '<p style="color:red;">Users not found</p>'

app.run('localhost', 8000)


