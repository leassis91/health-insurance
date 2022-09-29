import pickle
import pandas as pd
import numpy as np

class HealthInsurance:
    def __init__(self):
        self.home_path = ''
        self.annual_premium_scaler            = pickle.load(open('../features/annual_premium_scaler.pkl', 'rb'))
        self.age_scaler                       = pickle.load(open('../features/age_scaler.pkl', 'rb'))
        self.vintage_scaler                   = pickle.load(open('../features/vintage_scaler.pkl', 'rb'))
        self.target_encode_region_code_scaler = pickle.load(open('../features/target_encode_region_code_scaler.pkl', 'rb'))
        self.fe_policy_sales_channel_scaler   = pickle.load(open('../features/fe_policy_sales_channel.pkl', 'rb'))
        
    def data_cleaning(df):
        cols_new = ['id','gender','age','driving_license','region_code','previously_insured','vehicle_age','vehicle_damage','annual_premium','policy_sales_channel','vintage']
        
        # rename
        df.columns = cols_new
        
        return df
        
    def feature_engineering(df):
        # Vehicle Damage Number
        df['vehicle_damage'] = df['vehicle_damage'].apply(lambda x: 1 if x == 'Yes' else 0)
        
        # Vehicle Age
        df['vehicle_age'] = df['vehicle_age'].apply(lambda x: 'over_2_years' if x == '> 2 Years' else 'between_1-2_years'
                                                                             if x == '1-2 Year' else 'below_1_year')
        
        return df
    
    def data_preparation(df):        
        
        ## annual_premium
        df['annual_premium'] = self.annual_premium_scaler.transform(df[['annual_premium']].values)
        
        # age
        df['age'] = self.age_scaler.transform(df[['age']].values)

        # vintage
        df['vintage'] = self.vintage_scaler.transform(df[['vintage']].values)

        # gender
        df = pd.get_dummies(df,prefix='gender',columns=['gender'])
        
        # region_code - Frequency Encoding / Target Encoding / Weighted Target Encoding
        df.loc[:, 'region_code'] = df['region_code'].map(self.target_encode_region_code_scaler)

        # vehicle_age - One Hot Encoding / Frequency Encoding / Order Encoding
        df = pd.get_dummies(df, prefix='vehicle_age', columns=['vehicle_age'])

        # policy_sales_channel - Target Encoding / Frequency Encoding
        df.loc[:, 'policy_sales_channel'] = df['policy_sales_channel'].map(self.fe_policy_sales_channel_scaler)


        # Feature Selection
        cols_selected = ['annual_premium', 'vintage', 'age', 'region_code', 'vehicle_damage', 
                         'previously_insured', 'policy_sales_channel']
        
        return df[cols_selected]
    
    def get_predicition(self, model, original_data, test_data):
        # model prediction
        pred = model.predict_proba(test_data)
            
        # join prediction
        original_data['prediction'] = pred[:, 1]
        original_data = original_data.sort_values('prediction', ascending=False)
        
        return original_data.to_json(orient='records', date_format='iso')