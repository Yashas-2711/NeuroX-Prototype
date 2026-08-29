from pathlib import Path
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

MODEL_PATH = Path(__file__).resolve().parents[2] / "model" / "neurox-classifier"
_tokenizer = None
_model = None


def _load_model():
    global _tokenizer, _model
    if _model is None:
        _tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, local_files_only=True)
        _model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH, local_files_only=True)
        _model.eval()
    return _tokenizer, _model


def classify_challenge(text: str) -> dict:
    tokenizer, model = _load_model()
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
    with torch.no_grad():
        probabilities = torch.softmax(model(**inputs).logits, dim=-1)[0]
    index = int(torch.argmax(probabilities).item())
    label = model.config.id2label.get(index, model.config.id2label.get(str(index), "other"))
    return {"category": label, "confidence": round(float(probabilities[index]), 4)}
