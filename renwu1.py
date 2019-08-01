import csv
headers=['姓名','性别','年龄']
rows=[('刘甜甜',21,'女'),
      ('量产车',24,'男'),
      ('李聪聪',22,'女'),
      ('刘晨',23,'男'),
      ('张旭',24,'男')
      ]
with open('C:\\Users\\刘甜甜\Desktop\\学习笔记\\stock.csv','w',encoding='utf-8') as f:
    f_csv=csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)