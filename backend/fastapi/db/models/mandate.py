from pydantic.tools import T
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.sql.sqltypes import Float
from db.base_class import Base



class Mandate( Base ):
    id = Column(Integer, primary_key=True, index=True)
    begin_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    
