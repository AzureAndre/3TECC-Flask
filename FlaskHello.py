from flask import Flask       # Import the Flask class from the flask module

app = Flask(__name__)           # Create an instance of the Flask class, passing the name of the module as an argument

@app.route('/')                 # Define a route for the root URL ("/") and associate it with the hello_world function

def hello_world():              # Define the function that will be called when the root URL is accessed
    return 'Hello, World!'      # Return the string "Hello, World!" as the response to the request

if __name__ == '__main__':      # Check if the script is being run directly (as the main program)
    app.run(debug=True)                   # Start the Flask development server, which will listen for incoming requests and handle them using the defined routes and functions    

