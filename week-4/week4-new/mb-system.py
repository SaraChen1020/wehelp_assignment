from flask import *
app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def signin():
    account=request.form["account"]
    password=request.form["password"]

    if account=="test" and password=="test":
        res=make_response(redirect("/member"))
        res.set_cookie(key="user-login",value="success", max_age=3600)
        return res 
    elif account=="" or password=="":
        return redirect("/error?message=請輸入帳號、密碼")
    else:
         return redirect("/error?message=帳號、或密碼輸入錯誤")

@app.route("/member")
def member():
    if "user-login" in request.cookies:
        return render_template("member.html")
    else:
        return redirect("/")

# /error?message="文字"
@app.route("/error")
def error():
    msg=request.args.get("message","")
    return render_template("error.html",message=msg)

@app.route("/signout")
def signout():
    res=make_response(redirect("/"))
    res.delete_cookie("user-login")
    return res


@app.route("/square/<number>")
def result(number):
    if int(number) >= 0:
        number=int(number)
        result=number*number
        return render_template("square.html",result=result)
    else:
        return render_template("error-num.html")
app.run(port=3000)