import glob
import os
from flask import Flask, request, render_template
from french import translate_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    translation = ''
    latest_audio_file = None
    if request.method == 'POST':
        text = request.form.get('text')
        translation, audio_file = translate_text(text)

        # Only get the latest audio file if there is a translation
        if translation:
            latest_audio_file = os.path.basename(audio_file)

    return render_template('index.html', translation=translation, latest_audio_file=latest_audio_file)

if __name__ == '__main__':
    app.run(debug=True)