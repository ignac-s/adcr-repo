from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1.0/predict')
def predict():
    # Pobierz parametry 'num1' i 'num2' z query stringa
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
    except (TypeError, ValueError):
        return jsonify({"error": "wprowadz num1 i num2."}), 400
    
    # Suma liczb
    total = num1 + num2
    
    # Reguła decyzyjna: jeśli suma jest większa niż 5.8, zwróć 1, w przeciwnym razie 0
    prediction = 1 if total > 5.8 else 0
    
    # Zwróć odpowiedź w formacie JSON
    return jsonify({
        "prediction": prediction,
        "features": {
            "num1": num1,
            "num2": num2
        }
    })

if __name__ == '__main__':
    app.run()
