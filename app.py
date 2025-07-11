from flask import Flask,render_template,request
app=Flask(__name__)
def chatbot_response(message):
    message=message.lower()
    if "hello" in message:
        return "hi,how are you"
    elif "bye" in message:
        return "good bye! thank for using chatbot"
    elif "movie" in message:
        return "Shall i take you to movie based website"
    else:
        return "sorry i cant find result for search something else"
@app.route("/getmessage",methods=["GET"])
def message():
    user_input=request.args.get("ques")
    return chatbot_response(user_input)

@app.route("/index",methods=["GET","POST"])
def index():
    return render_template("index.html")
   
if __name__=="__main__":
    app.run(debug=True)
