# importaçãoes necessarias
# create_engina - cria conexão com banco
# declarative_base para as classes do python
# sessionmaker que faz a gerencia dos comandos acontecer
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, Relationship

engine = create_engine('sqlite:///compra.db')
Base = declarative_base()
Sessao = sessionmaker(engine)

# Criado uma classe Usuario

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String(40), unique=True)
    idade = Column(Integer)

    def __repr__(self):
        return self.nome


class Livro(Base):
    __tablename__ = 'livros'

    id = Column(Integer, primary_key=True)
    nome = Column(String(70))

    autor_id = Column(Integer, ForeignKey('autores.id'))
    autor = Relationship('Autor', backref='livros', lazy='subquery')



class Autor(Base):
    __tablename__ = 'autores'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))



Base.metadata.create_all(engine)

with Sessao() as sessao:

    # CREATE USUARIOS adicionando 
    # usuarios = Usuario(nome='Davi Carvalho', idade=33)
    # sessao.add(usuarios)
    # sessao.commit()

    # usuarios = Usuario(nome='Osvaldo', idade=54)
    # sessao.add(usuarios)
    # sessao.commit()
    
    # autor = Autor(nome='August Cury')
    # sessao.add(autor)
    # sessao.commit()

    # livro = Livro(nome='A luz da alegria', autor_id=1)
    # sessao.add(livro)
    # sessao.commit()

    # READ USUARIOS
    # usuarios = sessao.query(Usuario).first()
    # print(usuarios)

    # usuarios = sessao.query(Usuario).filter_by(id=2).first()
    # print(usuarios)

    # usuarios = sessao.query(Usuario).all()
    # print(usuarios)

    # usuarios = sessao.query(Usuario).all()
    # for usuario in usuarios:
    #     print(usuario.nome)

    # usuarios = sessao.query(Usuario).order_by(Usuario.idade).all()
    # for usuario in usuarios:
    #     print(usuario.nome)


    #UPDATE USUARIOS
    # usuarios = sessao.query(Usuario).filter_by(id=3).first()
    # usuarios.idade = 10
    # sessao.commit()

    # usuarios = sessao.query(Usuario).filter_by(id=2).first()
    # usuarios.nome = 'Andreia Car'
    # sessao.commit()

    # DELETAR USUARIOS
    usuarios = sessao.query(Usuario).filter_by(id=4).first()
    sessao.delete(usuarios)
    sessao.commit()