from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import date

class CreateCandidate( BaseModel ):
    id : str
    name : str
    document : str
    email : EmailStr
    party : str
    spent_daily : float
    spent_monthly : float
    spent_total : float
