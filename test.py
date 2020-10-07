import pymysql
import io, sys
import random, datetime
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') 
db = pymysql.connect("localhost","root","mysqltest","poetry" )
cursor = db.cursor()

seasonList = ['冬','春', '春', '春', '暑', '暑', '夏', '秋', '秋', '秋', '冬', '冬']
month = datetime.datetime.now().month
print(seasonList[month - 1])
sql = ''' SELECT * FROM tang WHERE paragraphs REGEXP '%s' ''' % (seasonList[month - 1])
cursor.execute(sql)
poetryList = cursor.fetchall() # 匹配诗词列表
roll = random.randint(0, len(poetryList)) # 随机数
print(poetryList[roll])

db.close()
