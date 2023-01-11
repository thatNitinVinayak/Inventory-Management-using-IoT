from flask import Flask, render_template
import pickle

recommendation_df = pickle.load(open('recommendation.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           )
    
if __name__ == '__main__':
    app.run(debug = True)