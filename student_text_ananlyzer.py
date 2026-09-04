title_one = "Student Text Analyzer"
full_name = " maxwell kwasi agyeman"
password = "Amaxw579"
sentence = "I love to eat pizza, and I love to do art."
word = "love"
sentence_upper_lower = sentence.upper() + sentence.lower()
full_name = full_name.strip()
word_count = sentence.count(word)
full_name = full_name.replace("kwasi", "kwame") 
print(full_name)
print(sentence_upper_lower)
print(word_count)
print(sentence.strip())
print(sentence.startswith("I"))
print(sentence.endswith("t"))
print(sentence.split(","))
print(sentence.isalpha())
print(sentence.isdigit())
print(sentence.isalnum())
if full_name =="":
    print("write in your full name")
else:
    print("you cannot register without")
    if password == "":
        print("write in your password")
    else:
        print("you can now register")
        