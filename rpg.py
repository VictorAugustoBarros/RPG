from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from route.rpg import rpg_blueprint

application = Flask(__name__)

application.config["SWAGGER"] = {
    "title": "RPG",
    "version": "1.0.0"
}
CORS(application)
swag = Swagger(application)

application.register_blueprint(rpg_blueprint)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, debug=True)
