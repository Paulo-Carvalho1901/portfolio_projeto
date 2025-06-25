import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker


# configurando a engine do DB
engine = create_engine('sqlite:///database.db')

# configurando a sessao
Session = sessionmaker(engine)

# criando a tabela
Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String(40), nullable=False)
    tipo = Column(String(40), nullable=False)


# CREATE
def insert_usuario(nome_usuario, tipo_usuario):
    session = Session()
    try:
        if all([nome_usuario, tipo_usuario]):
            usuario = Usuario(nome=nome_usuario, tipo=tipo_usuario)
            session.add(usuario)
            session.commit()
            print(f'Usuário {nome_usuario} cadastrado com sucesso!')
        else:
            print('É o obrigatório preencher o nome e o tipo do usuario!')
    except Exception as e:
        session.rollback()
        print(f'Ocorreu um erro ao tentar cadastrar o usuário {nome_usuario}: {e}')
    finally:
        session.close()

# READ
def select_usuarios(nome_usuario=''):
    session = Session()
    try:
        if nome_usuario:
            dados = session.query(Usuario).filter(Usuario.nome == nome_usuario)
        else:
            dados = session.query(Usuario).all()

        for i in dados:
            print(f'Usuário: {i.nome} - Tipo: {i.tipo}')

    except Exception as e:
        print('Ocorreu algum erro ao consultar o(s) usuários(s)!')
    finally:
        session.close()

# UPDATE
def update_nome_usuario(id_usuario, nome_usuario):
    session = Session()
    try:
        if all([id_usuario, nome_usuario]):
            usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
            usuario.nome = nome_usuario
            session.commit()
            print('Nome do usuário atualizado com sucesso!')
        else:
            print('É obrigatório informar o id e novo nome do usuário!')
    except Exception as e:
        session.rollback()
        print('Ocorreu um erro ao atualizar o usuário')
    finally:
        session.close()

# DELETE
def delete_usuario(id_usuario):
    session = Session()
    try:
        if id_usuario:
            usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
            session.delete(usuario)
            session.commit()
            print(f'Usuário de ID {id_usuario} deletado com sucesso!')
        else:
            print('É obrigatório informar o ID do usuário a ser deletado')
    except Exception as e:
        session.rollback()
        print(f'Erro ao tentar deletar o usuário de ID {id_usuario}')
    finally:
        session.close()



if __name__ == '__main__':
    os.system('cls')
    Base.metadata.create_all(engine)
    # insert_usuario('Andreia', 'usuário convidado')
    # select_usuarios('Paulo Carvalho')
    # update_nome_usuario(1, 'Pedro Roberto')
    # delete_usuario(1)
