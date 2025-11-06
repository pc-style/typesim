"""
Core typing engine with realistic human-like behavior.
Handles typos, corrections, pauses, and mid-sentence edits.
"""

import random
import time
from . import config
from . import keyboard_ctrl
from . import gemini_helper
from . import shortcuts

def wait_for_resume():
    """Wait while paused."""
    while shortcuts.is_paused() and not shortcuts.is_stopped():
        time.sleep(0.1)

def thinking_pause(min_ms: int = None, max_ms: int = None):
    """Pause for thinking - longer delay."""
    if min_ms is None:
        min_ms = config.THINKING_PAUSE_MIN()
    if max_ms is None:
        max_ms = config.THINKING_PAUSE_MAX()
    
    delay = config.random_delay(min_ms, max_ms)
    # apply speed multiplier
    delay /= shortcuts.get_speed_multiplier()
    time.sleep(delay)
    wait_for_resume()

def base_delay():
    """Normal delay between keystrokes."""
    delay = config.random_delay(config.BASE_DELAY_MIN(), config.BASE_DELAY_MAX())
    # apply speed multiplier
    delay /= shortcuts.get_speed_multiplier()
    time.sleep(delay)
    wait_for_resume()

def simulate_typo(char: str) -> tuple[str, bool]:
    """
    Simulate a typo by hitting a neighboring key.
    Returns (typed_char, was_typo)
    """
    if not config.should_make_typo():
        return char, False
    
    # get a neighbor key for typo
    neighbor = config.get_neighbor_key(char)
    if neighbor:
        return neighbor, True
    
    # fallback: just return original if no neighbor found
    return char, False

def backspace_and_fix(original: str):
    """Backspace and retype correctly."""
    # backspace the wrong chars
    keyboard_ctrl.press_backspace(len(original))
    base_delay()
    
    # retype correctly
    for c in original:
        keyboard_ctrl.type_char(c)
        base_delay()

def find_sentence_boundaries(text: str, position: int) -> tuple[int, int]:
    """
    Find sentence boundaries around position.
    Returns (sentence_start, sentence_end).
    """
    # look for sentence end markers
    sentence_end_chars = '.!?'
    
    # find previous sentence end
    start = 0
    for i in range(position - 1, -1, -1):
        if text[i] in sentence_end_chars:
            start = i + 1
            # skip whitespace
            while start < len(text) and text[start] in ' \n\t':
                start += 1
            break
    
    # find next sentence end
    end = len(text)
    for i in range(position, len(text)):
        if text[i] in sentence_end_chars:
            end = i + 1
            break
    
    return start, end

def rephrase_and_type_sentence(text: str, start: int, end: int, current_position: int, rephrased_sentences: set) -> int:
    """
    Type a rephrased version of a sentence (or part of it), then change it back to original.
    Only does this ONCE per sentence to avoid loops.
    current_position is where we are in typing (may be different from end if we've typed past it).
    Returns new position - the position we should continue typing from.
    """
    # get the actual text that was already typed (up to current_position)
    original_sentence = text[start:end].strip()
    
    if len(original_sentence) < 10:
        return current_position  # skip very short sentences
    
    # get rephrased version from gemini (if AI enabled)
    if not config.USE_AI():
        return current_position
    
    # only rephrase a small part (5-10 words max) to keep it manageable
    words = original_sentence.split()
    if len(words) < 3:
        return current_position  # too short
    
    # pick a random portion (3-8 words)
    max_words = min(8, len(words))
    num_words = random.randint(3, max_words)
    
    # pick starting position
    if len(words) <= num_words:
        # use all words
        selected_words = words
        word_start_idx = 0
    else:
        # pick random starting point
        word_start_idx = random.randint(0, len(words) - num_words)
        selected_words = words[word_start_idx:word_start_idx + num_words]
    
    text_to_rephrase = ' '.join(selected_words)
    
    # find character position in original text
    # reconstruct text up to this point
    prefix_words = ' '.join(words[:word_start_idx])
    if prefix_words:
        rephrase_char_start = start + len(prefix_words) + 1  # +1 for space
    else:
        rephrase_char_start = start
    
    rephrased = gemini_helper.rephrase_sentence(text_to_rephrase)
    
    if rephrased == text_to_rephrase or len(rephrased) < 3:
        return current_position  # skip if rephrasing failed or too short
    
    # backspace from current position to start of rephrase section
    if current_position <= rephrase_char_start:
        return current_position  # haven't typed this part yet
    
    chars_to_backspace = current_position - rephrase_char_start
    keyboard_ctrl.press_backspace(chars_to_backspace)
    thinking_pause(300, 600)  # pause while "thinking"
    
    # type rephrased version
    for c in rephrased:
        keyboard_ctrl.type_char(c)
        base_delay()
    
    thinking_pause(500, 1200)  # longer pause - "thinking about it"
    
    # backspace rephrased version
    keyboard_ctrl.press_backspace(len(rephrased))
    thinking_pause(200, 500)
    
    # type original version (just the part we rephrased)
    for c in text_to_rephrase:
        keyboard_ctrl.type_char(c)
        base_delay()
    
    # return position after the rephrased text
    return rephrase_char_start + len(text_to_rephrase)

def insert_random_edit(text: str, position: int, rephrased_sentences: set) -> int:
    """
    Go back and make an edit - change a word, insert something, or rephrase sentence.
    Returns new position after edit.
    """
    # decide: small edit (word level) or big edit (sentence rephrase)
    # use configurable probability for sentence rephrase
    if config.should_rephrase_sentence() and position > 50:
        # go much further back - find a sentence to rephrase
        lookback_start = max(0, position - random.randint(50, min(200, position)))
        sentence_start, sentence_end = find_sentence_boundaries(text, lookback_start)
        
        # check if this sentence was already rephrased
        sentence_key = (sentence_start, sentence_end)
        if sentence_end > lookback_start and sentence_end <= position and sentence_key not in rephrased_sentences:
            # mark as rephrased before doing it
            rephrased_sentences.add(sentence_key)
            # found a sentence to rephrase - only rephrase part of it sometimes
            return rephrase_and_type_sentence(text, sentence_start, sentence_end, position, rephrased_sentences)
    
    # regular word-level edit - go back further sometimes
    lookback_range = random.choice([
        (0, 20),      # nearby
        (20, 50),     # medium
        (50, 150),    # far back
    ])
    start = max(0, position - random.randint(lookback_range[0], lookback_range[1]))
    segment = text[start:position]
    
    # find last word boundary
    last_space = segment.rfind(' ')
    if last_space == -1:
        edit_start = start
    else:
        edit_start = start + last_space + 1
    
    word_to_edit = text[edit_start:position]
    
    if not word_to_edit or len(word_to_edit) < 2:
        return position  # skip if nothing to edit
    
    # backspace to the start of the word
    chars_to_backspace = position - edit_start
    keyboard_ctrl.press_backspace(chars_to_backspace)
    thinking_pause(100, 300)  # brief pause while "thinking"
    
    # decide: change word or insert something
    action = random.choice(['change', 'insert', 'improve'])
    
    if action == 'change' and len(word_to_edit) > 3:
        # try to get similar words from gemini (if AI enabled)
        similar_words = []
        if config.USE_AI():
            similar_words = gemini_helper.get_similar_words(word_to_edit, count=3)
        
        if similar_words and random.random() < 0.6:
            # use gemini suggestion
            new_word = random.choice(similar_words)
        else:
            # fallback to typo-based change
            new_word = word_to_edit
            if random.random() < 0.5:
                idx = random.randint(0, len(new_word) - 1)
                neighbor = config.get_neighbor_key(new_word[idx])
                if neighbor:
                    new_word = new_word[:idx] + neighbor + new_word[idx+1:]
        
        # type the changed word
        for c in new_word:
            keyboard_ctrl.type_char(c)
            base_delay()
        
        # then backspace and fix it
        thinking_pause(200, 500)
        keyboard_ctrl.press_backspace(len(new_word))
        thinking_pause(100, 300)
        
        # retype original correctly
        for c in word_to_edit:
            keyboard_ctrl.type_char(c)
            base_delay()
        
        return edit_start + len(word_to_edit)
    
    elif action == 'insert':
        # get varied insertion words from gemini (if AI enabled)
        insertions_list = []
        if config.USE_AI():
            insertions_list = gemini_helper.get_insertion_words()
        if not insertions_list:
            # fallback
            insertions_list = [' actually', ' really', ' kind of', ' sort of', ' I mean', ' well', ' like', ' you know', ' perhaps', ' maybe']
        
        chosen = random.choice(insertions_list)
        insertion = ' ' + chosen if not chosen.startswith(' ') else chosen
        
        for c in insertion:
            keyboard_ctrl.type_char(c)
            base_delay()
        
        thinking_pause(300, 700)
        
        # delete the insertion
        keyboard_ctrl.press_backspace(len(insertion))
        thinking_pause(100, 300)
        
        # retype original word
        for c in word_to_edit:
            keyboard_ctrl.type_char(c)
            base_delay()
        
        return edit_start + len(word_to_edit)
    
    else:  # improve
        # type word, then improve it
        for c in word_to_edit:
            keyboard_ctrl.type_char(c)
            base_delay()
        
        thinking_pause(200, 600)
        
        # maybe add something after
        if random.random() < 0.3:
            additions = ['er', 'ly', 'ing']
            addition = random.choice(additions)
            for c in addition:
                keyboard_ctrl.type_char(c)
                base_delay()
            
            thinking_pause(200, 500)
            keyboard_ctrl.press_backspace(len(addition))
            thinking_pause(100, 300)
        
        return edit_start + len(word_to_edit)

def type_text_realistic(text: str):
    """
    Main function: type text with realistic human behavior.
    """
    i = 0
    last_word_end = 0
    # track which sentences have been rephrased to avoid loops
    rephrased_sentences = set()
    
    while i < len(text) and not keyboard_ctrl.is_stopped() and not shortcuts.is_stopped():
        char = text[i]
        
        # check if we should make an edit (after finishing a word)
        if char in ' \n\t' and i > last_word_end + 3:
            if config.should_edit() and i < len(text) - 5:
                # go back and edit something
                new_i = insert_random_edit(text, i, rephrased_sentences)
                # if we moved backward (did an edit), continue from there
                if new_i < i:
                    i = new_i
                    # don't update last_word_end, we're going back
                    continue
                # if position didn't change, skip the edit and continue normally
                elif new_i == i:
                    pass  # fall through to normal typing
                else:
                    # moved forward after edit, continue from new position
                    i = new_i
                    last_word_end = i
                    continue
        
        # simulate typo
        typed_char, was_typo = simulate_typo(char)
        keyboard_ctrl.type_char(typed_char)
        
        if was_typo:
            # brief pause, then correct
            base_delay()
            thinking_pause(150, 400)
            backspace_and_fix(char)
            i += 1
            if char in ' \n\t':
                last_word_end = i
            continue
        
        # normal typing delay
        base_delay()
        
        # special pauses for punctuation
        if char == '.' or char == '!' or char == '?':
            # sentence end - longer pause
            thinking_pause(config.SENTENCE_PAUSE_MIN(), config.SENTENCE_PAUSE_MAX())
        elif char == ',' or char == ';':
            # comma/semicolon pause
            thinking_pause(config.COMMA_PAUSE_MIN(), config.COMMA_PAUSE_MAX())
        elif char == '\n':
            # paragraph break - even longer pause
            thinking_pause(config.SENTENCE_PAUSE_MIN() * 2, config.SENTENCE_PAUSE_MAX() * 2)
        
        i += 1
        if char in ' \n\t':
            last_word_end = i

