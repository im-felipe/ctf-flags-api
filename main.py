from pydantic import BaseModel
from fastapi import FastAPI
import sqlite3

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

@app.get("/flags", response_model=list[FlagRespuesta])
def mostrar_flags():
    conexion = sqlite3.connect("flags.db")
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT id, reto, flag_hash_o_texto, puntos, resuelta FROM flags
    """)
    filas = cursor.fetchall()
    cursor.close()
    conexion.close()
    return [dict(fila) for fila in filas]

@app.post("/flags", response_model=FlagRespuesta)
def insertar_flag(flag: Flag):
    conexion = sqlite3.connect("flags.db")
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO flags (reto, flag_hash_o_texto, puntos, resuelta) VALUES (?, ?, ?, ?)", (flag.reto, flag.flag_hash_o_texto, flag.puntos, int(flag.resuelta)))
    conexion.commit()
    nuevo_id = cursor.lastrowid
    cursor.close()
    conexion.close()
    return {"id": nuevo_id, "reto": flag.reto, "flag_hash_o_texto": flag.flag_hash_o_texto, "puntos": flag.puntos, "resuelta": flag.resuelta}
    
