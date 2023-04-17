# # # # days_remaining = int(input("Enter the number of days until your next birthday - "))
# # # # weeks_remaining = days_remaining //7
# # # # print(f"the number of weeks remaining for your next birthday is {weeks_remaining}")
# # #
# # # zoo = ['tiger','lion','snake','crow','cheetah']
# # # zoo.pop(3)
# # # zoo.append('elephant')
# # # zoo.remove('cheetah')
# # # # print(zoo)
# # # # print(zoo[0:3])
# # #
# # #
# # # grade = 99
# # # if grade>=90 and grade<=100:
# # #     print("A")
# # # elif grade >=80 and grade<=89:
# # #     print("B")
# # # elif grade >=70 and grade<=79:
# # #     print("C")
# # # elif grade >=60 and grade<=69:
# # #     print("D")
# # # elif grade >=0 and grade<=59:
# # #     print("F")
# # # else:
# # #     print("Enter a valid value")
# # #
# #
# #
# #
# # my_list = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
# # x = 0
# # while x<3:
# #     x+=1
# #     for i in my_list:
# #         if i =="Monday":
# #             print("------")
# #             continue
# #         print(i)
# #
# #
# #
# # user_dictionary = {
# #     'username':'surya001',
# #     'name':'surya',
# #     'age':30
# # }
# # user_dictionary["married"] = False
# # print(user_dictionary)
#
#
# my_vehicle ={
#     "model":"ford",
#     "make":"explorer",
#     "year":2018,
#     "mileage":40000
# }
# vehicle2 = my_vehicle.copy()
# vehicle2["number_of_tires"] = 4
# for k,v in my_vehicle.items():
#     print(k,v)
#
# print("-------")
#
#
# vehicle2.pop("mileage")
# for k in vehicle2.keys():
#     print(k)

def user_details(firstname,lastname,age):
    return {"firstname":firstname,"lastname":lastname,"age":age}


print(user_details("surya","cs",30))