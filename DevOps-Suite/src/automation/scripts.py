import subprocess
import inspect

def run_git_clone(repo_url, destination):
    command = ["git", "clone", repo_url, destination]
    subprocess.run(command, check=True)

def run_docker_build(image_name, dockerfile_path):
    command = ["docker", "build", "-t", image_name, dockerfile_path]
    subprocess.run(command, check=True)

def run_docker_run(image_name, container_name):
    command = ["docker", "run", "--name", container_name, image_name]
    subprocess.run(command, check=True)

def run_git_push(project_path, commit_message, branch):
    subprocess.run(["git", "add", "."], check=True, cwd=project_path)
    subprocess.run(["git", "commit", "-m", commit_message], check=True, cwd=project_path)
    subprocess.run(["git", "push", "-u", "origin", branch], check=True, cwd=project_path)

def get_script_parameters(script_name):
    script_func = get_script_function(script_name)
    if script_func:
        return list(inspect.signature(script_func).parameters.keys())
    return []

def get_script_function(script_name):
    return globals().get(script_name)

def run_script(script_name, params):
    script_func = get_script_function(script_name)
    if script_func:
        script_func(**params)
