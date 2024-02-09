from flask import Flask, request, render_template, url_for
from french import load_model, translate_text

app = Flask(__name__)

# Load the model and tokenizer once when the app starts
model_name = "Helsinki-NLP/opus-mt-fr-en"
model, tokenizer = load_model(model_name)

@app.route('/', methods=['GET', 'POST'])
def home():
    translation = ''
    audio_file = None
    if request.method == 'POST':
        text = request.form.get('text')
        translation, audio_file = translate_text(model, tokenizer, text)
    return render_template('index.html', translation=translation, audio_file=audio_file)

if __name__ == '__main__':
    app.run(debug=True)