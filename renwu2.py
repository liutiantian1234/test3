import json
data = {
    'name':'ltt',
    'age':21,
    'sex':'female'
}
with open('C:\\Users\\刘甜甜\\Desktop\\学习笔记\\stock.json','w',encoding='utf-8') as f:
    json.dump(data,f)
