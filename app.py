from flask import Flask, render_template, request
from core.summarize_text import get_summary
from core.reading_time import  get_reading_time,total_words

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        # Handle file upload or text paste
        
        text = request.form['text']

        original_text_word_count=total_words(text)
        reading_time_original_text=get_reading_time(text)

       # Summarize the text
        summary = get_summary(text)
        #print(summary)
        reading_time_summary=get_reading_time(summary)
        summary_text_word=total_words(summary)

        return render_template('index.html', summary=summary,original_total_words=original_text_word_count,original_reading_time=reading_time_original_text,summary_total_words=summary_text_word,summary_reading_time=reading_time_summary,original_text=text)

    

if __name__ == '__main__':
    app.run(debug=True)
