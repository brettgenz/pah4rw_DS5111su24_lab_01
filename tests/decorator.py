def decorator(func):
	def wrapper():
		print("This test should fail.")
		func()
	return wrapper