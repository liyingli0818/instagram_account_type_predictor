from flask import Flask, render_template
from src.DataPreparation import get_one_user_df, get_pred_one
import pickle


#url = instagram.com/username
loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
#prediction = get_pred_one(url, loaded_model)




app = Flask(__name__, static_url_path='')



@app.route("/")
def Homepage():
    return render_template('index.html', pred =20)

@app.route('/predict_account_type/<username>', methods=['GET'])
def predict_account_type(username):
    url = 'http://instagram.com/%s' % username
    prediction = str(get_pred_one(url, loaded_model)[0])
    return prediction



if __name__ == '__main__':
    app.run(debug=True)

