import subprocess

def run_binary(binary_name: str, args: list):
    result = subprocess.run([binary_name] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    error = result.stderr.decode('utf-8')
    if error is not None:
        raise Exception(error)
    return output, error
