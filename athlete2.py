def sanitize(time_string):
	
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return(time_string)
		
	(mins, secs) = time_string.split(splitter)
	return(mins + '.' + secs)
	
def read_data(filename):
	
	try:
	
		with open(filename, 'r') as data:
			list_data = data.readline().strip().split(',')
			return({'Name': list_data.pop(0), 
					'DOB' : list_data.pop(0), 
					'Times' : str(sorted(set([sanitize(t) for t in list_data]))[0:3])})
			
	except IOError as ioerr:
		print('File Error: '+ str(ioerr))
		return(None)
	
sarah = read_data('sarah2.txt')
print(sarah['Name'] + "'s fastest times are: "+ sarah['Times'])
	