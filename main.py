import re

with open("names.txt", "r") as data:
    data = data.read()
# [
#     ([first name] [last name],
#      email,
#      phone,
#      occupation,
#      Twitter handle)
# ]
names = (re.findall(r"|,\s\w+|\w+, \w+", data, re.UNICODE))
email = re.findall(r'[\d\w\'-+.]+@[-.\d\w]+', data)
phone = re.findall(r'\+?\d?\s?\(?\d{3}\)?\s?-?\d{3}-\d{4}', data)
occupation = re.findall(r"\t\w+,|\t\w+ \w+,", data)
twitter = re.findall(r'(?<=\t)+@[-.\d\w]+', data)
print(data)
print(names)
print(email)
print(occupation)
print(twitter)
