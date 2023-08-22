from difflib import SequenceMatcher



class TextUtils:
    THRESHOLD = 0.8
    
    def compute_similarity_percentage(self, a: str, b: str) -> float:
        """Compute similarity between two strings"""
        return SequenceMatcher(None, a, b).ratio()

    def is_similar(self, a: str, b: str, threshold: float = THRESHOLD) -> bool:
        """Check if two strings are similar"""
        return self.compute_similarity_percentage( a, b) > threshold