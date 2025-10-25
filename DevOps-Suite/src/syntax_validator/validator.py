import ast
import subprocess
import tempfile
import os

class SyntaxValidator:
    def validate_python(self, code):
        try:
            ast.parse(code)
            return True, None
        except SyntaxError as e:
            return False, str(e)

    def validate_csharp(self, code):
        with tempfile.NamedTemporaryFile(suffix=".cs", delete=False) as temp_file:
            temp_file.write(code.encode('utf-8'))
            temp_file_path = temp_file.name

        try:
            result = subprocess.run(["csc", "/nologo", "/out:" + os.devnull, temp_file_path], capture_output=True, text=True, check=True)
            return True, None
        except subprocess.CalledProcessError as e:
            return False, e.stderr
        except FileNotFoundError:
            return False, "csc.exe no encontrado. Asegúrate de que el SDK de .NET esté instalado y en el PATH."
        finally:
            os.remove(temp_file_path)

    def validate_java(self, code):
        with tempfile.NamedTemporaryFile(suffix=".java", delete=False) as temp_file:
            temp_file.write(code.encode('utf-8'))
            temp_file_path = temp_file.name

        try:
            result = subprocess.run(["javac", "-d", os.devnull, temp_file_path], capture_output=True, text=True, check=True)
            return True, None
        except subprocess.CalledProcessError as e:
            return False, e.stderr
        except FileNotFoundError:
            return False, "javac.exe no encontrado. Asegúrate de que el JDK esté instalado y en el PATH."
        finally:
            os.remove(temp_file_path)
