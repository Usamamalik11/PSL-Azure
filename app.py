from flask import Flask,request,jsonify, render_template, url_for
import pandas as pd
import numpy as np
#from sklearn.base import BaseEstimator, TransformerMixin
#from sklearn import preprocessing

app=Flask(__name__)

with open('model' ,'rb') as f1:
    loaded_model = pickle.load(f1)



@app.route('/')
def home():
    #return 'Hello World'
    return render_template('index.html')
    #return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def predict():
    if request.method == 'POST':
        
        int_features = [x for x in request.form.values()]

        Over_Ball=int_features[0]
        Batting_Team=int_features[1]
        Bowling_Team=int_features[2]
        Stadium=int_features[3]
        Runs_Scored=int_features[4]
        Extras=int_features[5]
        Fallen_Wickets=int_features[6]
        Cumulative_Runs_Scored=int_features[7]
        
        data={'Over_Ball':[Over_Ball],
              'Batting_Team':[Batting_Team],
              'Bowling_Team':[Bowling_Team],
              'Stadium':[Stadium],
              'Runs_Scored':[Runs_Scored],
              'Extras':[Extras],
              'Fallen_Wickets':[Fallen_Wickets],
              'Cumulative_Runs_Scored':[Cumulative_Runs_Scored]
            }
        
        
        check = pd.DataFrame (data, columns =['Over_Ball','Batting_Team', 'Bowling_Team','Stadium','Runs_Scored', 'Extras', 'Fallen_Wickets','Cumulative_Runs_Scored'])
        Bat=pd.Series(check['Batting_Team'].values)
        check[['Batting_Team']]=Bat.map({'Islamabad United':0,'Peshawar Zalmi':4,'Quetta Gladiators':5,'Lahore Qalandars':2,'Multan Sultans':3,'Karachi Kings':1})
        Bowl=pd.Series(check['Bowling_Team'].values)
        check[['Bowling_Team']]=Bowl.map({'Islamabad United':0,'Peshawar Zalmi':4,'Quetta Gladiators':5,'Lahore Qalandars':2,'Multan Sultans':3,'Karachi Kings':1})
        Stad=pd.Series(check['Stadium'].values)
        check[['Stadium']]=Stad.map({'Sharjah Cricket Stadium':5,'Rawalpindi Cricket Stadium':4,'Gaddafi Stadium Lahore':1,'Dubai International Cricket Stadium':0,'National Stadium Karachi':3,'Sheikh Zayed Stadium Abu Dhabi':6,'Multan Cricket Stadium':2})
        prediction=loaded_model.predict(check)
        return render_template('index.html', prediction_text="Predicted Score is {}".format(prediction))
         


'''
@app.route('/predict_api',methods=['POST'])
def predict_api():
    
    For direct API calls trought request
    
    data = request.get_json(force=True)
    prediction = loaded_model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)
'''




    













if __name__=='__main__':
    app.run(debug=True)