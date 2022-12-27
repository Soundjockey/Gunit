url_token = 'https://restful-booker.herokuapp.com/auth'
params = {"username": "admin", "password": "password123"}
headers = {'Content-Type' : 'application/json'}
url_update = 'https://restful-booker.herokuapp.com/booking/123'
params_update = {"firstname" : "James","lastname" : "Brown","totalprice" : 111,"depositpaid" : True,"bookingdates" : {"checkin" : "2018-01-01","checkout" : "2019-01-01"},"additionalneeds" : "Breakfast"}
