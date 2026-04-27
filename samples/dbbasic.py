# Install flask_sqlalchemy using pip 
# pip  install flask_sqlalchemy

# add the following imports to the top of your file just below the current imports

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt

# add the following code just after the app=Flask(__name__) line
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



# add the following routes just before the if __name__ == '__main__' line at the end of the file
# Ths is to initialise the datbase and load initial data into the database.

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


