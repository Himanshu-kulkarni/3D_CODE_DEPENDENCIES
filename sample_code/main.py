import sample_code.utils as utils
import models

def fetch_data(source):
    raw = utils.load(source)
    return raw

def process(data):
    cleaned = utils.clean(data)
    result = models.predict(cleaned)
    return result

def run_pipeline(source):
    data = fetch_data(source)
    return process(data)
