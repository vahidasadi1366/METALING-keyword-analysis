# METALING-keyword-analysis
Spelling Variation Analyzer

This project is a Python-based tool designed to identify and count spelling variations of target words across multiple text files in Metaling corpus.

Overview

The script scans .txt files in a given directory and detects predefined spelling variations (including historical or non-standard forms) of selected target words. It then counts their frequency in each file and outputs the results.

This is particularly useful for:

Linguistic analysis
Historical text studies
Corpus-based research
 Features
Detects multiple spelling variations for each target word
Processes multiple .txt files automatically
Extracts author and year from filenames
Outputs frequency counts per file
Case-insensitive text processing
 Project Structure
project/
│
├── script.py
├── data/
│   ├── author1_1600.txt
│   ├── author2_1700.txt
│   └── ...
 How It Works
Define target words and their spelling variations:
target_words_variations = {
    'does': ['doth', 'does', 'dos', 'doeth'],
    'syllable': ['syllable', 'Sillable'],
    ...
}
The script:
Reads all .txt files in the directory
Converts text to lowercase
Tokenizes words using regex
Counts occurrences of each variation
Outputs results per file:
Author/Year: author1_1600
doth: 12
does: 5
Usage
Set the directory path:
directory = '/path/to/your/text/files'
Run the script:
python script.py
Requirements
Python 3.x
No external libraries required (uses built-in modules only)
Example Use Case

This tool can be used to track diachronic changes in spelling, such as:

"doth" → "does"
"maketh" → "makes"
Notes
Only .txt files are processed
Filenames should include author and year (e.g., Shakespeare_1600.txt)
Results are printed in the terminal (can be extended to save to file)
Future Improvements
Export results to CSV/Excel
Visualize frequency trends
Support for larger corpora
GUI interface
Vahid Asadidehziri

 License

This project is open-source and available for academic and research purposes.
