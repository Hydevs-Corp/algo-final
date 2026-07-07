from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        # Vérifier si le corps de la requête est en JSON
        if not request.is_json:
            return jsonify({"error": "Le format de la requête doit être JSON"}), 400

        data = request.get_json()

        # Vérifier si on a bien reçu une liste de chaînes de caractères
        if not isinstance(data, list) or not all(isinstance(item, str) for item in data):
            return jsonify({"error": "L'endpoint attend une liste de chaînes de caractères"}), 400

        if not data:
            return jsonify({"error": "La liste des tweets est vide"}), 400

        # pyrefly: ignore [missing-import]
        import joblib
        import os

        model = None
        model_path = os.path.join(os.path.dirname(__file__), 'sentiment_model.pkl')
        if os.path.exists(model_path):
            model = joblib.load(model_path)

        results = {}
        for i, tweet in enumerate(data):
            if model:
                # Predict probabilities
                proba = model.predict_proba([tweet])[0]
                # Assuming classes are [-1, 1]
                classes = list(model.classes_)
                if 1 in classes and -1 in classes:
                    prob_pos = proba[classes.index(1)]
                    prob_neg = proba[classes.index(-1)]
                    score = prob_pos - prob_neg # Score between -1 and 1
                else:
                    # Fallback if only one class was learned
                    pred = model.predict([tweet])[0]
                    score = float(pred)
            else:
                score = 0.0 # Default if no model
            
            # Format the score to 2 decimal places or keep it raw
            results[f"tweet{i+1}"] = round(score, 4)

        return jsonify(results), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
