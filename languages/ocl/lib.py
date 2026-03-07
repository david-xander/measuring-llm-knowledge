import re

def get_cleaned_valid_text_according_to_keywords(text, keywords):
    if not (text.startswith("\'") or text.startswith("\"")):
        if text in keywords:                
            return text
        else:                
            cleaned_token = re.sub('[^a-zA-Z]+', '', text)
            if cleaned_token in keywords:                
                return cleaned_token
            else:
                return None
    else:
        return None
