import pymongo
from bson.son import SON

#gets you the handler on the mongo client
client = pymongo.MongoClient()
#choose the data base
db = client.hys

user_collection = db.users
trip_collection = db.trips

def delete_all():
	user_collection.remove()
	trip_collection.remove()

def add_user(uname):
	print uname
	user_collection.insert({
		"user_name": uname,
		"trips": []
		})
	print user_collection.find_one()

def is_user(uname):
	user_entry = user_collection.find( { "user_name": uname } )
	return True if user_entry else False

def get_user_trips(uname):
	trip_list = list()
	if is_user(uname):
		trips = user_collection.find( { "user_name": uname }, {"trips":1} )
		for trip in trips:
			trip_list.append(get_trip_details(trip))
	return trip_list

def get_trip_details(trip_name):
	print trip_collection.find({ "trip_name": trip_name }, { "_id": 0 })
	return trip_collection.find({ "trip_name": trip_name }, { "_id": 0 })

def add_trip(trip):
	trip_collection.find({"trip_name": trip['trip_name']})
	user_list = [trip['trip_owner'], trip['participant_1'], trip['participant_2']]
	u_list = list()
	for user in user_list:
		if not is_user(user) and not None:
			u_list.append(user)
			print "Not a user"
			return None
	trip_collection.insert({
			'trip_name': trip['trip_name'],
			'trip_owner': trip['trip_owner'],
			'participants': [trip['participant_1'], trip['participant_2']],
			'destinations': [trip['destination_1']]
		})
	[user_collection.update({ "user_name": user}, { "$addToSet": {"trips": [trip['trip_name']] }} ) for user in u_list]
	return trip['trip_name']

def edit_trip(trip_name):
	pass

def get_trip_participants():
	pass
