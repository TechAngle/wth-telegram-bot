from jellyfish import jaro_similarity
from jellyfish import levenshtein_distance
from jellyfish import damerau_levenshtein_distance

from config import custom_words, profanity_percent

class StrDistance:
    def __init__(self, text: str):
        """Compute distance between text and custom profinity words

        Args:
            text (str): Text with potential profinity words
        """
        self.text = text
        self.text_words = self.text.lower().split()
        
    @staticmethod
    def arithmetic_mean(input: list[float | int]) -> float:
        if len(input) <= 0:
            return 0
        return sum(input)/len(input)
        
    def jaro(self) -> float:
        """Using Jaro string distance method

        Returns:
            float: arithmetic mean of all similarities (in percents)
        """
        similarities: list[float | int] = []
        for input_word in self.text_words:
            for profanity_word in custom_words:
                jaro_dist = jaro_similarity(input_word.lower(), profanity_word.lower())
                if jaro_dist is not None and jaro_dist*100 >= profanity_percent:
                    similarities.append(jaro_dist)
                    break

        if similarities:
            return self.arithmetic_mean(similarities) * 100
        else:
            return 0  # No valid similarities found
    
    def levenshtein(self) -> float:
        """Using Levenshtein string distance method

        Returns:
            float: arithmetic mean of all similarities (in percents)
        """
        similarities: list[float | int] = []
        
        for input_word in self.text_words:
            for profanity_word in custom_words:
                lev_dist = levenshtein_distance(input_word.lower(), profanity_word.lower())
                if lev_dist is not None:
                    similarities.append(lev_dist)
                    break

        if similarities:
            return self.arithmetic_mean(similarities) * 10
        else:
            return 0  # No valid similarities found

    def dameru_levenshtein(self) -> float:
        """Using Damerau-Levenshtein string distance method

        Returns:
            float: arithmetic mean of all similarities (in percents)
        """
        similarities: list[float | int] = []
        
        for input_word in self.text_words:
            for profanity_word in custom_words:
                lev_dist = damerau_levenshtein_distance(input_word.lower(), profanity_word.lower())
                if lev_dist is not None:
                    similarities.append(lev_dist)
                    break

        if similarities:
            return self.arithmetic_mean(similarities) * 10
        else:
            return 0  # No valid similarities found

    
    def compute(self) -> float:
        """Computing distance with using different algorithms for string distance

        Returns:
            float: In percentages
        """
        _jaro: float = self.jaro()
        _levenshtein: float = self.levenshtein()
        _damerau_levenshtein: float = self.dameru_levenshtein()
        
        _list: list[float] = [_jaro, _levenshtein, _damerau_levenshtein]
        
        valid_scores = [score for score in _list if score is not None]
        
        if valid_scores:
            max_valid_score = max(valid_scores)
            return max_valid_score  # Return the maximum valid score
        else:
            return 0  # No valid similarity score found, return a default value


