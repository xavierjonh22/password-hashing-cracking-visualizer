from flask import Flask, request, jsonify, render_template
from hashing.hasher import hash_all
from hashing.cracker import dictionary_cracker, crack_md5

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hash', methods=['POST'])
def hash_password():
    try:
        data = request.get_json()
        password = data['password']
        result = hash_all(password)
        return jsonify(result)
    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500
@app.route('/crack', methods=['POST'])
def crack_password():
    try:
        data = request.get_json()
        target_hash = data['target_hash']
        algorithm = data['algorithm']
        if algorithm == "argon2":
            result = dictionary_cracker(target_hash)
        elif algorithm == "md5":
            result = crack_md5(target_hash)
        print("Crack result:", result)
        return jsonify(result)

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


