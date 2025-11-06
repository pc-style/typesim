"""
Gemini API helper for getting synonyms and rephrasing sentences.
"""

import os
from google import genai
from google.genai import types

# global client instance
_gemini_client = None

def get_client():
    """Get or create Gemini client."""
    global _gemini_client
    if _gemini_client is None:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set")
        _gemini_client = genai.Client(api_key=api_key)
    return _gemini_client

def get_similar_words(word: str, count: int = 5) -> list[str]:
    """
    Get similar meaning words/synonyms for a word.
    Returns list of alternative words.
    """
    try:
        client = get_client()
        prompt = f"""Give me {count} alternative words or synonyms for "{word}" that have similar meaning.
Return ONLY a comma-separated list of words, nothing else. No explanations, no numbers, just words separated by commas.
Example format: word1, word2, word3"""
        
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=prompt,
            config=types.GenerateContentConfig(temperature=0.7)
        )
        
        result = response.text.strip()
        # parse comma-separated words
        words = [w.strip() for w in result.split(',')]
        # filter out empty and keep only reasonable length words
        words = [w for w in words if w and len(w) < 20 and w.isalpha()]
        return words[:count]
    
    except Exception as e:
        # fallback to empty list if API fails
        print(f"// gemini error getting synonyms: {e}")
        return []

def rephrase_sentence(sentence: str) -> str:
    """
    Rephrase a sentence to have similar meaning but different wording.
    Returns the rephrased version.
    """
    try:
        client = get_client()
        prompt = f"""Rephrase this sentence to have the same meaning but different wording. 
Keep it natural and human-like. Return ONLY the rephrased sentence, nothing else.

Original: {sentence}"""
        
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=prompt,
            config=types.GenerateContentConfig(temperature=0.8)
        )
        
        result = response.text.strip()
        # clean up any quotes or extra formatting
        result = result.strip('"').strip("'").strip()
        return result
    
    except Exception as e:
        # fallback to original if API fails
        print(f"// gemini error rephrasing: {e}")
        return sentence

def get_insertion_words(context: str = "") -> list[str]:
    """
    Get varied insertion words/phrases based on context.
    Returns list of words/phrases that could be inserted.
    """
    try:
        client = get_client()
        prompt = f"""Give me 10 short filler words or phrases (1-3 words each) that someone might type while thinking, then delete.
Examples: "actually", "really", "kind of", "sort of", "I mean", "well", "hmm", "like", "you know"
Return ONLY a comma-separated list, nothing else."""
        
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=prompt,
            config=types.GenerateContentConfig(temperature=0.9)
        )
        
        result = response.text.strip()
        words = [w.strip() for w in result.split(',')]
        words = [w for w in words if w and len(w) < 25]
        return words[:10]
    
    except Exception as e:
        # fallback to varied list if API fails
        print(f"// gemini error getting insertions: {e}")
        return ['actually', 'really', 'kind of', 'sort of', 'I mean', 'well', 'like', 'you know', 'perhaps', 'maybe']

