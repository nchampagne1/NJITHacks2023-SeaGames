from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    # Run your Python script and capture its output
    output = subprocess.check_output(['python', 'C:\Users\JosephMChampagne\Desktop\try\JumpBob-NJITHacks2023'], text=True)

    # Render the HTML template and pass the Python script's output
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
