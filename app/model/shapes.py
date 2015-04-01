from sqlalchemy import Column, Integer, String, Float, Time, Date, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ShapeConfiguration(Base):
    __tablename__ = 'shape_configurations'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    display_duration = Column(Float)
    show_delay = Column(Float)
    series = relationship("ShapeSerie", order_by="ShapeSerie.id", backref="configuration")


class ShapeSerie(Base):
    __tablename__ = 'shape_series'
    id = Column(Integer, primary_key=True)
    configuration = relationship("ShapeConfiguration", backref=backref('series', order_by=id))
    shapes = relationship("Shape", order_by="Shape.id", backref="serie")


class Shape(Base):
    __tablename__ = 'shapes'
    id = Column(Integer, primary_key=True)
    filename = Column(String)
    serie = relationship("ShapeSeries", backref=backref('shapes', order_by=id))


class ShapeSession(Base):
    __tablename__ = 'shape_sessions'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('people.id'))
    configuration_id = Column(Integer, ForeignKey('shape_configurations.id'))
    series = relationship("ShapeSessionSerie", order_by="ShapeSessionSerie.id", backref="session")
    date = Column(Date)


class ShapeSessionSerie(Base):
    __tablename__ = 'shape_session_series'
    id = Column(Integer, primary_key=True)
    session = relationship("ShapeSession", backref=backref('series', order_by=id))
    serie_id = Column(Integer, ForeignKey('shape_series.id'))
    expected_shape_id = Column(Integer, ForeignKey('shapes.id'))
    selected_shape_id = Column(Integer, ForeignKey('shapes.id'))
    display_time = Column(Time)
    action_time = Column(Time)
