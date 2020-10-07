import random, datetime

def getToDatPoetry(cur):
  seasonList = ['冬','春', '春', '春', '暑', '暑', '夏', '秋', '秋', '秋', '冬', '冬']
  month = datetime.datetime.now().month
  sql = ''' SELECT * FROM tang WHERE paragraphs REGEXP '%s' ''' % (seasonList[month - 1])
  cur.execute(sql)
  poetryList = cur.fetchall() # 匹配诗词列表
  roll = random.randint(0, len(poetryList)) # 随机数
  return poetryList[roll]