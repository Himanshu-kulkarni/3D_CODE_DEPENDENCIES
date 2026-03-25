import sample_code.utils as utils

def predict(data):
    utils.log("Running prediction")
    return len(data)

def train(dataset):
    utils.log("Training model")
    return {"weights": [0.1, 0.2, 0.3]}

def evaluate(model, test_data):
    score = predict(test_data)
    return score

def save_model(model, path):
    utils.log(f"Saving to {path}")
