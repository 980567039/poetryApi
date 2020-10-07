from typing import Optional
from fastapi import FastAPI
import pymysql
import io, sys
from api.toDayPoetry import *
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') 
db = pymysql.connect("localhost","root","mysqltest","poetry" )
cursor = db.cursor()

app = FastAPI()

# 获取今日诗词
@app.get("/toDayPoetry")
def read_Poetry():
  data = getToDatPoetry(cursor)
  return {"author": data[0], 'paragraphs': data[1], 'title': data[2], 'id': data[3]}