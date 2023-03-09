from urllib import request
from flask import *
import json , time 

import os
from flask import send_from_directory


app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

# our first endpoint
@app.route('/' , methods= ['GET']) 
def Homepage() :
    page_data = {'Page':'Home' , 'Message': 'successfully loaded the homepage' , 'Timestamp' : time.time()} # returns the current time  
    # we are saying that we have a page and it has a value of home when we call the above endpoint  
    jsonFormat = json.dumps(page_data) # this function converts the object to a json format for strings

    return jsonFormat
# so very time we call this get route it creates this object and gives as current time then converts it to json

@app.route('/user/' , methods= ['GET']) 
def Requestpage() :
    user_query = str(request.args.get('user')) # /user/?user= USERNAME
    page_data = {'Page':'Request' , 'Message': f'successfully got the request for {user_query}' , 'Timestamp' : time.time()} # returns the current time  
    # we are saying that we have a page and it has a value of Request when we call the above endpoint  
    jsonFormat = json.dumps(page_data) # this function converts the object to a json format for strings

    return jsonFormat

if __name__ =='__main__':
    app.run( debug = True,port =5757)
