from pydantic.tools import T
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.sql.sqltypes import Float
from db.base_class import Base


class Candidate( Base ):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    document = Column(String, primary_key=True, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True, index=True)
    party = Column(String, nullable=False)
    spent_daily = Column(Float, nullable=True)
    spent_monthly = Column(Float, nullable=True)
    spent_total = Column(Float, nullable=True)
    mandate_id = Column(Integer, ForeignKey('mandate.id'))
