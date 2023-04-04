# from jinja2 import Environment

# def intcomma(value):
#     return f"{value:,}"

# env = Environment()
# env.filters['intcomma'] = intcomma
#=========above is under test===

from flask import Flask, render_template, request
from data_functions import top_5_districts
app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    # Get the user input from the HTML form
    input_data = request.form['input_data']
    
    # Call the Python function and get the result
    result = top_5_districts(input_data)
    
    # Pass the result to the HTML template and render it
    return render_template('result.html', result=result)
 #======this was test========
#def top_5_districts(input_data):
    # Add your Python function code here
   # square = pow(5, 2)
    #return(square)
 #======this was test========

if __name__ == '__main__':
    app.run(debug=True)
