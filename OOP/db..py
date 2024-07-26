#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker, declarative_base
#from config import settings

#DB_URL = settings.DB_URL
#engine = create_engine(DB_URL)
#Session = sessionmaker(bind=engine)

#Base = declarative_base()

# Использование Base для определения моделей
#class User(Base):
#    __tablename__ = 'users'

#    id = Column(Integer, primary_key=True)
#    name = Column(String)
#    email = Column(String)

# Создвние таблиц
#if __name__ == "__main__":
#    Base.metadata.create_all(engine)