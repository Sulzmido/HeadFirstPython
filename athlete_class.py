def sanitize(time_string):
	
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return(time_string)
		
	(mins, secs) = time_string.split(splitter)
	return(mins + '.' + secs)

class Athlete:
	
	def __init__(self, a_name, a_dob=None, a_times=[]):
		
		self.name = a_name
		self.dob = a_dob
		self.times = a_times
	
	def top3(self):
		return(sorted(set([sanitize(t) for t in self.times]))[0:3])
		
	def add_time(self, time_val):
		self.times.append(time_val)
		
	def add_times(self, times_list):
		self.times.extend(times_list)
	
def read_data(filename):
	
	try:
	
		with open(filename, 'r') as data:
			list_data = data.readline().strip().split(',')
			return Athlete(list_data.pop(0), list_data.pop(0), list_data)
			
	except IOError as ioerr:
		print('File Error: '+ str(ioerr))
		return(None)
	
sarah = read_data('sarah2.txt')
print(sarah.name + "'s fastest times are: "+ str(sarah.top3()))

vera = Athlete('Vera Vi')
vera.add_time('1.31')
print(vera.top3())
vera.add_times(['2.22', '1-21', '2:22'])
print(vera.top3())
	