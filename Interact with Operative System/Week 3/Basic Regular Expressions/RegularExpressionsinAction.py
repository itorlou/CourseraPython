import re 

print(re.search(r"A.*a","Argetina"))
print(re.search(r"^A.*a$","Azerbaijan")) # que empiece ^ y termine $

print(re.search(r"^A.*a$","Australia"))

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"

print(re.search(pattern, "_this_is_a_valid_variable_name"))

print(re.search(pattern, "loren ipsum dolor sit anem"))
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2my_variable1"))