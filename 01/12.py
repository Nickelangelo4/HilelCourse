import string
import keyword

input_string = 'getValue'

is_valid = (
    input_string.isidentifier() and
    input_string not in keyword.kwlist and
    input_string.islower() and
    input_string.count('_') <= 1
)

print(is_valid)
