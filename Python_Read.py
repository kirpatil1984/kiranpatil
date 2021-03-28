#program to count character form the string
#final
#import pprint
message = "ASASASAAAAasaasaaaaaaaaaaaaa"
count = {}
for char in message.upper():
    count.setdefault(char, 0)
    count [char] = count[char]  + 1

print(count)
