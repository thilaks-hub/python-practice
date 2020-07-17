def passwordstrength(password=None,length=8,alpha=4,special=2,digit=2):
	if password:
		if len(password) >= length:
			alphalength=0
			speciallength=0
			digitlength=0
			for char in password:
				if char.isalpha():
					alphalength = alphalength + 1
				elif char.isdigit():
					digitlength = digitlength + 1
				else:
					speciallength = speciallength + 1
			if alphalength < alpha:
				return "Password must contain atleast 4 alphabets"
			elif digitlength < digit:
				return "Password must contain atleast 2 numbers"
			elif speciallength < special:
				return "Password must contain atleast 2 special characters"
			else:
				return "password okay"
		else:
			return "password must contain atleat 8 characters"
	else:
		return "Password cannot be empty"

print(passwordstrength(password='Your password here'))
