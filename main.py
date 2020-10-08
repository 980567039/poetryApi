from typing import Optional
from fastapi import FastAPI
import pymysql
import io, sys
from api.toDayPoetry import *
from fastapi.middleware.cors import CORSMiddleware
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') 
db = pymysql.connect("localhost","root","mysqltest","poetry" )
cursor = db.cursor()

app = FastAPI()
origins = [
  "http://144.34.161.204",
  "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 获取今日诗词
@app.get("/toDayPoetry")
def read_Poetry():
  data = getToDatPoetry(cursor)
  return {"author": data[0], 'paragraphs': data[1], 'title': data[2], 'id': data[3]}