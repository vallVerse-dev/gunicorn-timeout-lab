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
    return jsonify({"servicio": "api-compras", "instancia": INSTANCE_ID, "estado": "ok"}), 200


@app.route("/health")
def health():
    return jsonify({"status": "healthy", "instancia": INSTANCE_ID}), 200


@app.route("/comprar", methods=["POST"])
def procesar_compra():
    # El desarrollador agregó una llamada a un servicio externo de validación
    # de fraude. Este servicio externo hipotético tarda 4 segundos en responder.
    try:
        app.logger.info(
            "POST /comprar recibido instancia=%s (llamando a validacion de fraude)",
            INSTANCE_ID,
        )
        time.sleep(4)
        app.logger.info("Compra aprobada instancia=%s transaccion_id=9942", INSTANCE_ID)
        return {"status": "Aprobado", "transaccion_id": 9942}, 200
    except Exception as e:
        app.logger.error("Fallo en pasarela de pagos: %s", str(e))
        return {"error": "Servicio no disponible"}, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
