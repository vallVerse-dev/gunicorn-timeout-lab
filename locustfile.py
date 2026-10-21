from locust import HttpUser, between, task


class Comprador(HttpUser):
    wait_time = between(0.5, 1.5)

    @task
    def comprar(self):
        payload = {"producto_id": 1, "cantidad": 1, "metodo_pago": "tarjeta"}
        with self.client.post("/comprar", json=payload, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"HTTP {response.status_code}: {response.text[:120]}")
