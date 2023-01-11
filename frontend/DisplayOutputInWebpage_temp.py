from flask import Flask,render_template,request
import pickle
import numpy as np

items = pickle.load(open('recommendation.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
products = pickle.load(open('products.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           ProductName = list(items['Product-Name'].values),
                           ProductBrand=list(items['Brand'].values),
                           ProductImage=list(items['ProductImage'].values),
                           ProductProductAverageRatingss=list(items['ProductAverageRatingss'].values),
                           ProductAverageRatings=list(items['avgProductAverageRatings'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_products',methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = products[products['Product-Name'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Product-Name')['Product-Name'].values))
        item.extend(list(temp_df.drop_duplicates('Product-Name')['Brand'].values))
        item.extend(list(temp_df.drop_duplicates('Product-Name')['ProductImage-URL-M'].values))

        data.append(item)

    print(data)

    return render_template('recommend.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)