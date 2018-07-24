from flask import (Flask,
                   render_template,
                   redirect,
                   url_for,
                   request
                   )
from models.blog import Blog
app = Flask('app')


@app.route('/')
def index():
    blogs = Blog.list()
    return render_template('index.html', blogs=blogs)


@app.route('/add', methods=['POST', 'GET'])
def add():
    data = dict(request.form.items())
    if data.get('title', None):
        Blog.add(
            title=data.get('title'),
            body=data.get('body')
        )
        return redirect(url_for('index'))
    return render_template('add_blog.html')

app.run(debug=True, host='0.0.0.0', port=8080)
