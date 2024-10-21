import os
from collections import Counter
import re
import socket
import string

# Dictionary of contractions and their expanded forms
contractions_dict = {
    "can't": "cannot", "won't": "will not", "n't": " not", "'re": " are", "'s": " is",
    "'d": " would", "'ll": " will", "'ve": " have", "'m": " am", "it's": "it is",
    "he's": "he is", "she's": "she is", "i'm": "i am", "they're": "they are",
    "we're": "we are", "you've": "you have", "i've": "i have", "you'll": "you will",
    "i'll": "i will", "there's": "there is", "that's": "that is"
}

# Read files
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Function to expand contractions
def expand_contractions(text):
    # Replace contractions using the contractions_dict
    for contraction, expanded in contractions_dict.items():
        text = re.sub(r"\b" + re.escape(contraction) + r"\b", expanded, text)
    return text

# Preprocess text: remove punctuation, replace dashes, and convert to lowercase
def preprocess_text(text):
    # Replace dashes (— and -) with spaces
    text = text.replace("—", " ").replace("-", " ")
    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    return text

# Count words
def word_count(text):
    words = re.findall(r"\b\w+\b", text)
    return words

# Get the top N frequent words
def get_top_words(words, top_n=3):
    return Counter(words).most_common(top_n)

# Get machine IP address
def get_ip_address():
    return socket.gethostbyname(socket.gethostname())

# Main function
if __name__ == "__main__":
    # File paths
    file1 = '/home/data/IF.txt'
    file2 = '/home/data/AlwaysRememberUsThisWay.txt'

    # Read files
    file1_content = read_file(file1)
    file2_content = read_file(file2)

    # Expand contractions and preprocess text
    file1_content = expand_contractions(file1_content)
    file2_content = expand_contractions(file2_content)

    file1_words = preprocess_text(file1_content).split()
    file2_words = preprocess_text(file2_content).split()

    file1_word_count = len(file1_words)
    file2_word_count = len(file2_words)
    grand_total_words = file1_word_count + file2_word_count

    # Top words
    top_words_file1 = get_top_words(file1_words)
    top_words_file2 = get_top_words(file2_words)

    # Get IP address
    ip_address = get_ip_address()

    # Output results
    result = f"""
    IF.txt word count: {file1_word_count}
    AlwaysRememberUsThisWay.txt word count: {file2_word_count}
    Grand total word count: {grand_total_words}
    Top 3 words in IF.txt: {top_words_file1}
    Top 3 words in AlwaysRememberUsThisWay.txt: {top_words_file2}
    Container IP address: {ip_address}
    """

    # Write result to file
    output_file = '/home/data/output/result.txt'
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        f.write(result)

    # Print the result
    print(result)
