from flask import (Flask,
                   render_template,
                   redirect,
                   url_for
                   )
import models.blog
from models.blog import Blog
app = Flask('app')


@app.route('/')
def index():
    models.blog.initialize()
    blogs = Blog.select()
    return render_template('index.html', blogs=blogs)


app.run(debug=True, host='0.0.0.0', port=8080)
