from flask import Flask
# Replace with the actual name of your file
from routes import bot_blueprint

app = Flask(__name__)
app.register_blueprint(bot_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
