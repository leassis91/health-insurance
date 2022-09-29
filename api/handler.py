import pickle
import pandas as pd
from flask import Flask, request, Response
# from NOME_DA_PASTA.NOME_DO_ARQUIVO import NOME_DA_FUNCAO
from healthinsurance.Insurance import HealthInsurance


# loading model
path = 'home/leassis/repos_wsl/projects/health_insurance/'
model = pickle.load(open(path + 'src/models/lgbm_final.pkl', 'rb'))

# initialize API
app = Flask(__name__)

@app.route('/heatlhinsurance/predict', methods=['POST'])
def health_insurance_predict():
    test_json = request.get_json()
    
    if test_json: #verifica se existe
        
        if isinstance(test_json, dict):
            test_raw = pd.DataFrame(test_json, index=[0])
            
        else:
            test_json = pd.DataFrame(test_json, columns=test_json[0].keys())
            
        pipeline = HealthInsurance()

        # data cleaning
        df1 = pipeline.data_cleaning(test_raw)

        # feature engineering
        df2 = pipeline.feature_engineering(df1)

        # data preparation
        df3 = pipeline.data_preparation(df2)

        # prediction
        df_response = pipeline.get_prediction(model, test_raw, df3)


        return df_response
    
    else:
        return Response('{}', status=200, mimetype='application/json')
    
if __name__ == '__main__':
    # port = os.environ.get('PORT', 5000)
    app.run('192.168.1.2', debug=True)