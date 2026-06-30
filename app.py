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

        results = {}
        for i, tweet in enumerate(data):
            # Logique temporaire : scores basiques entre -1 et 1
            # (Sera remplacé par le modèle de Machine Learning plus tard)
            score = (len(tweet) % 3) - 1 # donne -1, 0, ou 1
            results[f"tweet{i+1}"] = score

        return jsonify(results), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
