def read_data(filename):
	
	try:
	
		with open(filename, 'r') as data:
			return data.readline().strip().split(',')
			
	except IOError as ioerr:
		print('File Error: '+ str(ioerr))
		return(None)
		
def sanitize(time_string):
	
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return(time_string)
		
	(mins, secs) = time_string.split(splitter)
	return(mins + '.' + secs)
	
james = read_data('james.txt')
julie = read_data('julie.txt')
sarah = read_data('sarah.txt')
mikey = read_data('mikey.txt')

print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])


	