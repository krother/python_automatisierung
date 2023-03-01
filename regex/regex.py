
import re

text = '''thyme coriander rosemary cinnamon
pepper tarragon basil salvia cumin'''

pattern = "c\w+"

# find all occurences
re.findall(pattern, text)

# dot matches newline
re.findall(pattern, text, re.DOTALL)

# find first occurence or None
s = re.search(pattern, text)
s.span()

# replace
re.sub(pattern, "SPICE", text)

# ignore upper/lower case
re.findall(pattern, text, re.IGNORECASE)
