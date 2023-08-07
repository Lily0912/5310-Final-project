
import random
from faker import Faker
from faker.providers import date_time
import pandas as pd

#%%
#生成user数据
df1=pd.read_csv("D:/data/data/Travel details dataset（1-4）.csv")
list(df1)
fake = Faker()
data1 = []
for _ in range(138):
    email = fake.email()
    phone = fake.phone_number()
    record = {
        'email': email,
        'phone': phone
    }
    
    data1.append(record)
# 打印生成的数据
data1 = pd.DataFrame(data1)
data_user=pd.concat([df1,data1],axis=1)
list(data_user)
user_id_ch=data_user['Trip ID']

fake = Faker()
data_itinerary = []
for _ in range(138):
    user_id= random.choice(user_id_ch)  # 随机生成hotel_id
    record = {
        'user_id': user_id
    }
    
    data_itinerary.append(record)
data_itinerary = pd.DataFrame(data_itinerary)
data_user=pd.concat([data_user,data_itinerary],axis=1)
# 打印生成的数据

data_user1=data_user.loc[:,['Trip ID','Traveler name','Traveler age','Traveler gender','Traveler nationality','email','phone']]
data_user2=data_user.loc[:,['Trip ID','user_id','Destination','Start date','End date','Duration (days)','Accommodation type','Accommodation cost','Transportation type','Transportation cost']]
data_user=pd.concat([data_user1,data_user2],axis=1)
data_user.columns=['user_id','user_name','age','gender','nationality','email','phone',
                   'trip_id','user_id','destination','start_date','end_date','duration',
                   'accommodation_type','accommodation_cost','transportation_type','transportation_cost']
data_user.to_csv('D:/data/data_user.csv', index=False)  # 保存为CSV文件，不包含行索引

#%%生成hotel数据
#hotel1

fake = Faker()
data2 = []

for _ in range(238):
    hotel_id = fake.unique.random_number(digits=6)
    hotel_name = fake.company()
    city_id = fake.random_number(digits=4)
    contact_number = fake.phone_number()
    address = fake.address()
    starrating = fake.random_element(elements=('1 Star', '2 Star', '3 Star', '4 Star', '5 Star'))
    
    data2.append([hotel_id, hotel_name, city_id, contact_number, address, starrating])

data_hotel1 = pd.DataFrame(data2, columns=['hotel_id', 'hotel_name', 'city_id', 'contact_number', 'address', 'starrating'])
data_hotel1.to_csv('D:/data/data_hotel1.csv', index=False)  # 保存为CSV文件，不包含行索引

hotel_id_ch=data_hotel1['hotel_id']

#hotel2
fake = Faker()
# 生成500条随机数据
data22 = []
for _ in range(500):
    room_id = fake.unique.random_number(digits=5)  # 随机生成room_id
    hotel_id = random.choice(hotel_id_ch)  # 随机生成hotel_id
    room_number = fake.random_int(min=100, max=999)  # 随机生成room_number
    room_type = fake.word()  # 随机生成room_type
    room_price = fake.random_int(min=50, max=200)  # 随机生成room_price
    occupancy_limit = fake.random_int(min=1, max=4)  # 随机生成occupancy_limit
    room_status = fake.boolean()  # 随机生成room_status

    data22.append([room_id, hotel_id, room_number, room_type, room_price, occupancy_limit, room_status])
# 转换为数据框格式
data_hotel2 = pd.DataFrame(data22, columns=['room_id', 'hotel_id', 'room_number', 'room_type', 'room_price', 'occupancy_limit', 'room_status'])
data_hotel2.to_csv('D:/data/data_hotel2.csv', index=False)  # 保存为CSV文件，不包含行索引

room_id_ch=data_hotel2['room_id']
#hotel3
fake = Faker()

# 生成随机数据
data23 = []
for _ in range(200):
    reservation_id = fake.unique.random_number(digits=7)
    user_id = random.choice(user_id_ch)
    number_of_occupants = fake.random_int(min=1, max=4)
    hotel_id = random.choice(hotel_id_ch)
    room_id = random.choice(room_id_ch)
    check_in_date = fake.date_between(start_date='-1y', end_date='+1y')
    check_out_date = fake.date_between(start_date=check_in_date, end_date='+1y')
    total_price = fake.random_int(min=100, max=1000)
    
    data23.append([reservation_id, user_id, number_of_occupants, hotel_id, room_id, check_in_date, check_out_date, total_price])

# 转换为数据框
data_hotel3 = pd.DataFrame(data23, columns=['reservation_id', 'user_id', 'number_of_occupants', 'hotel_id', 'room_id', 'check_in_date', 'check_out_date', 'total_price'])
data_hotel3.to_csv('D:/data/data_hotel3.csv', index=False)  # 保存为CSV文件，不包含行索引
hotel_reservation_id_ch=data_hotel3['reservation_id']
#%%生成car数据
data3=pd.read_csv("D:/data/data/car rental sample.csv")
list(data3)
fake = Faker()
data31 = []
for _ in range(2730):
    supplier_id = fake.unique.random_number(digits=6)
    contact_number = fake.phone_number()
    record = {
        'supplier_id': supplier_id,
        'contact_number': contact_number
    }
    
    data31.append(record)
# 打印生成的数据
data31 = pd.DataFrame(data31)
data_car_1=pd.concat([data31['supplier_id'],data3.loc[:,['supplier_name','supplier_address','supplier_loction_type' ]],data31['contact_number']],axis=1)
list(data_car_1)
data_car_1.columns=['supplier_id','supplier_name','supplier_address','supplier_location_type','contact_number']
data_car_1.to_csv('D:/data/data_car_1.csv', index=False,errors='ignore')  # 保存为CSV文件，不包含行索引

supplier_id_ch=data_car_1['supplier_id']
#car2
data_car_2=data3.loc[:,['product_id','product_name','airbags','aircon','doors','group','seats','transmission','mileage','price']]
data_car_2.columns=['car_id','car_name','airbags','aircon','doors','groups','seats','transmission','mileage','rental_price_per_day']
data_car_2.to_csv('D:/data/data_car_2.csv', index=False)  # 保存为CSV文件，不包含行索引

car_id_ch=data_car_2['car_id']

#car3
fake = Faker()
data33 = []
for _ in range(2730):
    reservation_id = fake.unique.random_number(digits=6)
    user_id = random.choice(user_id_ch)
    record = {
        'reservation_id': reservation_id,
        'user_id': user_id
    }
    
    data33.append(record)
data33=pd.DataFrame(data33)
data_car_3=pd.concat([data33,car_id_ch,supplier_id_ch,data3.loc[:,['city','rental_length','start_date','start_time','return_date','return_time','deposit_price','drive_away_price','price','RunDate']]],axis=1)
data_car_3.to_csv('D:/data/data_car_3.csv', index=False)  # 保存为CSV文件，不包含行索引
list(data_car_3)
car_reservation_id_ch=data_car_3['reservation_id']
#%%
#airline
# 创建Faker对象
fake = Faker()
data41 = []
for _ in range(90):
    airline_id = fake.unique.random_int(min=1000, max=9999)
    airline_name = fake.company()
    country_id = fake.random_int(min=1, max=10)
    headquarters = fake.city()
    contact_number = fake.phone_number()
    data41.append([airline_id, airline_name, country_id, headquarters, contact_number])

# 转换为数据框
data_airline = pd.DataFrame(data41, columns=['airline_id', 'airline_name', 'country_id', 'headquarters', 'contact_number'])
data_airline.to_csv('D:/data/data_airline.csv', index=False)  # 保存为CSV文件，不包含行索引
airline_id_ch=data_airline['airline_id']
#airport
fake = Faker()
data42 = []
for _ in range(120):
    airport_id = fake.unique.random_int(min=1, max=1000)
    airport_name = fake.company()
    city_id = fake.random_int(min=1, max=100)
    country_id = fake.random_int(min=1, max=50)
    IATA_code = fake.random_element(elements=('AAA', 'BBB', 'CCC', 'DDD', 'EEE'))
    coordinates = str(fake.latitude()) + ', ' + str(fake.longitude())
    
    data42.append([airport_id, airport_name, city_id, country_id, IATA_code, coordinates])

data_airport = pd.DataFrame(data42, columns=['airport_id', 'airport_name', 'city_id', 'country_id', 'IATA_code', 'coordinates'])
data_airport.to_csv('D:/data/data_airport.csv', index=False)  # 保存为CSV文件，不包含行索引
airport_id_ch=data_airport['airport_id']

#flight
data4=pd.read_csv("D:/data/data/routes（14）.csv")
fake = Faker()
fake.add_provider(date_time)
data43 = []
for _ in range(67663):
    flight_id = fake.unique.random_number(digits=6)
    airline_id = random.choice(airline_id_ch)
    departure_airport_id = random.choice(airport_id_ch)
    departure_time = fake.date_time_between(start_date='-1y', end_date='now')
    arrival_airport_id = random.choice(airport_id_ch)
    arrival_time= departure_time + timedelta(hours=fake.random_int(min=1, max=10))

    data43.append([flight_id,airline_id,departure_airport_id,departure_time,arrival_airport_id,arrival_time])
# 打印生成的数据
data43 = pd.DataFrame(data43)
data_flight=pd.concat([data43,data4.iloc[:,7:9]],axis=1)
data_flight.columns=['flight_id','airline_id','departure_airport_id','departure_time','arrival_airport_id','arrival_time','stops','equipment']
data_flight.to_csv('D:/data/data_flight.csv', index=False)  # 保存为CSV文件，不包含行索引
flight_id_ch=data_flight['flight_id']

#flight_reservation
data4_1=pd.read_csv("D:/data/data/Passanger_booking_data.csv")
fake=Faker()
fake.add_provider(date_time)
data44 = []
for _ in range(50002):
    reservation_id = fake.unique.random_number(digits=6)
    user_id = random.choice(user_id_ch)
    flight_id = random.choice(flight_id_ch)
    flight_time = fake.date_time_between(start_date='-1y', end_date='now')

    data44.append([reservation_id,user_id,flight_id,flight_time])
# 打印生成的数据
data44 = pd.DataFrame(data44)
data44.columns=['reservation_id','user_id','flight_id','flight_time']
data_flight_reservation=pd.concat([data44,data4_1.loc[:,['route','flight_duration']]],axis=1)
data_flight_reservation.to_csv('D:/data/data_flight_reservation.csv', index=False)  # 保存为CSV文件，不包含行索引
list(data_flight_reservation)
flight_reservation_id_ch=data_flight_reservation['reservation_id']
#%%group_booking
fake=Faker()
data_group_booking = []
for _ in range(500):
    group_booking_id = fake.unique.random_number(digits=6)
    group_name = fake.company()
    booking_date = fake.date()
    hotel_reservation_id = random.choice(hotel_reservation_id_ch)
    car_reservation_id  = random.choice(car_reservation_id_ch)
    flight_reservation_id  = random.choice(flight_reservation_id_ch)
    
    data_group_booking.append([group_booking_id, group_name, booking_date, hotel_reservation_id, car_reservation_id, flight_reservation_id])

# 打印生成的数据
data_group_booking = pd.DataFrame(data_group_booking)
data_group_booking.columns=['group_booking_id', 'group_name', 'booking_date', 'hotel_reservation_id', 'car_reservation_id', 'flight_reservation_id']

data_group_booking.to_csv('D:/data/data_group_booking.csv', index=False)  # 保存为CSV文件，不包含行索引

group_booking_id_ch=data_group_booking['group_booking_id']
#%%booking
fake = Faker()
data_booking = []
for _ in range(2380):
    booking_id = fake.unique.random_number(digits=6)
    group_booking_id = random.choice(group_booking_id_ch)
    user_id = random.choice(user_id_ch)
    hotel_id = random.choice(hotel_id_ch)
    check_in_date = fake.date_between(start_date='-30d', end_date='+30d')
    check_out_date = fake.date_between(start_date=check_in_date, end_date='+30d')
    hotel_price = fake.random_number(digits=4)
    car_id = random.choice(car_id_ch)
    start_date = fake.date_between(start_date='-30d', end_date='+30d')
    return_date = fake.date_between(start_date=start_date, end_date='+30d')
    car_price = fake.random_number(digits=4)
    flight_id = random.choice(flight_id_ch)
    flight_time = fake.date_time_between(start_date='-30d', end_date='+30d')
    flight_price = fake.random_number(digits=4)
    
    data_booking.append([booking_id, group_booking_id, user_id, hotel_id, check_in_date, check_out_date, hotel_price,
                 car_id, start_date, return_date, car_price, flight_id, flight_time, flight_price])

# 转换为数据框格式
data_booking = pd.DataFrame(data_booking, columns=['booking_id', 'group_booking_id', 'user_id', 'hotel_id', 'check_in_date',
                                 'check_out_date', 'hotel_price', 'car_id', 'start_date', 'return_date',
                                 'car_price', 'flight_id', 'flight_time', 'flight_price'])

data_booking.to_csv('D:/data/data_booking.csv', index=False)  # 保存为CSV文件，不包含行索引

booking_id_ch=data_booking['booking_id']

#%%booking_segments
fake = Faker()
data_booking_segments = []
booking_id = random.sample(booking_id_ch.tolist(), 1000)
flight_id = random.sample(flight_id_ch.tolist(), 1000)
for _ in range(1000):
    segment_price = fake.random_number(digits=4)
    
    data_booking_segments.append(segment_price)


data_booking_segments = pd.DataFrame({'booking_id': booking_id, 'flight_id': flight_id, 'segment_price': data_booking_segments})
data_booking_segments.to_csv('D:/data/data_booking_segments.csv', index=False)  # 保存为CSV文件，不包含行索引

