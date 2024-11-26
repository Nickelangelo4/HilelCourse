import string

input_string = 'Should, I. subscribe? Yes!'

cleaned_string = input_string.translate(str.maketrans('', '', string.punctuation))

words = cleaned_string.split()
capitalized_words = ''.join(word.capitalize() for word in words)

hashtag = f"#{capitalized_words}"

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)
