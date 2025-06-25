from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configurando a engine do DB
engine = create_engine('sqlite:///database.db')

# Configurando a sessão
Session = sessionmaker(engine)

