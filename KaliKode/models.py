from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import hashlib

db = SQLAlchemy()

# criptografia simples
def criptografar_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

class Editor(db.Model):
    __tablename__ = 'editores'
    id = db.Column(db.String(2), primary_key=True)  # contagem hex de 00 a FF
    nome = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(64), nullable=False) 

    riddles = relationship('Riddle', back_populates='criador')

class Riddle(db.Model):
    __tablename__ = 'riddles'
    id = db.Column(db.String(3), primary_key=True)  # contagem hex de 00 a FF
    id_usuario = db.Column(db.String(2), ForeignKey('editores.id'), nullable=False)
    string1 = db.Column(db.String(50), nullable=False)
    imagem = db.Column(db.String(100), nullable=False)  # caminho da imagem
    string2 = db.Column(db.String(50), nullable=False)
    resposta = db.Column(db.String(50), nullable=False)

    criador = relationship('Editor', back_populates='riddles')
    avaliacoes = relationship('Avaliacao', back_populates='riddle')

class Avaliacao(db.Model):
    __tablename__ = 'dificuldades'
    id = db.Column(db.Integer, primary_key=True)
    id_riddle = db.Column(db.String(3), ForeignKey('riddles.id'), nullable=False)
    id_editor = db.Column(db.String(2), ForeignKey('editores.id'), nullable=False)
    classificacao = db.Column(db.String(1), nullable=False)  # F, M ou D
    observacao = db.Column(db.String(200))

    riddle = relationship('Riddle', back_populates='avaliacoes')
    editor = relationship('Editor')
