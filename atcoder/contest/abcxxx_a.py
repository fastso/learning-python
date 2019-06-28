nums = [1,2]
print(any([num % 7 == 0 for num in nums]))


doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
keyword = 'casino'
indices = []
# Iterate through the indices (i) and elements (doc) of documents
for i, doc in enumerate(doc_list):
    print(i, doc)
    # Split the string doc into a list of words (according to whitespace)
    tokens = doc.split()
    # Make a transformed list where we 'normalize' each word to facilitate matching.
    # Periods and commas are removed from the end of each word, and it's set to all lowercase.
    normalized = [token.rstrip('.,').lower() for token in tokens]
    print(normalized)
    # Is there a match? If so, update the list of matching indices.
    if keyword.lower() in normalized:
        indices.append(i)
print(indices)