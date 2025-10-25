class CodeGenerator:
    def generate_singleton(self, class_name):
        return (
            f"class {class_name}:\n"
            f"    _instance = None\n"
            f"\n"
            f"    def __new__(cls, *args, **kwargs):\n"
            f"        if not cls._instance:\n"
            f"            cls._instance = super({class_name}, cls).__new__(cls, *args, **kwargs)\n"
            f"        return cls._instance\n"
        )
