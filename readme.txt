FuzzyQuery
=============

FuzzyQuery generates binder queries designed to catch typos.

Requirements:
- Python 2.7 (download here: https://www.python.org/downloads/release/python-2713/)


Instructions
-------------
  1. Unzip directory to desktop
  2. Open terminal
  3. type "cd desktop/fuzzyquery" and press enter
  4. type "python fuzzyquery.py" and press enter

NOTE: The script requires the "d_arrays.npz" file to be in the same directory as the fuzzyquery.py file.


Info
-------------
The script makes four types of edits to the input word:

  1. Deletions         "yogurt" ->  "yogrt"

  2. Transposes        "yogurt" ->  "yogrut"

  3. Insertions        "yogurt" ->  "yohgurt"

  4. Replacements      "yogurt" ->  "vogurt"


Some typos are more likely than others. The "typo distance" parameter influences the behavior of insertions and replacements. When set to zero replacements do not occur and insertions only include neighoring characters.


FuzzyQuery generates potential errors based on four schemes:

  1. Wildcards
    - Not affected by "typo distance" because wildcard insertions and replacements include all characters

  2. Keyboard Distance
    - Neighboring keys have a lower "typo distance" than more distant keys

  3. Human Error-Frequencies
    - Common errors made by mech-turk transcribers are favored over rare errors (based on David Su's data).

  4. OCR Error-Frequencies
    - Common errors made by OCR are favored over rare errors (based on David Su's data).


Support
-------------
Gus Ostow
augustus.ostow@infoscoutinc.com



