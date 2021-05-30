import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myDB = myclient["railDB"]

# login = myDB["login"]

# user1 = {
#     'username': "harry",
#     'password': "harry123"
# }

# user2 = {
#     'username': "rahul",
#     'password': "rahul123"
# }

# user3 = {
#     'username': "raju",
#     'password': "raju123"
# }

# users = [user1, user2, user3]
# login.insert_many(users)

trains = myDB["trains"]

# train1 = {
#     'number': "12267",
#     'name': "MUMBAI CENTRAL - AHMEDABAD AC DURONTO EXP",
#     'type': 'Duronto',
#     'source': "Mumbai",    
#     'destination': "Ahmedabad",
#     'available_seats': 200,
#     'arrival_time': "05:55",
#     'departure_time': "23:55"
# }

# train2 = {
#     'number': "22201",
#     'name': "KOLKATA SEALDAH - PURI DURONTO EXPRESS",
#     'type': 'Duronto',
#     'source': "Sealdah",    
#     'destination': "Puri",
#     'available_seats': 200,
#     'arrival_time': "04:00",
#     'departure_time': "20:00"
# }

# train3 = {
#     'number': "12951",
#     'name': "MUMBAI CENTRAL - NEW DELHI RAJDHANI EXPRESS",
#     'type': 'Rajdhani',
#     'source': "Mumbai",    
#     'destination': "New Delhi",
#     'available_seats': 200,
#     'arrival_time': "08:35",
#     'departure_time': "16:35"
# }

# train4 = {
#     'number': "22204",
#     'name': "SECUNDERABAD - VISAKHAPATNAM AC DURONTO EXPRESS",
#     'type': 'Duronto',
#     'source': "Secunderabad",    
#     'destination': "Vishakapatnam",
#     'available_seats': 200,
#     'arrival_time': "06:35",
#     'departure_time': "20:15"
# }

# train5 = {
#     'number': "12430",
#     'name': "NEW DELHI - LUCKNOW AC SF EXPRESS",
#     'type': 'Rajdhani',
#     'source': "New Delhi",    
#     'destination': "Lucknow",
#     'available_seats': 200,
#     'arrival_time': "06:40",
#     'departure_time': "20:50"
# }

# train6 = {
#     'number': "12019",
#     'name': "HOWRAH - RANCHI SHATABDI EXPRESS",
#     'type': 'Shatabdi',
#     'source': "Howrah",    
#     'destination': "Ranchi",
#     'available_seats': 200,
#     'arrival_time': "13:15",
#     'departure_time': "06:05"
# }


# train7 = {
#     'number': "12801",
#     'name': "PURI - NEW DELHI PURUSHOTTAM SF EXPRESS",
#     'type': 'Superfast',
#     'source': "Puri",    
#     'destination': "New Delhi",
#     'available_seats': 200,
#     'arrival_time': "04:50",
#     'departure_time': "21:45"
# }

# train8 = {
#     'number': "12833",
#     'name': "AHMEDABAD - HOWRAH SF EXPRESS",
#     'type': 'Superfast',
#     'source': "Ahmedabad",    
#     'destination': "Howrah",
#     'available_seats': 200,
#     'arrival_time': "13:30",
#     'departure_time': "00:15"
# }

# train9 = {
#     'number': "01049",
#     'name': "ADI PUNE SF SPL",
#     'type': 'Superfast',
#     'source': "Mumbai",    
#     'destination': "Ahmedabad",
#     'available_seats': 200,
#     'arrival_time': "07:30",
#     'departure_time': "22:35"
# }

# train10 = {
#     'number': "02420",
#     'name': "Gomti Express SPL",
#     'type': 'Superfast',
#     'source': "New Delhi",    
#     'destination': "Lucknow",
#     'available_seats': 4,
#     'arrival_time': "07:30",
#     'departure_time': "21:40"
# }

# trains_list = [train1, train2, train3, train4, train5, train6, train7, train8, train9]

# trains.insert_many(trains_list)
# trains.insert_one(train10)


# print("hello".capitalize())
