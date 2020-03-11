import re, base64, json

def Encode(message):
	message_bytes = message.encode('ascii')
	base64_bytes = base64.b64encode(message_bytes)
	base64_message = base64_bytes.decode('ascii')
	return base64_message

def Decode(base64_message):
	base64_bytes = base64_message.encode('ascii')
	message_bytes = base64.b64decode(base64_bytes)
	message = message_bytes.decode('ascii')
	return message

def Validate(email, password, name, cell_number):
	match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

	if (match != None and len(cell_number) == 9 and len(password)>=6):
		return True
	return False


def Register(email, password, name, cell_number):
	if(Validate(email, password, name, cell_number)):
		password = Encode(password)
		data = {}
		try:
			with open('accounts.json', 'r') as fp:
				data = json.load(fp)
		except:
			pass
		data.update({email: (password, name, cell_number)})
		with open('accounts.json', 'w') as fp:
			json.dump(data, fp)
		return True
	return False


def Login(email, password):
	try:
		with open('accounts.json', 'r') as fp:
			data = json.load(fp)
		for item in data:
			if email == item and Encode(password) == data[item][0]:
				return True
		return False
	except:
		pass