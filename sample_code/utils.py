def load(source):
    with open(source) as f:
        return f.read()

def clean(data):
    return data.strip().lower()

def format_output(result):
    return f"Result: {result}"

def log(message):
    print(f"[LOG] {message}")
