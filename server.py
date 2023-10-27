from flask import Flask, render_template, request
import spacy

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    prompt = request.form['prompt']
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(prompt)
    concepts = []
    for token in doc:
        if token.pos_ == 'NOUN':
            concepts.append(token.text)
    return render_template('results.html', concepts=concepts)

if __name__ == '__main__':
    app.run(debug=True)