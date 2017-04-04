FuzzyQuery
-------------

FuzzyQuery generates binder queries designed to catch typos.

Requirements:
- Python 2.7 (download here: https://www.python.org/downloads/release/python-2713/)


Instructions
-------------
  1. Unzip directory to desktop
  2. Open terminal
  3. type `pip install numpy pandas pyperclip`
  4. type `cd desktop/FuzzyQuery" and press enter`
  5. type `python fuzzyquery.py" and press enter`


Usage
-------------
Input a list of words seperated by commas to generate a Binder "name contains" query that will catch typos within a Levenshtein distance of 1.
  
  **Input:**
         `sprite, pepsi`

  **Returns:** 
          *name contains ('srite', 'p*psi', 'sp*ite', 'srpite', 'ppsi', 'pe*psi', 'spr*te', 'pep*i', 'pepis', 'pepi', 'spri*te', 'spite', 'epsi', 'pe*si', 'spr*ite', 'sprte', 'pespi', 'peps', 'sp*rite', 'sprite', 's*rite', 'spirte', 'pepsi', 'spri*e', 'ppesi', 'sprtie', '*epsi', 'peps*i', 'sprit', 'pesi', 'prite', 'sprie', 'psrite', 'pep*si')*



Optionally, seperate list of words with a "|". Words to the left of "|" are edited within an edit distance; words on the right are appended onto the query untouched. 

  **Input:**
         `sprite, pepsi| coke, cke, cola`

  **Returns:**
          *name contains ('srite', 'p*psi', 'sp*ite', 'srpite', 'ppsi', 'pe*psi', 'spr*te', 'pep*i', 'pepis', 'pepi', 'spri*te', 'spite', 'epsi', 'pe*si', 'spr*ite', 'sprte', 'pespi', 'peps', 'sp*rite', 'sprite', 's*rite', 'spirte', 'pepsi', 'spri*e', 'ppesi', 'sprtie', '*epsi', 'peps*i', 'sprit', 'pesi', 'prite', 'sprie', 'psrite', 'pep*si', 'coke', 'cke', 'cola')*

Info
-------------
The script makes four types of edits to the input word:

  1. Deletions         "yogurt" ->  "yogrt"

  2. Transposes        "yogurt" ->  "yogrut"

  3. Insertions        "yogurt" ->  "yohgurt"

  4. Replacements      "yogurt" ->  "vogurt"


FuzzyQuery generates potential replacement errors based on four schemes:

  1. Wildcards
    - Not affected by "typo distance" because wildcard insertions and replacements include all characters

  2. Keyboard Distance **(DEPRECATED IN version 1.2)**
    - Neighboring keys have a lower "typo distance" than more distant keys

  3. Human Error-Frequencies **(DEPRECATED IN version 1.2)**
    - Common errors made by mech-turk transcribers are favored over rare errors (based on David Su's data).

  4. OCR Error-Frequencies **(DEPRECATED IN version 1.2)**
    - Common errors made by OCR are favored over rare errors (based on David Su's data).


Support
-------------
Gus Ostow
augustus.ostow@infoscoutinc.com
