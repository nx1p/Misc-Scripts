def ReadOutLog():
	with open('env_data.csv','r') as env_data:
		return env_data.read()
		
print(ReadOutLog())