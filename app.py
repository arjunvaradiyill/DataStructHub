from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stacks', methods=['GET', 'POST'])
def stacks():
    return render_template('stacks.html')

@app.route('/queues', methods=['GET', 'POST'])
def queues():
    return render_template('queues.html')

@app.route('/trees', methods=['GET', 'POST'])
def trees():
    return render_template('trees.html')

@app.route('/graphs', methods=['GET', 'POST'])
def graphs():
    return render_template('graphs.html')

@app.route('/arrays', methods=['POST'])
def arrays():
    array_data = request.form.get('array').split(',')
    operation = request.form.get('operation')
    if operation == 'search':
        key = request.form.get('key')
        result = key in array_data
    elif operation == 'sort':
        result = sorted(array_data)
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
