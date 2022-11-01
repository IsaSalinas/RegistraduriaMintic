import json
from flask import Flask
from flask import jsonify # coge un dicc y lo pasa a json
from flask_cors import CORS
from waitress import serve

regisApp = Flask(__name__) #Creamos la aplicacion de Flask
cors = CORS(regisApp)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
