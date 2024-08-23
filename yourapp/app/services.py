import requests

class APIService:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_vaccination_data(self):
        """Obtiene los datos de vacunación desde la API REST."""
        response = requests.get(f"{self.base_url}/vaccinations")
        response.raise_for_status()  # Lanza una excepción para respuestas erróneas
        return response.json()

    def get_vaccination_by_year(self, year):
        """Obtiene los datos de vacunación por año."""
        response = requests.get(f"{self.base_url}/vaccinations/{year}")
        response.raise_for_status()
        return response.json()
