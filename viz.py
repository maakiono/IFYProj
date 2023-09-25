from flask import Flask, render_template, request, jsonify
from classifier_model.modlib import *
import os

model = Classifier()
template_dir = "web/templates"
static_dir = "web/static"
app = Flask(__name__,template_folder=template_dir,static_folder=static_dir)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'classify':
            text = request.form['text']
            categories = classify_text(text)
            return jsonify({'categories': categories})
        elif action == 'random':
            random_text = random_classify()  
            return jsonify({'random_text': random_text})
    return render_template('index.html')

def random_classify():
    return classify_text(model.random_message())

def classify_text(text):
    lis = list(str(pd.Series(model.classifyraw(text),index=model.categories)).replace("0","❌").replace("1","✅").split("\n")[:-1])
    lisf= sorted(lis, key=lambda x: x.endswith("✅"))[:9:-1]
    lisf.insert(0,f"'{text}'")
    return lisf

if __name__ == '__main__':
    app.run(debug=True)
