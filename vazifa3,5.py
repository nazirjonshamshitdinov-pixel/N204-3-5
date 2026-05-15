import os 
os.system("cls")

# 1 - masala
# cars = {
#     "Malibu": 35000,
#     "Spark": 12000,
#     "Cobalt": 18000,
#     "Tracker": 28000
# }

# q=max(cars,key=cars.get)
# a=min(cars,key=cars.get)
# s=sum(cars.values())/len(cars)
# print("eng qimmat avtomobil: ",q,cars[q])
# print("eng aarzon avtomobil: ",a,cars[a])
# print("urtacha: ",s)






# 2 - masala
# movies = {
#     "Titanic": 1997,
#     "Avatar": 2009,
#     "Inception": 2010,
#     "Interstellar": 2014
# }
# for i in movies:
#     if movies[i]>2000:
#         print(i)






# 4 - masala
# professions = {
#     "Bill Gates": "Dasturchi",
#     "Cristiano Ronaldo": "Futbolchi",
#     "Elon Musk": "Tadbirkor",
#     "Messi": "Futbolchi"
# }
# ism = input("ism kiriting: ")
# if ism in professions:
#     print(professions[ism])
# else:
#     print("bunday ism yuq")






# 5 - masala
# car_count = {
#     "Chevrolet": 120,
#     "Toyota": 95,
#     "BMW": 60,
#     "Kia": 75
# }
# kop = max(car_count,key = car_count.get)
# kam = min(car_count,key = car_count.get)
# print("eng kup: ",kop,car_count[kop])
# print("eng kam: ",kam,car_count[kam])






#  6 - masala
# books = {
#     "O'tkan kunlar": {
#         "muallifi": "Abdulla Qodiriy",
#         "janri": "Roman",
#         "chop etilgan yili": 1926,
#         "tarjimalar soni": 5
#     },
#     "Mehrobdan chayon": {
#         "muallifi": "Abdulla Qodiriy",
#         "janri": "Roman",
#         "chop etilgan yili": 1929,
#         "tarjimalar soni": 3
#     },
#     "Kecha va kunduz": {
#         "muallifi": "Cho'lpon",
#         "janri": "Roman",
#         "chop etilgan yili": 1934,
#         "tarjimalar soni": 4
#     },
#     "Sarob": {
#         "muallifi": "Abdulla Qahhor",
#         "janri": "Roman",
#         "chop etilgan yili": 1935,
#         "tarjimalar soni": 2
#     },
#     "Ulug'bek xazinasi": {
#         "muallifi": "Odil Yoqubov",
#         "janri": "Tarixiy roman",
#         "chop etilgan yili": 1974,
#         "tarjimalar soni": 6
#     },
#     "Don Kixot": {
#         "muallifi": "Migel de Servantes",
#         "janri": "Roman",
#         "chop etilgan yili": 1605,
#         "tarjimalar soni": 50
#     },
#     "Urush va tinchlik": {
#         "muallifi": "Lev Tolstoy",
#         "janri": "Tarixiy roman",
#         "chop etilgan yili": 1869,
#         "tarjimalar soni": 45
#     },
#     "Alkimyogar": {
#         "muallifi": "Paulo Koelyo",
#         "janri": "Falsafiy roman",
#         "chop etilgan yili": 1988,
#         "tarjimalar soni": 80
#     },
#     "1984": {
#         "muallifi": "Jorj Oruell",
#         "janri": "Antiutopik roman",
#         "chop etilgan yili": 1949,
#         "tarjimalar soni": 65
#     },
#     "Kichkina shahzoda": {
#         "muallifi": "Antuan de Sent-Ekzyuperi",
#         "janri": "Falsafiy ertak",
#         "chop etilgan yili": 1943,
#         "tarjimalar soni": 300
#     }
# }

# nom = input("kitob: ").lower()
# topildi = False
# for kitob in books:
#     if kitob.lower() == nom:
#         print("Muallifi:", books[kitob]["muallifi"])
#         print("Janri:", books[kitob]["janri"])
#         print("Chop etilgan yili:", books[kitob]["chop etilgan yili"])
#         print("Tarjimalar soni:", books[kitob]["tarjimalar soni"])
#         topildi = True
#         break
# if topildi == False:
#     print("kitob topilmadi: ")
