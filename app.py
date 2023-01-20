#import TableClass
#import sqlalchemy
#from sqlalchemy.orm import sessionmaker

#engine = sqlalchemy.create_engine('sqlite:///C:\\Users\\user\\python\\hello\\mydb.db')
#Session = sessionmaker(bind=engine)
# DB table 생성
#TableClass.create_tb(engine)


from flask import Flask, request, render_template, url_for ,abort, session ,redirect
import dbdb , sqlite3

app = Flask(__name__)

app.secret_key = b'aaa!111/'

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form["username"]
        cont = request.form["content"]
        session['user'] = name
        
        with open("static/submit_save.txt_{}".format(name),"w", encoding='utf-8') as f:
            f.write("%s , %s" % (name , cont ))
        
         
        return "POST로 전달된 데이터({}, {})".format(name, cont)
        
        
        
@app.route('/get_register')
def get_register():
    data = session['user']
    
    with open("static/submit_save.txt_{}".format(data), "r", encoding='utf-8') as file:
        student = file.read().split(',')  # 쉽표로 잘라서 student 에 배열로 저장
    return 'NAME : {}, 인사말 : {}'.format(student[0], student[1])

@app.route('/main_boot')
def main_boot():
    return render_template('main_boot.html')


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/main')
def index_start():
    return render_template('main.html')
    
@app.route('/startgame')
def startgame():
    return render_template('startgame.html')
    
@app.route('/join')
def join():
    return render_template('main.html')
    
@app.route('/artemis')
def myimage():
    return render_template("myimage.html")
    
@app.route('/register')
def hellohtml():
    return render_template('form.html')

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return 'GET 으로 전송이다.'
    else:
        num = request.form["num"]
        name = request.form["name"]
        #args_dict = request.args.to_dict()
        #print(args_dict[num], [name])
        dbdb.insert_data(num, name)
        
        #session = Session()
        #st_data = TableClass.Students(num, name)
        #try:
            #session.add(st_data)
            #session.commit()
        #except Exception as e:
            #session.rollback ()
            #abort (500, 'Error. 데이터 저장 실패')
        return 'POST 이다. 학번은: {} 이름은: {}'.format(num, name)

@app.route('/getinfo')
def getinfo():
    info = dbdb.select_all()
    return render_template("info.html", data=info)

# 로그인
@app.route('/login', methods=['POST'])
def login():
    
        num = request.form["num"]
        name = request.form["name"]
        
        #dbdb.insert_data(num, name)
        #return render_template('login.html')
    
        if len(num) == 0 or len(name) == 0:
            return 'Register'
        
        #dbdb.dbcon()
        #dbdb.select_all_me()
        #c = dbdb.select_num_me(num)
        else:
            con = sqlite3.connect('mydb.db')
            cursor = con.cursor()
            #setdata = (num,)
            
            sql = ' SELECT * FROM student '
            sql += ' WHERE num = ? ' #query 만들때 앞뒤로 공백주기
            cursor.execute(sql, (num,))
            
            rows = cursor.fetchall() #리턴값 없으면 [], 있으면 list-tuple [(),()]
            for rs in rows:
                if name == rs[1] and num == rs[0]: # userId == rs[1] 얜 없어도됨
                    session['logFlag'] = True
                    session['num'] = rs[0]
                    session['name'] = rs[1]
                    return redirect(url_for('join'))
                
                
                elif  name != rs[1] and num != rs[0]:   
                    return 'Member not found please register'
                
                elif name != rs[1] or num != rs[0]:
                    return "Member NOT FOUND. please register"
                     
                     
                     # return redirect(url_for('register'))
                     
                     
                     
                
        
                
              
        
        
        
        # id와 pw가 임의로 정한 값이랑 비교 해서 맞으면 맞다 틀리면 틀리다
        #if id == 'abc' and pw == '1234':
            #session['user'] = id
            #return '''
                #<script> alert("안녕하세요~ {}님");
                #location.href="/form"
                #</script>
            #'''.format(id)
            # return redirect(url_for('form'))
        #else:
            #return "아이디 또는 패스워드를 확인 하세요."


# 로그아웃(session 제거)
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

# 로그인 사용자만 접근 가능으로 만들면
@app.route('/form')
def form():
    if 'user' in session:
        return render_template('test.html')
    return redirect(url_for('login'))


#def getinfo():
    info = dbdb.select_all()
    retstr = ''
    for i, v in enumerate(info):
        retstr += '%d. 학번: %s 이름: %s<br>' % (i+1, v[0], v[1])
    return retstr
    
    
    
    #session = Session()
    #info  = session.query(TableClass.Students.num, TableClass.Students.name).all()
    #return render_template("info.html", data=info)




if __name__ == '__main__':
    app.run(debug=True)