#Imports
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import getpass
from sqlalchemy.ext.declarative import declarative_base
import sys
import reusables


#Setup
logger = reusables.get_logger(__name__, level=10, stream=sys.stdout)
eng_local = 'sqlite:///db1.db'          #home/{}/Documents/.format(getpass.getuser())
engine = create_engine(eng_local)
Base = declarative_base()


#Tables
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    password = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', password='%s')>" % (self.name, self.password)


class Soaps(Base):
    __tablename__ = 'soaps'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(500))
    season = Column(String(50))
    date_created = Column(DateTime)
    wholesale = Column(Float)
    retail = Column(Float)
    batch_size = Column(Integer)
    recipe_link = Column(String(100))
    stock = Column(Integer)
    #recipes = relationship("Recipes", back_populates='soaps')

    def __repr__(self):
        return "<Soaps(name='%s', description='%s', season='%s', date_created='%s', wholesale='%s', retail='%s', " \
               "batch_size='%s', recipe_link='%s', stock='%s')>" %(self.name, self.description, self.season,
                        self.date_created, self.wholesale, self.retail, self.batch_size, self.recipe_link, self.stock)
"""
class Recipes(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    #ingredients = Column(String(60))
    amount = Column(Float, ForeignKey('amounts.id'))
    soap_id = Column(Integer, ForeignKey('soaps.id'))
    soaps = relationship("Soaps", back_populates='recipes')
    ingredients = relationship("Ingredients", back_populates='recipes')
    amounts = relationship("Amounts", back_populates='recipes')

    def __repr__(self):
        return "<Recipes(user_id='%s', soap_id='%s', ingredients='%s', amounts='%s', amount_units='%s')>" % \
               (self.user_id, self.soap_id, self.ingredients, self.amounts, self.amount_units)


class Ingredients(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    cost_per = Column(Float)
    table_parent = relationship(Recipes)

    def __repr__(self):
        return "<Ingredients(id='%s', name='%s', cost_per='%s')>" % (self.id, self.name, self.cost_per)

class Amounts(Base):
    __tablename__ = 'amounts'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'))
    amount = Column(Integer)
    amount_units = Column(String(40))
    #table_parent = relationship(Recipes, back_populates='amounts')

    def __repr__(self):
        return "<Amounts(id='%s', recipe_id='%s', ingredient_id='%s', amount='%s', amount_units='%s')>" % \
               (self.id, self.recipe_id, self.ingredient_id, self.amount, self.amount_units)


print(User)
print(Recipes)
"""
Base.metadata.create_all(engine)



