import pyautogui
import time
import random

def type_text(text, min_delay=0.05, max_delay=0.1):
    words = text.split()
    typos_to_correct = []
    
    for i, word in enumerate(words):
        # Decide if this word will have a typo
        if random.random() < 0.1:
            original_word = word
            typo_chance = random.random()

            if typo_chance < 0.1:
                # Replace one letter
                index_to_replace = random.randint(0, len(word) - 1)
                typo_char = random.choice('asdfghjkl')
                word = word[:index_to_replace] + typo_char + word[index_to_replace + 1:]

            elif typo_chance < 0.2:
                # Replace two letters
                indices_to_replace = random.sample(range(len(word)), min(2, len(word)))
                for index in indices_to_replace:
                    typo_char = random.choice('asdfghjkl')
                    word = word[:index] + typo_char + word[index + 1:]

            elif typo_chance < 0.3:
                # Replace three letters
                indices_to_replace = random.sample(range(len(word)), min(3, len(word)))
                for index in indices_to_replace:
                    typo_char = random.choice('asdfghjkl')
                    word = word[:index] + typo_char + word[index + 1:]

            elif typo_chance < 0.8:
                # Add extra letters
                extra_chars = ''.join(random.choices('asdfghjkl', k=random.randint(1, 3)))
                insertion_point = random.randint(0, len(word))
                word = word[:insertion_point] + extra_chars + word[insertion_point:]

            # Add typo information for later correction
            typos_to_correct.append((i, original_word))

        # Type the word (with or without typo)
        for char in word:
            pyautogui.write(char)
            time.sleep(random.uniform(min_delay, max_delay))
        pyautogui.write(' ')
        time.sleep(random.uniform(min_delay, max_delay))

        # Correct the typo based on the probability
        if typos_to_correct and random.random() < 0.6:
            typo_index, correct_word = typos_to_correct.pop(0)
            if typo_index == i - 1:
                pyautogui.write('\b' * len(word))  # Remove the previous word
                for char in correct_word:
                    pyautogui.write(char)
                    time.sleep(random.uniform(min_delay, max_delay))
                pyautogui.write(' ')
                time.sleep(random.uniform(min_delay, max_delay))

    # Correct remaining typos at the end of the sentence
    for typo_index, correct_word in typos_to_correct:
        pyautogui.write('\b' * len(words[typo_index]))  # Remove the incorrect word
        for char in correct_word:
            pyautogui.write(char)
            time.sleep(random.uniform(min_delay, max_delay))
        pyautogui.write(' ')
        time.sleep(random.uniform(min_delay, max_delay))

time.sleep(5)  # Delay before starting to type
text_to_type = "In the end, while there are challenges to being an outsider, it plays a big part in helping people grow, become strong, and think creatively, making it a really important part of the human experience."
type_text(text_to_type)
