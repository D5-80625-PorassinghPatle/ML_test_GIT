from flask import Flask

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])

def index():

    return "starting Machien learning projec "

if  __name__=="__main__":

    app.run(debug=True)

def poras():

    pass