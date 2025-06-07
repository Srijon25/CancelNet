from sentence_transformers import SentenceTransformer, util

class CancelPhraseDetector:
    def __init__(self, cancel_phrases=None, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.cancel_phrases = cancel_phrases or []
        self.embeddings = self.model.encode(self.cancel_phrases, convert_to_tensor=True)

    def add_phrase(self, phrase):
        self.cancel_phrases.append(phrase)
        self.embeddings = self.model.encode(self.cancel_phrases, convert_to_tensor=True)

    def detect(self, input_text, threshold=0.7):
        input_embedding = self.model.encode(input_text, convert_to_tensor=True)
        scores = util.pytorch_cos_sim(input_embedding, self.embeddings)[0]
        best_score = float(scores.max())
        best_match = self.cancel_phrases[scores.argmax()] if best_score > threshold else None
        return best_match, best_score
