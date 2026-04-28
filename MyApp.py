from flask import Flask, render_template as RenderTemplate      # Import the Flask class from the flask module
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt

allposts= [
    {
        'title': 'Post 1',
        'content': 'This is the content of post 1.',
        'author': 'Author 1'
    },
    {
        'title': 'Post 2',
        'content': 'This is the content of post 2.'
    },
    {
        'title': 'Post 3',
        'content': 'This is the content of post 3.'
    },
    {
        'title': 'Post 4',
        'content': 'This is the content of post 4.',
        'author': 'Author 4'
    },
    {
        'title': 'Post 5',
        'content': 'This is the content of post 5.'
    }
]

app = Flask(__name__)           # Create an instance of the Flask class, passing the name of the module as an argument
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(130), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=dt.now() )
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(30), nullable=False, default='N/A')

    def __repr__(self):
        return 'Post ID: ' + str(self.id) 

@app.route('/dbcreate')
def create_db():
    db.create_all()
    return 'Database and tables created!'

@app.route('/dbcheck')
def get_posts():    
    posts = Post.query.all()
    npost = len(posts)
    return str(npost) + ' posts found in the database!'

@app.route('/dbload')
def add_post(): 
    post1 = Post(title='Post 1', content='This is the content of post 1.', author='Author 1')
    post2 = Post(title='Post 2', content='This is the content of post 2.')
    post3 = Post(title='Post 3', content='This is the content of post 3.')
    post4 = Post(title='Post 4', content='This is the content of post 4.', author='Author 4')
    post5 = Post(title='Post 5', content='This is the content of post 5.')
    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    db.session.add(post4)
    db.session.add(post5)
    db.session.commit()

    return 'Posts added to the database! '

@app.route('/allposts')
def posts():
    return RenderTemplate('allposts.html', posts=allposts)


@app.route('/')                 # Define a route for the root URL ("/") and associate it with the hello_world function

def index():              # Define the function that will be called when the root URL is accessed
    return RenderTemplate('index.html')      # Return the rendered HTML template as the response to the request


if __name__ == '__main__':      # Check if the script is being run directly (as the main program)
    app.run(debug=True)                   # Start the Flask development server, which will listen for incoming requests and handle them using the defined routes and functions    
