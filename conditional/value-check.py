sentence = 'The quick brown fox jumped over the lazy Dog'
word = 'quick'

if word in sentence:
#we can put .lower() at the end of sentence to check with out case sensitivity
    print('found')
else:
    print('not found')


nums = [1, 2, 3, 4]

if 3 in nums: #can be done the same way with strings
    print('found')
else:
    print('not found')