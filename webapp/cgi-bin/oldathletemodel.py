import pickle
from athletelist import AthleteList

def get_coach_data(filename):
	
	try:
	
		with open(filename, 'r') as data:
			list_data = data.readline().strip().split(',')
			return AthleteList(list_data.pop(0), list_data.pop(0), list_data)
			
	except IOError as ioerr:
		print('File Error: '+ str(ioerr))
		return(None)
		
def put_to_store(files_list):

	all_athletes = {}
	
	for filename in files_list:
		ath = get_coach_data(filename)
		all_athletes[ath.name] = ath
	try:
		with open('athletes.pickle','wb') as pf:	
			pickle.dump(all_athletes, pf)
			
	except IOError as err:
		print('File Error: '+str(err))
	
	except pickle.PickleError as perr:
		print('Pickling Error: '+str(perr))
		
	return(all_athletes)
	
def get_from_store():

	all_athletes = {}
	try:
		with open('athletes.pickle','rb') as pf:	
			all_athletes = pickle.load(pf)
			
	except IOError as err:
		print('File Error: '+str(err))
	
	except pickle.PickleError as perr:
		print('Pickling Error: '+str(perr))
		
	return(all_athletes)
	
def get_names_from_store():
	
	athletes = get_from_store()
	#return athletes.keys()
	response = [athletes[each_ath].name for each_ath in athletes]
	return(response)