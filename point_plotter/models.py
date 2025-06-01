from sqlalchemy import Column, Integer, String, Text, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

# One shape can have many points
class PointClass(Base):
    __tablename__ = 'point_classes'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)

    # Relationship to points
    points = relationship("Point", back_populates="shape", cascade="all, delete")

class Point(Base):
    __tablename__ = 'points'

    id = Column(Integer, primary_key=True)
    x = Column(Integer, nullable=False)
    y = Column(Integer, nullable=False)

    point_class_id = Column(Integer, ForeignKey('point_classes.id'))
    shape = relationship("PointClass", back_populates="points")


# This will ACTUALLY create the database file and tables
def init_db(db_name="points.db"):
    engine = create_engine(f'sqlite:///{db_name}', echo=False)
    Base.metadata.create_all(engine)
    return engine

#  create a session
def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()