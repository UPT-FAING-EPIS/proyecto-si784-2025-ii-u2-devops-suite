class HardwareCalculator:
    def calculate_requirements(self, app_type, user_load):
        # Lógica de cálculo simple
        if app_type == "Web App":
            cpu = user_load / 100
            ram = user_load / 50
            disk = user_load / 10
        elif app_type == "Database":
            cpu = user_load / 50
            ram = user_load / 20
            disk = user_load / 5
        else:
            cpu = user_load / 200
            ram = user_load / 100
            disk = user_load / 20

        return {
            "cpu": f"{cpu:.2f} Cores",
            "ram": f"{ram:.2f} GB",
            "disk": f"{disk:.2f} GB"
        }
