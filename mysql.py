
import pymysql

# Connect to the database
# ahulock2018@47.96.175.196:3307
connection = pymysql.connect(host='47.96.175.196',
                             port= 3307,
                             user='root',
                             password='ahulock2018',
                             db='learning',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor=connection.cursor()     
sql = "INSERT INTO `liutiantian` (`fullname`,`age`, `card`,`school`) VALUES ('liutiantian','21','p19301167','anhuidaxue')" 
sql2= "UPDATE `liutiantian` SET age = age + 1  " 
sql3= "DELETE FROM `liutiantian` WHERE age < '%d'" % (22)               
try:
    cursor.execute(sql)
    connection.commit()
finally:
    print("yishangchuan")

try:
    cursor.execute(sql2) 
    connection.commit()
finally:
    print(2)
        # connection is not autocommit by default. So you must commit to save
        # your changes.
try:
    cursor.execute(sql3) 
    connection.commit()
    
finally:
    print(3)

try:
    cursor.execute("SELECT * FROM `liutiantian`")
    results = cursor.fetchall()
    print(results)
    for row in results:
        fullname=row['fullname']
        age=row['age']
        card=row['card']
        school=row['school']
        print('fullname=%s,age=%d,card=%s,school=%s'%(fullname,age,card,school))

finally:
    connection.close()


