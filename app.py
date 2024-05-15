from dataclasses import dataclass
import datetime
from sqlalchemy import select, and_, or_, ForeignKey, UniqueConstraint
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func
from flask import Flask, jsonify,  request, render_template,session,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
app = Flask(__name__)
db = SQLAlchemy(app)



@dataclass
class PERSONA(db.Model):
    __tablename__ = 'PERSONA'
    id: int
    correo:str
    username: str
    password: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    correo = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'<PERSONA {self.username}>'
    
    def check_password(self, password):
        return self.password == password

@app.route('/personas',methods=['GET', 'POST'])
def route_personas():
    if request.method=='GET':
        personas = PERSONA.query.all()
        return jsonify(personas)
    
    elif request.method == 'POST':
        data = request.get_json()
        persona = PERSONA(username=data["username"], correo=data["correo"], password=data["password"])
        db.session.add(persona)
        db.session.commit()
        return jsonify(persona)


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        username = data['username']
        password = data['password']
        persona = PERSONA.query.filter_by(username=username).first()
        if persona is None:
            return 'No existe este nombre de usuario.'
        else:
            if persona.password == password:
                return jsonify(persona)
            else:
                return 'Contraseña incorrecta.'
        