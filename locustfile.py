from locust import HttpUser, task, between

class BibliotecaUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def listar_livros(self):
        self.client.get("/books")