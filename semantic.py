# Importing spacy.
import spacy
# Specifying the model to be used.
# IMPORTANT: this model must be installed:
# >>> python -m spacy download en_core_web_md
nlp = spacy.load('en_core_web_md')

# Declaring variables containing spacy objects to be analyzed for similarities.
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4 = nlp("car")
word5 = nlp("petrol")
word6 = nlp("coal")

# Printing out similarities for objects declared above.
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print(word4.similarity(word5))
print(word4.similarity(word6))
# It's interesting how the natural language processing can find references among items of the same groups
# (e.g. cat and monkey) and establish a degree of similarity between them.
# I also analyzed an additional example comparing car with petrol and with coal. The nlp found a much higher
# similarity between car and petrol, as the latter is used as fuel to the former, than with coal,
# even though car has more letter in common with coal.

# When using the simpler language model 'en_core_web_sm', the similarity found between elements is much higher.
# This possibly indicates a more limited power when it comes to establish similarities taking into
# consideration parameters beyond simply the letters themselves.


# Further examples found on the pdf:
# Declaring all words into a single spacy object and looping through it using a nested loop to get similarities.
# tokens = nlp("cat apple monkey banana")
# for token1 in tokens:
#     for token2 in tokens:
#         print(token1.text, token2.text, token1.similarity(token2))


# Declaring sentences to be used to establish similarities.
# sentence_to_compare = "Why is my cat on the car"
# sentences = [
# "where did my dog go",
# "Hello, there is my car",
# "I\'ve lost my car in my car",
# "I\'d like my boat back",
# "I will name my dog Diana"
# ]
# model_sentence = nlp(sentence_to_compare)
# for sentence in sentences:
#     similarity = nlp(sentence).similarity(model_sentence)
#     print(sentence + " - ", similarity)
