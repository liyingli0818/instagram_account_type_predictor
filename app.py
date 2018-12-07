from flask import Flask, render_template
from src.DataPreparation import get_one_user_df, get_pred_one
import pickle



#loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
#prediction = get_pred_one(url, loaded_model)




app = Flask(__name__)

@app.route("/")
def Homepage():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, pred = 20)

