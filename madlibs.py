# string concayanation(aka how to put strings together)

from unicodedata import name


youtuber = "nutralnine"
name = input("Your name : ")
channel = input("Channel Name : ")


print("Subscribe to " + youtuber)
print("Subscribe to {}".format(youtuber))
print(f"Subscribe to {youtuber}")


madlib = f"My name is {name}. I have a youtube channel {channel}, on which I upload my daily vlogs. "
print(madlib)