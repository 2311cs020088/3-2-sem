import nltk
from collections import Counter
word_count = {
    "the": 1000,
    "tea": 50,
    "ten": 30,
    "team": 20,
    "that": 500
}
total_words = sum(word_count.values())
def prior(candidate):
    return word_count.get(candidate, 0) / total_words
def likelihood(word, candidate):
    distance = nltk.edit_distance(word, candidate)
    if distance == 0:
        return 0.1
    return 1 / (10 ** distance)
def suggested(word):
    candidates = word_count.keys()
    best_candidate = None
    max_prob = -1
    for candidate in candidates:
        prob = likelihood(word, candidate) * prior(candidate)
        if prob > max_prob:
            max_prob = prob
            best_candidate = candidate
    return best_candidate
wrong_input = "teama"
correction = suggested(wrong_input)
print(f"Suggested correction for '{wrong_input}': {correction}")