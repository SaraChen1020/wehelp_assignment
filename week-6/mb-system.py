from flask import *
import mysql.connector

app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)
app.secret_key="123789secret"

connection = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="159753",
  database="website"
)
mycursor=connection.cursor()

@app.route("/")
def index():
    return render_template("index.html")

#註冊
@app.route("/signup", methods=["POST"])
def signup():
    member_name=request.form["name"]
    account=request.form["account"]
    password=request.form["password"]

    sql="SELECT * FROM member WHERE username = %s"
    mycursor.execute(sql,(account,))
    # mycursor.execute("SELECT * FROM member WHERE username = %s",[account])
    myresult=mycursor.fetchone()

    if myresult != None:
        return redirect("/error?message=帳號已經被註冊")
    else:
        sql="INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
        mycursor.execute(sql,(member_name,account,password))
        # mycursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)",[member_name, account, password])
        connection.commit()
        return redirect("/")

#登入
@app.route("/signin", methods=["POST"])
def signin():
    account=request.form["account"]
    password=request.form["password"]

    mycursor.execute("SELECT id,name FROM member WHERE username = %s AND password = %s",[account,password])
    myresult=mycursor.fetchone()

    if myresult == None:
        return redirect("/error?message=帳號或密碼輸入錯誤")
    else:
        session["id"]=myresult[0]
        session["name"]=myresult[1]
        return redirect("/member")

#會員頁面
@app.route("/member")
def member():
    if "name" in session:
        name=session["name"]
        mycursor.execute("SELECT member.name,message.content FROM member INNER JOIN message WHERE member.id=message.member_id ORDER BY message.time DESC")
        results=mycursor.fetchall()
        return render_template("member.html",name=name,results=results)
    else:
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

#新增留言
@app.route("/message", methods=["POST"])
def message():
    content=request.form["content"]
    member_id=session["id"]

    mycursor.execute("INSERT INTO message (member_id, content) VALUES (%s, %s)",[member_id, content])
    connection.commit()

    return redirect("/member")

app.run(port=3000)