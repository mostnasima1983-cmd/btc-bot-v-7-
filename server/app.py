from flask import Flask, jsonify
import os
app = Flask(__name__)

CONFIG = {
    "symbol": "PAXGUSDT",
    "leverage": 10,
    "tp": 0.6,
    "sl": 0.4,
    "rr": "1:1.5",
    "min_score": 6,
    "order": "LIMIT_MAKER_POST_ONLY",
    "fee": 0.051
}

@app.route('/')
def home():
    return jsonify({"status":"GOLD BOT LIVE - 10x Fixed","config":CONFIG})

@app.route('/health')
def health():
    return jsonify({"status":"ok","balance":"$5","leverage":10})

@app.route('/signal')
def signal():
    return jsonify({
        "bias":"bullish",
        "entry":4025.5,
        "sl":4009.4,
        "tp":4049.6,
        "score":7,
        "action":"BUY_LIMIT",
        "quantity":0.01125
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT",10000)))
