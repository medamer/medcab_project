# web_app/__init__.py

from flask import Flask

from web_app.routes.home import home
#from web_app.routes.home import predictions

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home)
    #app.register_blueprint(predictions)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)