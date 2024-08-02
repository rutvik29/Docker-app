
from flask import Flask, request, render_template
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            data = pd.read_csv(file)
        else:
           
            pass

        model = LinearRegression()
        X = data[['feature1', 'feature2']]  
        y = data['target']  
        model.fit(X, y)
        predictions = model.predict(X)
        
        return render_template('results.html', predictions=predictions)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
