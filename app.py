from flask import Flask
from dotenv import load_dotenv
from models import db
import os
from controllers.book_controller import books_bp

load_dotenv()
app = Flask(__name__)
url = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_DATABASE_URI'] = url
db.init_app(app)

app.register_blueprint(books_bp)

if __name__ == '__main__':
    app.run()

