class Deployer:
    def deploy(self, provider, config):
        print(f"Desplegando en {provider} con la siguiente configuración:")
        for key, value in config.items():
            print(f"  {key}: {value}")
        print("Despliegue iniciado.")
