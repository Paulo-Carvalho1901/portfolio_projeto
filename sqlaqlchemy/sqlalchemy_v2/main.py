import os
from database.database import Session, engine
from models.usuario import Usuario, Base



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
            print('É o obrigatório preencher o nome e o tipo do usuário!')
    except Exception as e:
        session.rollback()
        print(f'Ocorreu um  erro ao tentar cadastrar usuário {nome_usuario}: {e}')
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
            print(f'Uusuário {i.nome} - Tipo: {i.tipo}')
           
    except Exception as e:
        print(f'Usuário algum erro ao consultar o(s) usuário(s)!')
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
            print('É obrigatório informar o ID e novo nome do usuário!')
    except Exception as e:
        session.rollback()
        print(f'Ocorreu um erro ao atualizar o usuáro: {e}' )
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
        print(f'Erro ao tentar deletar o usuário ID {id_usuario}: {e}')
    finally:
        session.close()



if __name__ == '__main__':
    Base.metadata.create_all(engine)
    # insert_usuario('Davi', 'usuario_admin')
    # select_usuarios('Paulo')
    # update_nome_usuario(1, 'Pedro Roberto')
    # delete_usuario(1)