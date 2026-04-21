from flask import Flask, render_template         # Import the Flask class from the flask module

app = Flask(__name__)

# The following shows a function with two routes.
@app.route('/')
@app.route('/hello')
def hello_world():
    return '<head><h1>Hello, World!</h1></head>'

# The following shows a function with a route that accepts parameters.
@app.route('/user/<string:username>/id/<int:user_id>')
def user_profile(username, user_id):
    return f'Hello user #{str(user_id)},  {username}!!'

# The following shows a function with a route that accepts only POST requests. 
# The return is a string that indicates that this endpoint is for GET requests only.
# This should fail to load
@app.route('/getonly', methods=['POST'])
def get_only():
    return 'This is a GET request only endpoint!'   


# This will render the templates/hello.html template when the /hellohtml route is accessed.
@app.route('/hellohtml')
def hello_html():
    return render_template('hello.html')      



if __name__ == '__main__':
    app.run(debug=True)