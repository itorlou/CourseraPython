import re

print(re.search(r".com","wellcome."))
print(re.search(r"\.com","wellcome."))

print(re.search(r"\.com","wellcome.com"))


print(re.search(r"\w","wellcome.com"))
print(re.search(r"\w*","lorem ipsum"))