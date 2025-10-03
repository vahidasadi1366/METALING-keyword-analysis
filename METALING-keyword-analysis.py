import os
import re
from collections import defaultdict

# Define a dictionary of target words with their common variations
target_words_variations = {
    'does': ['doth', 'does', 'dos','doeth'],
    'syllable': ['syllable', 'Sillable'],
    'has': ['has', 'hath'],
    'make': ['make', 'makes', 'maketh'],
    'take': ['take', 'takes', 'taketh'],
    'come': ['come', 'comes', 'cometh'],
    'public': ['public', 'Publik', 'publice'],
    #'represent': ['represent', 'representeth'],
    #'done': ['done', 'doe', 'dones', 'don'],
   # 'before': ['before', 'befor', 'beforee', 'ear'],
    #'judge': ['judge','iudge'],
    #'speak': ['speaks', 'speakes', 'speaketh'],
    #'vowel': ['vowel', 'vowels', 'vowell'],
    #'linguistic': ['linguistic', 'linguistics', 'linguistick', 'linguistiks'],
    #'tongue': ['tongue', 'tongues', 'tung', 'tongs'],
    #'semantics': ['semantics', 'semantick', 'semanticks'],
    #'grammar': ['grammar', 'grammars', 'grammer', 'grammere'],
    #'word': ['word', 'worde', 'wordes'],
    #'dialect': ['dialect', 'dialects', 'dialecte', 'dialekt'],
    #'discourse': ['discourse', 'discourses', 'discours', 'discoursee'],
    #'language': ['language', 'languag', 'languge','languadge','languadg'],
    #'topic': ['topic', 'topick', 'topicks'],
    #'letter': ['letter', 'letters', 'lettre', 'lettrs'],
    #'know': ['knows', 'knowes', 'knoweth'],
}

# Function to find spelling variations of target words in the text files
def find_spelling_variations_in_files(directory, target_words_variations):
    # Store results for each file
    results = []

    # Loop through each file in the directory
    for filename in os.listdir(directory): 
        if filename.endswith('.txt'):
            author_year = filename[:-4]  # Extract author and year from filename
            file_path = os.path.join(directory, filename)

            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read().lower()  # Normalize text to lowercase

                # Initialize a dictionary to store found variations for this file
                found_variations = defaultdict(int)

                # Tokenize the text
                words = re.findall(r'\b\w+\b', text)

                # Check each word against the list of variations
                for target_word, variations in target_words_variations.items():
                    for variation in variations:
                        found_variations[variation] += words.count(variation)

                # Store the results with author and year
                results.append((author_year, found_variations))

    return results

# Path to your directory containing text files
directory = #'/home//Documents//Project/MetaLing corpus/C'  # Update path as needed

# Perform the analysis
variations_results = find_spelling_variations_in_files(directory, target_words_variations)

# Print the results
for author_year, variations in variations_results:
    print(f"\nAuthor/Year: {author_year}")
    for variation, count in variations.items():
        if count > 0:
            print(f"{variation}: {count} times")
