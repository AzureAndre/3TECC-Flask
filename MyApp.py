from flask import Flask, render_template as RenderTemplate      # Import the Flask class from the flask module

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




@app.route('/allposts')
def posts():
    return RenderTemplate('allposts.html', posts=allposts)



@app.route('/')                 # Define a route for the root URL ("/") and associate it with the hello_world function

def index():              # Define the function that will be called when the root URL is accessed
    return RenderTemplate('index.html')      # Return the rendered HTML template as the response to the request




if __name__ == '__main__':      # Check if the script is being run directly (as the main program)
    app.run(debug=True)                   # Start the Flask development server, which will listen for incoming requests and handle them using the defined routes and functions    
