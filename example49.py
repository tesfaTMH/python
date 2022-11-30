# a program that chnges a text to coded numbers 
msg = input("Enter a random text: ")
new_msg = msg.replace("a", "4")
new_msg = new_msg.replace("b", "8")
new_msg = new_msg.replace("e", "3")
new_msg = new_msg.replace("l", "1")
new_msg = new_msg.replace("o", "0")
new_msg = new_msg.replace("s", "5")
new_msg = new_msg.replace("t", "7")

print(new_msg)