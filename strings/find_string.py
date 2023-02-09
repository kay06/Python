sentence = 'The quick brown fox jumped over the lazy dog.'

#query = sentence.find('oops') finds string and prints begining position, but if not found returns a -1
#query_two = sentence.index('oops') finds string and prints begining position, but if not found caused error 

#print(query)
#print(query_two)

query = 'oops' in sentence #puts true or false into the variable determened if the string can be found in the original variable listed
query_2 = 'fox' in sentence

print(query) # prints false because oops is not uin the sentence
print(query_2) #prints true