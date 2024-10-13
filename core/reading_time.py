import math

def get_reading_time(text):

    word_count = len(text.split()) # Split and Count
    #print(word_count)
    reading_time = math.ceil(word_count / 200) # average reading speed of 200 words per minute

    #print(f"Estimated reading time: {reading_time} minutes")

    return reading_time
def total_words(text):
    word_count = len(text.split())
    return word_count