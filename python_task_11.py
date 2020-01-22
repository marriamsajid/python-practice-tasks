import re

removeBrackets = ["example ()", "w3resource", "github (.com57656utyjghmghfjghj)", "stackoverflow (.com)"]
pattern = r"\(\.*\w*\)\.*"

for element in removeBrackets:
    brackets = re.search(pattern, element)
    if brackets is not None:
        print(element[:brackets.start()] + element[brackets.end():])
    else:
        print(element)
