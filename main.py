from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Flag(BaseModel):
    reto: str
    flag_hash_o_texto: str
    puntos: int | None
    resuelta: bool

class FlagRespuesta(BaseModel):
    id: int
    reto: str
    flag_hash_o_texto: str
    puntos: int | None
    resuelta: bool