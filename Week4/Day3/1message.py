# encoded message = asdfHxcvsdfgEasdewrLasvsvdLasdsdOasfg

encode_msg = input("Enter the encoded message: ")
message = ""
for letter in encode_msg:
	if letter.isupper():
		message = message + letter
		
print("the message was : ", message)