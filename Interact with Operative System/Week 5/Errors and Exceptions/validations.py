def validate_user(username, minlen):
    assert type(username) == str, "username must be a string" #assert comprueba que sea cierto sino saca una excepción AssertionError
    if minlen <1:
        raise ValueError("minlen must be at least 1")
    if len(username)< minlen:
        return False
    if not username.isalnum():
        return False
    return True


# # desde consola
# >>> from Try import validate_user
# >>> validate_user("",-1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/workspaces/CourseraPython/Interact with Operative System/Week 5/Errors and Exceptions/Try.py", line 3, in validate_user
#     raise ValueError("minlen must be at least 1")
# ValueError: minlen must be at least 1
# >>> 