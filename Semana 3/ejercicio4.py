translate_dict = {}
translations = input("Please enter the transalations <word>:<translate> and divided by commas: ")
translation_list = translations.split(",")
#["Hello:Hola","Bye:Adios"]
for translation in translation_list:
    values_list= translation.split(":")
    #["Hello","Hola"]
    key_english = values_list[0]
    value_spanish = values_list[1]
    translate_dict[key_english] =value_spanish

input_to_translate = input("Please enter a phrase to translate: ")
word_list = input_to_translate.split(" ")
word_result= ""

for word in word_list:
    word_result += translate_dict.get(word,word) 
    word_result += " "

print(word_result)