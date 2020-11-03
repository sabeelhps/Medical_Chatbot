from flask import Flask,render_template,request,redirect,url_for
from chat import ask_question

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_response():
    
    userText = request.args.get('msg')
    
    # response="Heyyyy........"

    response=ask_question(userText)
    print("Length : {}".format(len(response)))
    if len(response)==0:
        return str("")
    else:
        return str(response)
    

if __name__ == '__main__':
    app.run(debug=True)