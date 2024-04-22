from flask import Flask,render_template,request
import pickle
app = Flask(__name__)


#load the model
model = pickle.load (open ('eps_v1.sav' , 'rb'))

#home page
@app.route('/')
def home():
    return render_template('index.html', **locals())


@app.route('/predict', methods = ['POST','GET'])
def predict ():
    v1 = float ( request.form['ROCE (%)'] ) 
    v2 = float ( request.form['CASA (%)']  ) 
    v3 = float ( request.form['Return on Equity / Networth (%)'] ) 
    v4 = float ( request.form['Non-Interest Income/Total Assets (%)']  ) 
    v5 = float ( request.form['Operating Profit/Total Assets (%)'] ) 
    v6 = float ( request.form['Operating Expenses/Total Assets (%)']  ) 
    v7 = float ( request.form['Interest Expenses/Total Assets (%)'] ) 
    v8 = float ( request.form['Face_value']  ) 
    


    result = model.predict ([[v1,v2,v3,v4,v5,v6,v7,v8]]) [0]

    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run ()