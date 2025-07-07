from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def submit_name():
    if request.method == 'POST':
        name = request.form.get('name') or request.json.get('name')
        if not name:
            return jsonify({"error": "No name provided"}), 400

        return jsonify({"message": f"Hello, {name}! 🎉 You’ve just submitted your name."})

    return '''
        <form method="POST">
            <label>Enter your name:</label>
            <input name="name" />
            <input type="submit" />
        </form>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
