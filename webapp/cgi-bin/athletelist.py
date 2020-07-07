def sanitize(time_string):
	
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return(time_string)
		
	(mins, secs) = time_string.split(splitter)
	return(mins + '.' + secs)

class AthleteList(list):
	
	def __init__(self, a_name, a_dob=None, a_times=[]):
		
		list.__init__([])
		self.name = a_name
		self.dob = a_dob
		self.extend(a_times)
	
	@property
	def top3(self):
		return(sorted(set([sanitize(t) for t in self]))[0:3])
	
	@property
	def to_dict(self):
		return ({'Name': self.name,
				 'DOB': self.dob,
				 'Top3': self.top3})
	
	@property
	def clean_data(self):
		return(sorted(set([sanitize(t) for t in self])))
	
def read_data(filename):
	
	try:
	
		with open(filename, 'r') as data:
			list_data = data.readline().strip().split(',')
			return AthleteList(list_data.pop(0), list_data.pop(0), list_data)
			
	except IOError as ioerr:
		print('File Error: '+ str(ioerr))
		return(None)
	