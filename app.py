from flask import Flask,redirect,render_template,request,url_for
import json
import os.path

app=Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/your_url" , methods=['POST','GET'])
def your_url():
    if request.method=='POST':

        urls={}
        if os.path.exists('your_url.json') :
            with open('your_url.json') as filename:
                urls=json.load(filename)
        if request.form['code'] in urls.keys():
            return redirect(url_for('home'))

        urls[request.form['code']]={'url':request.form['url']}
        with open('your_url.json','w') as filename:
            json.dump(urls,filename)

        return render_template('your_url.html',code=request.form['code'])
    else:
        return redirect(url_for('home'))




if __name__=="__main__":
    app.run(debug=True)