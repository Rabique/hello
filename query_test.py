import sqlite3
con = sqlite3.connect('mydb.db')
cursor = con.cursor()
            #setdata = (num,)
            
sql = ' SELECT * FROM student '


#sql += ' WHERE name = ? ' #query 만들때 앞뒤로 공백주기
cursor.execute(sql,)
ret = cursor.fetchall()            
#rows = cursor.fetchall() #리턴값 없으면 [], 있으면 list-tuple [(),()]
print (ret)
#for rs in rows:
    #if name == rs[1] and num == rs[0]: # userId == rs[1] 얜 없어도됨
        #session['logFlag'] = True
        #session['num'] = rs[0]
        #session['name'] = rs[1]