from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/symptoms', methods=['GET'])
def get_symptoms():
    return jsonify({"message": "API is working!"})

if __name__ == '__main__':
    app.run(debug=True)
