from time import time
from fastapi import FastAPI, __version__

import pandas as pd 

df = pd.read_csv('./data/diagnoses2018.csv')

app = FastAPI()

@app.get('/')
async def hello():
    return {'res': 'pong', 'version': __version__, "time": time()}

@app.route('/', methods=["GET"])
def home():
    return 'this is a API service for MN ICD code details'

@app.route('/preview', methods=["GET"])
def preview():
    top10rows = df.head(1)
    result = top10rows.to_json(orient="records")
    return result

@app.route('/serviceyear/<value>', methods=['GET'])
def serviceyear(value):
    print('value:', value)
    filtered = df[df['service_year'] == value]
    if len(filtered) <= 0:
        return 'There is nothing here'
    else:
        return filtered.to_json(orient="records")
        
@app.route('/serviceyear/<value>/sex/<value2>')
def serviceyear2(value, value2):
    filtered = df[df['service_year'] == value]
    filtered2 = filtered[filtered['sex'] == value2]
    if len(filtered2) <= 0:
        return 'There is nothing here'
    else:
        return filtered2.to_json(orient="records")


if __name__ == '__main__':
app.run(debug=True)