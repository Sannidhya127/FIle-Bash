import difflib
from difflib import SequenceMatcher, get_close_matches, Differ
from pprint import pprint

str1 = "a"
str2 = "a"
seq = SequenceMatcher(a=str1, b=str2)
print(seq.ratio())
command = input("Enter here: ")
word_list = ["bash --q", "git init", "cd",
             "cd --to", "ls --check",  "ls", "mv"]
if command in word_list:
    print("Ok")

else:
    items = get_close_matches(command, word_list, n=1, cutoff=0.5)
    for i in items:
        print(f"Did you mean {i}?")

f1 = open("file1.txt", "r")
f2 = open("file2.txt", "r")

txt1 = f1.read().splitlines()
txt2 = f2.read().splitlines()

dif = Differ()

df = list(dif.compare(txt1, txt2))

newLine = "\n"
if newLine in df:
    newLine = ""
pprint(df)
