from flask import Flask,render_template,request
from summary import summarizer

app=Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')  

@app.route('/summarize',methods=['GET','POST'])
def summarize():
    if request.method=='POST':
        rawtext=request.form['rawtext']
        summary,original,len_orig,len_summ=summarizer(rawtext)

    return render_template('summary.html',summary=summary,original=original,len_orig=len_orig,len_summ=len_summ)

if __name__=='__main__':
    app.run(debug=True)