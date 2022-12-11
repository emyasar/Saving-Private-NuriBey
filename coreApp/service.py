###################
# This code generated by my new assistant https://chat.openai.com/chat
####################

from flask import Flask, request
from subprocess import call

app = Flask(__name__)

@app.route('/run_app', methods=['POST'])
def run_app():
    # Get the application to run from the request body.
    app = request.json['app']

    # Run the application using the `call()` function from the `subprocess` module.
    return_code = call(['python', app])

    # Return the return code as the response.
    return str(return_code)

if __name__ == '__main__':
    app.run()
