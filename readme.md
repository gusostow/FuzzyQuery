FuzzyQuery
-------------

FuzzyQuery generates binder queries designed to catch typos.

Requirements:
- Python 2.7 (download here: https://www.python.org/downloads/release/python-2713/)


Instructions
-------------
  1. Unzip directory to desktop
  2. Open terminal
  3. type "pip install numpy pandas pyperclip"
  4. type "cd desktop/FuzzyQuery" and press enter
  5. type "python fuzzyquery.py" and press enter


Usage
-------------
Input a list of words seperated by commas to generate a Binder "name contains" query that will catch typos within a Levenshtein distance of 1.

**Example 1:** 
  Input: comb, hair
  Returns: name contains ('hiar', 'cmob', 'hair', 'hai*r', 'ha*r', 'hai', 'h*ir', 'h*air', '*hair', 'cobm', 'c*omb', '*omb', 'omb', 'hir', 'hai*', 'c*mb', 'co*b', 'ocmb', 'comb', 'har', 'co*mb', 'ha*ir', 'cmb', 'ahir', 'air', 'cob', 'com')


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
