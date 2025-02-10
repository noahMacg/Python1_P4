# MacGillivrayP4
# Programmer: Noah MacGillivray
# EMail: nmacgillivray@cnm.edu
# Purpose: Use python dictionary to create a small
# two language translator

# dictionary to hold phrases in

gaelic_translations = {
    "Hello world!": "Halò a shaoghail!",
    "How are you?": "Ciamar a tha sibh?",
    "I am learning Python.": "Tha mi ag ionnsachadh Python.",
    "What is the meaning of life?": "Dè an ciall a tha beatha?",
    "Where are you from?": "Cò às a tha thu?",  # Informal
    "Where are you from? (formal/plural)": "Cò às a tha sibh?",
    "They may take our lives but they will never take our freedom!": "’S dòcha gun toir iad ar beatha ach cha toir iad ar saorsa gu bràth!",
}
print(gaelic_translations.keys())
print()

user_phrase = input(
    "Please provide a phrase from above to translate to Gaelic (case and punctuation must match):"
)

print(gaelic_translations.get(user_phrase))
