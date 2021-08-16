from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import date

from sqlalchemy.sql.sqltypes import Integer


class CreateMandate( BaseModel ):
    id : int
    begin_date : date
    end_date : date