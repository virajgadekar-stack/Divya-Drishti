from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# --- IN-MEMORY DATABASES ---
PRODUCT_DB = {
    "DATA-TRUST-101": {
        "status": "SAFE",
        "name": "Mahyco Cotton Seeds (Bt)",
        "message": "✅ GENUINE. Batch #MH-2025 verified.",
        "expiry": "Dec 2025"
    },
    "FAKE-PESTICIDE-99": {
        "status": "FAKE",
        "name": "Counterfeit / Unknown",
        "message": "❌ WARNING: Fake Product Detected!",
        "expiry": "N/A"
    }
}

FARMERS_DB = []

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    FARMERS_DB.append(data)
    print(f"🆕 NEW FARMER REGISTERED: {data['name']} from {data['village']}")
    return jsonify({"message": "Registration Successful", "status": "success"})

@app.route('/scan', methods=['POST'])
def scan():
    code = request.json.get('code')
    print(f"Scanned: {code}")
    data = PRODUCT_DB.get(code, {
        "status": "UNKNOWN",
        "name": "Unknown Product",
        "message": "⚠️ Product not found.",
        "expiry": "-"
    })
    return jsonify(data)

@app.route('/ask', methods=['POST'])
def ask():
    query = request.json.get('query', '').lower()
    if "yellow" in query or "leaf" in query:
        advice = "🍂 Diagnosis: Nitrogen Deficiency.\n👉 Remedy: Apply Urea (20kg/acre)."
    elif "price" in query:
        advice = "💰 Market Intelligence:\nGovt Rate: ₹266 per bag.\n⚠️ Alert: Do not pay more than ₹270."
    else:
        advice = "🙏 I am your Agri-Gyani.\nAsk about 'Yellow leaves' or 'Fertilizer Price'."
    return jsonify({"advice": advice})

if __name__ == '__main__':
    print("Divya Drishti Server Running...")
    app.run(port=5000, debug=True)