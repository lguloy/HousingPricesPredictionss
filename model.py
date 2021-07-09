import pickle
import pandas as pd
def run_model(dictionary):
    #LOAD MODEL
    VSC_model = pickle.load(open("VLC_Ames_Housing_Price_Model", 'rb'))
    
    #CONVERT TO INTEGERS
    for sub in dictionary:
        dictionary[sub] = str(dictionary[sub])
    
    #CONVERT TO DATA FRAME
    df = pd.DataFrame(data=dictionary, index=range(1))
    
    #USE VSC_MODEL
    sale_price = VSC_model.predict(df)[0]
    
    return sale_price
    
