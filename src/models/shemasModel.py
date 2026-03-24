from pydantic import BaseModel, EmailStr, field
from typing import Optional
from datetime import date, time

class UsuarioShema(BaseModel):
    nombre: str = Field(min_length=3, max_length=100)
    email : EmailStr
    password: str = Field(mi)