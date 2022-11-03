from flask import *
import mysql.connector
from mysql.connector import pooling
from flask_restful import Resource, Api

app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)
api=Api(app)
app.secret_key="123789secret"

connectionpool = mysql.connector.pooling.MySQLConnectionPool(
  pool_name="mysqlpool",
  pool_reset_session=True,
  pool_size=5,
  host="localhost",
  port="3306",
  user="root",
  password="",
  database="website"
)

@app.route("/")
def index():
    return render_template("index.html")

#註冊
@app.route("/signup", methods=["POST"])
def signup():
    member_name=request.form["name"]
    account=request.form["account"]
    password=request.form["password"]
    try:
        connection=connectionpool.get_connection()
        mycursor=connection.cursor()
        mycursor.execute("SELECT * FROM member WHERE BINARY username = %s",[account])
        myresult=mycursor.fetchone()

        if myresult != None:
            return redirect("/error?message=帳號已經被註冊")

        mycursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)",[member_name, account, password])
        connection.commit()
        return redirect("/") 
    except:
        print("Unexpected Error")
    finally:
        mycursor.close()
        connection.close()
    

#登入
@app.route("/signin", methods=["POST"])
def signin():
    
    account=request.form["account"]
    password=request.form["password"]
    try:
        connection=connectionpool.get_connection()
        mycursor=connection.cursor()
        mycursor.execute("SELECT id,name FROM member WHERE BINARY username = %s AND BINARY password = %s",[account,password])
        myresult=mycursor.fetchone()

        if myresult == None:
            return redirect("/error?message=帳號或密碼輸入錯誤")

        session["id"]=myresult[0]
        session["name"]=myresult[1]
        return redirect("/member")
    except:
        print("Unexpected Error")
    finally:
        mycursor.close()
        connection.close()

#會員頁面
@app.route("/member")
def member():
    if "name" in session:
        name=session["name"]
        try:
            connection=connectionpool.get_connection()
            mycursor=connection.cursor()
            mycursor.execute("SELECT member.name,message.content FROM member INNER JOIN message WHERE member.id=message.member_id ORDER BY message.time DESC")
            results=mycursor.fetchall()
            return render_template("member.html",name=name,results=results)
        except:
            print("Unexpected Error")
        finally:
            mycursor.close()
            connection.close()
    return redirect("/")

#錯誤頁面
@app.route("/error")
def error():
    msg=request.args.get("message","")
    return render_template("error.html",message=msg)

#登出
@app.route("/signout")
def signout():
    del session["id"]
    del session["name"]
    return redirect("/")

#新增留言(增加session驗證)
@app.route("/message", methods=["POST"])
def message():
    content=request.form["content"]
    if "id" in session:
        member_id=session["id"]
        try:
            connection=connectionpool.get_connection()
            mycursor=connection.cursor()
            mycursor.execute("INSERT INTO message (member_id, content) VALUES (%s, %s)",[member_id, content])
            connection.commit()
            return redirect("/member")
        except:
            print("Unexpected Error")
        finally:
            mycursor.close()
            connection.close()
    return redirect("/")

#Api
class MemberSystem(Resource):
    #查詢會員資料
    def get(self):
        username=request.args.get("username")
        if "id" in session: #要驗證是已登入狀態
            try:
                connection=connectionpool.get_connection()
                mycursor=connection.cursor()
                mycursor.execute("SELECT id,name,username FROM member WHERE BINARY username = %s",[username])
                result=mycursor.fetchone()

                if result != None:
                    return {"data":{"id":result[0],"name":result[1],"username":result[2]}}
                return {"data":None}
            except:
                print("Unexpected Error")
            finally:
                mycursor.close()
                connection.close()
        return {"data":None}

    #更新會員姓名
    def patch(self):
        newName=request.json["name"]
        if "id" in session :
            id=session["id"]
            try:
                connection=connectionpool.get_connection()
                mycursor=connection.cursor()
                mycursor.execute("UPDATE member SET name = %s WHERE id = %s",[newName, id])
                connection.commit()
                
                mycursor.execute("SELECT name FROM member WHERE BINARY name = %s",[newName])
                result=mycursor.fetchone()

                if result != None:
                    return {"ok":True}
                return {"error":True}
            except:
                print("Unexpected Error")
            finally:
                mycursor.close()
                connection.close()
        return {"error":True}

api.add_resource(MemberSystem, "/api/member")

if __name__ == "__main__":
    # app.config['JSON_AS_ASCII'] = False
    app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
    app.run(port=3000, debug=True)