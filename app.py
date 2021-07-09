from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import model
import os
from tables import create_classes
from config import password

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
from flask_sqlalchemy import SQLAlchemy

## CREATE CONNECTION ##
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '').replace("://", "ql://", 1) or f'postgresql+psycopg2://postgres:{password}@housingpriceprediction.cxgg7v5earry.us-east-2.rds.amazonaws.com:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Features = create_classes(db)

@app.route("/", methods=["GET", "POST"])
def home():
    prices = "Awaiting entry"
    

    if request.method == "POST":
        model_input = {"Year Built": request.form["Yearbuilt"],
                       "1stFlrSF" : request.form["1stFlrSF"],
                       "GrLivArea": request.form["GrLivArea"],
                       "LotArea": request.form["LotArea"],
                       "GarageArea": request.form["GarageArea"],
                       "BsmtUnfSF": request.form["BsmtUnfSF"],
                       "TotalBsmtSF": request.form["TotalBsmtSF"],
                       "LotFrontage": request.form["LotFrontage"],
                       "GarageYrBlt": request.form["GarageYrBlt"],
                       "MoSold": request.form["MoSold"]
            
            }
        
        price= model.run_model(model_input)
        predicted_price = f'$ {price}'
        
        features = Features(firstflrsf=model_input["1stFlrSF"], \
                            grlivarea=model_input["GrLivArea"], \
                            lotarea=model_input["LotArea"], \
                            garagearea=model_input["GarageArea"], \
                           bsmtunfsf=model_input["BsmtUnfSF"], \
                            totalbsmtsf=model_input["TotalBsmtSF"], \
                            lotfrontage=model_input["LotFrontage"], \
                            garageyrblt=model_input["GarageYrBlt"], \
                            mosol=model_input["MoSold"], \
                            yearbuilt=model_input["Year Built"], \
                            saleprice=str(price) )
        db.session.add(features)
        db.session.commit()
        
        return render_template("index.html", prices=predicted_price)
    
    return render_template("index.html", prices=prices)
# =============================================================================
# @app.route("/send", methods=["GET", "POST"])
# def send():
#   if request.method == "POST":
#         model_input = {"Year Built": request.form["Yearbuilt"],
#                        "1stFlrSF" : request.form["1stFlrSF"],
#                        "GrLivArea": request.form["GrLivArea"],
#                        "LotArea": request.form["LotArea"],
#                        "GarageArea": request.form["GarageArea"],
#                        "BsmtUnfSF": request.form["BsmtUnfSF"],
#                        "TotalBsmtSF": request.form["TotalBsmtSF"],
#                        "LotFrontage": request.form["LotFrontage"],
#                        "GarageYrBlt": request.form["GarageYrBlt"],
#                        "MoSold": request.form["MoSold"]
#             
#             }
#         
#         price= model.run_model(model_input)
#         predicted_price = f'$ {price}'
#         
#         features = Features(firstflrsf=model_input["1stFlrSF"], \
#                             grlivarea=model_input["GrLivArea"], \
#                             lotarea=model_input["LotArea"], \
#                             garagearea=model_input["GarageArea"], \
#                            bsmtunfsf=model_input["BsmtUnfSF"], \
#                             totalbsmtsf=model_input["TotalBsmtSF"], \
#                             lotfrontage=model_input["LotFrontage"], \
#                             garageyrblt=model_input["GarageYrBlt"], \
#                             mosol=model_input["MoSold"], \
#                             yearbuilt=model_input["Year Built"], \
#                             saleprice=str(price) )
#         db.session.add(features)
#         db.session.commit()
#         
#         return render_template("index.html", prices=predicted_price)
#     
#     return render_template("dummy.html")
# 
# =============================================================================
    



if __name__ == "__main__":
    app.run()
