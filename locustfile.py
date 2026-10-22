from locust import HttpUser, between, task


class Comprador(HttpUser):
    wait_time = between(0.5, 1.5)

    @task
    def aplicar_descuento(self):
        payload = {"cupon": "SRE-2026", "compra_id": 9942}
        with self.client.post(
            "/aplicar-descuento", json=payload, catch_response=True
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"HTTP {response.status_code}: {response.text[:120]}")
