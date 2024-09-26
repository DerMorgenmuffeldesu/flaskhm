from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request
from flask_migrate import Migrate



MYSQL_DSN = 'mysql://admin:1234@127.0.0.1:3306/flask_test'

#app = Flask('test_app')
app = Flask(__name__)
#app.config.from_mapping(SQLALCHEMY_DATABASE_URI=MYSQL_DSN)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:1234@127.0.0.1:3306/flask_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.init_app(app)


@app.route('/advs', methods=['POST'])
def create_ad():
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No input data provided'}), 400
    
    header = data.get('header')
    owner = data.get('owner')
    description = data.get('description')

    if not header or not owner or not description:
        return jsonify({'error': 'Missing required fields'}), 400

    new_ad = AdvModel(header=header, owner=owner, description=description)
    db.session.add(new_ad)
    db.session.commit()

    return jsonify({'message': 'Ad created successfully'}), 201
