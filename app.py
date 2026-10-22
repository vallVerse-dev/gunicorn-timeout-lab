import logging
import os
import time

from flask import Flask, jsonify

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

INSTANCE_ID = os.getenv("INSTANCE_ID", "api-local")


@app.route("/")
def index():
    return jsonify({"servicio": "api-cupones", "instancia": INSTANCE_ID, "estado": "ok"}), 200


@app.route("/health")
def health():
    return "OK", 200


@app.route("/aplicar-descuento", methods=["POST"])
def aplicar_descuento():
    app.logger.info("POST /aplicar-descuento recibido instancia=%s", INSTANCE_ID)
    time.sleep(1.2)
    app.logger.info("Descuento aplicado instancia=%s", INSTANCE_ID)
    return {"status": "Descuento aplicado", "descuento": 15}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
