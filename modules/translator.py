# Translator for translatting bad words to english if they are contained in sentence
from deep_translator import GoogleTranslator
from googletrans import Translator
from config import default_language


class TranslateText:
    """Class of translator for text
    
    Args:
        text (str): Text for translation

    Returns:
        str: Translated text
    """
    def __init__(self, text) -> str:        
        self.translator = Translator()
        self.text = text
        self.src = self._detect()
        
    def _detect(self) -> str:
        try:
            return self.translator.detect(self.text).lang
        
        except:
            return default_language

    def translate(self) -> str:
        if self.src == 'en':
            return self.text
        
        try:
            translated = GoogleTranslator(source=self.src, target='en').translate(self.text)
            return translated
        
        except Exception as e:
            print("Error occured while translating: %s" % e)