from sqlalchemy.orm import Session

from models import Curso


# método responsável por buscar todos os cursos cadastrados;
class CursoRepository:
    @staticmethod
    def find_all(db: Session) -> list[Curso]:
        return db.query(Curso).all()
    
    """
    método responsável por salvar um curso no banco de dados, esse método foi escrito de forma que ele possa ser utilizado tanto para cadastro de um novo curso, quanto para a edição de um curso já existente;
    
    """
    @staticmethod
    def save(db: Session, curso: Curso) -> Curso:
        if curso.id:
            db.merge(curso)
        else:
            db.add(curso)
        db.commit()
        return curso

    """
    método responsável por buscar um curso no banco de dados com base do id do curso;
    """
    @staticmethod
    def find_by_id(db: Session, id: int) -> Curso:
        return db.query(Curso).filter(Curso.id == id).first()
    
    """
    método responsável por verificar se existe algum curso cadastrado com base no id do curso;
    """
    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Curso).filter(Curso.id == id).first() is not None
    
    """
     método responsável por excluir um curso com base no seu id.
    """
    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        curso = db.query(Curso).filter(Curso.id == id).first()
        if curso is not None:
            db.delete(curso)
            db.commit()