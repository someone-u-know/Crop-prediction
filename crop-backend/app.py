from flask import Flask, request, jsonify
from flask_cors import CORS

import pickle
with open ('model.pkl', 'rb') as f:
   model= pickle.load(f)

def pred_result(n,p,ph,t,r,h):
    x_new=[[n,p,ph,t,r,h]]
    y=model.predict(x_new)[0]
    return y



app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
def index():
    return {"name":"croppy"}


@app.route('/predict', methods=['POST'])
def greet():
    # Get the 'name' parameter from the URL query string
    data= request.get_json()
    N=data['N']
    P=data['P']
    Ph=data['Ph']
    temp=data['temp']
    rainf=data['rainf']
    humidity=data['humidity']
    print(N,P,Ph,temp,rainf,humidity)
    result = pred_result(int(N),int(P),int(Ph),int(temp),int(rainf),int(humidity))
    r=str(result)
    
    return {"crop":r}

if __name__ == '__main__':
    app.run(debug=True)