from flask  import Flask
from utils.db import db
from routes.productos import Productos_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/inventariodb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'

db.init_app(app)

app.register_blueprint(Productos_bp)
