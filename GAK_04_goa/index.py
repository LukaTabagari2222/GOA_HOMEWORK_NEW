# DAV N1
#  BIg_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# total = 0
# for i in BIg_lists:
#     total = total + i
#     print(total)
# DAV N1.2

# BIg_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# for i in BIg_lists:
#     print(i)
# ამ შემთხვეეაშ გვაქვს ლისტი რომელშიც არი 20 - ინდექსი შესაბამისად ხდება ის რომ მათი საერთო ჯამის ათვლა ხდება ანუ ჯერ
# 1+2=3 3+3=6 6+4=10 10+5=15 15+6=21 .....  ასევე შეიძ₾ება რომ ეს ყვლა რიცხვის დაჯამებაც მოხდეს მაგ: 1+2=3 3+3=6 ამათი ჯამი 3+6=9 და ასე შემდეგ
# თუმცა ეს არ მაქვს დავალებაში


# BIg_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# for i in BIg_lists:
#     if i % 2 == 0:
#         print(i)

# ამ შემთვევეაშ იფ გამოვიყენე  რადგან ლოგიკა გამოსულიტყო ამის გარეშე ციკლი ვარდება იშლება:

# DAV N3.1
# BIg_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# max_number = BIg_lists[0]
# for i in BIg_lists:
#     if i > max_number:
#         max_number = i
# print(max_number)
# # DAV N3 .2
# BIg_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# max_number = BIg_lists[0]
# for i in BIg_lists:
#     if i < max_number:
#         max_number = i
# print(max_number)

# DAV N4
# BIg_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# for i in BIg_lists :
#   if i % 2 !=0 :
#     print(i)


# DAV N5
# number = int(input("Enter number (0 to stop): "))
# while True:
#   if number == 0 :
#     print(f"{number} migebulia: 0")
#     break
#   else:
#     print("sheiyvbent 0")
#   number = int(input("Enter number (0 to stop): "))


# DAV N6
# გამიჭირადა ამის გკეთება რადგან ლოგიკა ამერეია შესაბამიად ცოყტა ვიწვალე რადგან for-თავისებური მიდგომა უნდა
# 2 სთ ვაკეთებდი ან 3
# next_Input = input("sheiyvanet ricxvebi: ")

# if next_Input== "":
#     print("sheivnet ricxvebi")
# else:
#     numbers = []
#     for x in next_Input.split():
#        num = int(x)
#        numbers.append(num)

#        if num == 0:
#            print(f"გიპოვნე 0 {numbers}")

#        else:
#            print(f"მოიძებნა შეუძლებელია: {numbers}")


# DAV N7
# BIg_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# x = 20
# while  x < 50 :
#    x +=1
# print(BIg_lists)
# მე 2 მეთოდი:
# number = 20
# while number < 50:
#   number+=1
#   print(number)


# DAV N8
# num = 0
# while num < 100:
#     num+=1
#     print(num)

# num = 0
# for i in num:
#   if i < 100:
#     i+=1
#     print(i)


# DAV N9
# num=[0]
# for x in num:
#    if len(num) < 100:
#      num.append(len(num))
# print(num)

# გამიჭრიდა ციკლებთან ლოგიკური მუშაობა რადგან ვერ აღვიქვი დამოუკიდებლად სამწუხაროდ:
# num = []

# i = 100
# while i >= 0:
#     num.append(i)
#     i -= 1
#     print(i)

# DAV N10
# for i in range(10,21):
#       print(i)

# r = range(10, 20)

# i = 0
# while i < len(r):
#     print(r,i)
#     i += 1

# DAV N11

# for i in range(100,205,5):
#     print(i)

# DAV N12
# counter += 1 არ არის დაკავშირებული list-თან
# როგორც მონაცემთან. ის უბრალოდ არის შენი საკუთარი ლოგიკური ცვლადი, რომელსაც ვიყენებ დათვლისთვის.
# ანუ ეს counter არანაირ კავშირიში არ არ სი ლისტთან არანაირშ საერთოდ არ შედის მაშში უბრალოდ ვადრრით ლისტს
# რაც ნუშNავს რომ ლისტს მიყვება ციკლი და რადგან +=1 მიწერია ეს ნიშნავს რომ რადგაგ counter ციკლშა იმდენჯერ დაემატება +1 რამდენითაც გავა
# ციკლიში იმდეჯერ დაემატება 1 ხოლო შმდეგ უბრალოდ ვაჩერებ break-ით რაც ნიშნავს რომ გაჩეერდეს დამთვლელი counter თორ ამას უშვალოდ ლისტთან
# არანაირი კავშირი არ აქვს.
# listss = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# counter = 0
# for i in listss:
#     print(i)
#     counter += 1
#     if counter == 10:
#         break

# DAV N12.2
# listss = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# i=0
# while i < len(listss):
#     print(i)
#     i+=1
#     if i ==11:
#        break


# DAV N12.3

# n=11
# i= 0
# while i < n:
#     print(i)
#     i+=1


# DAV N13
# num_big=int(input("შეიყვანეთ რიცხვები:"))

# if num_big < 0:
#     print("რიცხვი უარყოფითია: ")
# elif num_big > 0:
#     print("რიცხვი დადებითია: ")
# else:
#     print("რიცხვი ტოლია 0-ის:")


# DAV N13.1
# ამ შემთხტვეაშ გადაყავს სპლიტს ლისტად და შემდგ ვატარებთ ციკლში სტრინგად წამოსულ num_big-ის ვაქცევთ რიცხვებად და შემდეგ: ამ რიცხვებს ვუკეთებთ
# შედარებას თუ ნაკლებია 0-ზე ანუ უარყოფითია თუ მეტაი 0-ზე ანუ დაადებითია და სხვა შემთხვეევაშ ანუ როდესაც არის 0-ის ტოლი ელსი მუშოავდება
# რადგან სხავ ლოგიკა ყველა ავტომატურად გაკეთებულაი რიცხვი ანუ 0 ზე მეტია ან არა:
# for ციკლი გადის იმ ელემენტებზე, რაც input-იდან მიიღე (list-ზე), და თითოეულ ელემენტზე ცალ-ცალკე სრულდება ეს ნაწილი:
# ანუ იფ შდაც და ელსიშდაც:
# აქ რომ ყოფილიყო მხოლოდ სტრინგი სპლიტის გარეშე ეს იქნებოდა რომ აღიქვამდა თითოულ სიმბოლოს მაგ:helo h,e,l,o შესაბამისად არ აღიქვებოდა
# სიტყვებად არამედ თითოული ცალ ცალკე სიმბოლოდ რაც არ მომცემდა შესაბამის შედეაგ ამიტომაც გავაეკთე სპლიტი რომ დაყოს თთოული ცალ ცალკე სვეტებად

# num_big=input("შეიყვანეთ რიცხვები:")
# num=num_big.split()

# for num_big in num:
#     num_big=int(num_big)

# if num_big < 0:
#     print("რიცხვი უარყოფითია: ")
# elif num_big > 0:
#     print("რიცხვი დადებითია: ")
# else:
#     print("რიცხვი ტოლია 0-ის:")


# DAV N14
# number_strongtesting=int(input("შეიყვანეთ რიცხვები: "))
# if number_strongtesting > 0 and number_strongtesting <= 12:
#     print(f"{number_strongtesting} ბავში ხართ!: ")
# elif number_strongtesting >= 13 and number_strongtesting <= 19:
#     print(f"{number_strongtesting} თინეიჯერი ხართ!: ")
# elif number_strongtesting > 20 and number_strongtesting <=64:
#     print(f"{number_strongtesting} ზრდასრული ხართ!: ")
# elif number_strongtesting >=120:
#     print(f"{number_strongtesting} ყოჩაღ შენ!: ")
# else:
#     print("მინუსიაა!: ")

# DAV N14.1
# number_strongtesting=int(input("შეიყვანეთ რიცხვები: "))
# if number_strongtesting < 0:
#     print(f"{number_strongtesting} არასწორი ინფო!: ")
# elif number_strongtesting >= 120:
#     print(f"{number_strongtesting} ყოჩაღ შეენ!: ")
# elif number_strongtesting >= 65:
#     print(f"{number_strongtesting} ხანში შესული ხართ!: ")
# elif number_strongtesting >= 20:
#     print(f"{number_strongtesting} ზრდასრული ხართ: ")
# elif number_strongtesting >= 14:
#     print(f"{number_strongtesting} მოზარდი/თინეიჯერი ხარ ")
# else:
#     print("ბავში ხარ!: ")


# DAV N14.2
# number_strongtesting=input("შეიყვანეთ რიცხვები: ")
# num_break=number_strongtesting.split()
# for number_strongtesting in num_break:
#     number_strongtesting=int(number_strongtesting)
# if number_strongtesting < 0:
#     print(f"{number_strongtesting} მინუსია!: ")
# elif number_strongtesting >= 120:
#     print(f"{number_strongtesting} ყოჩაღ შეენ!: ")
# elif number_strongtesting >= 65:
#     print(f"{number_strongtesting} ხანში შესული ხართ!: ")
# elif number_strongtesting >= 20:
#     print(f"{number_strongtesting} ზრდასრული ხართ: ")
# elif number_strongtesting >= 14:
#     print(f"{number_strongtesting} მოზარდი/თინეიჯერი ხარ ")
# else:
#     print("ბავში ხარ!: ")


# # DAV N15
# num_1 = int(input("Enter the first number!: "))

# num_2 = float(input("Enter the scond number!: "))

# num_3 = float(input("Enter the third number!: "))

# if num_1 >= num_2 and num_1 >=num_3:
#     print(f"big Number is {num_1}")

# elif num_2 >=num_1 and num_2 >= num_3:
#     print(f"big Number is {num_2}")

# else:
#     print(f"big Number is {num_3}")


# DAV N16
# daysof_theweek = input("შეიყვანეთ რიცხვები 1-7 მდე:! ").strip().lower()

# if daysof_theweek == "":
#     print("ცარიელია შეიყვანეთ ტექასტი:")
# elif daysof_theweek == "1":
#     print(f"{daysof_theweek} ორშაბათი!")
# elif daysof_theweek == "2":
#     print(f"{daysof_theweek} სამშაბათი! ")
# elif daysof_theweek == "3":
#     print(f"{daysof_theweek} ოთხშაბათი! ")
# elif daysof_theweek == "4":
#     print(f"{daysof_theweek} ხუთშაბათი! ")
# elif daysof_theweek == "5":
#     print(f"{daysof_theweek} პარასკევი! ")
# elif daysof_theweek == "6":
#     print(f"{daysof_theweek} შაბათი! ")
# elif daysof_theweek == "7":
#     print(f"{daysof_theweek} კვირა! ")
# else:
#     print("მსგავსი კვირსის დღე არ არსებობს!: ")



# DAV N16.1
# dayof_wiiik = input("შეიყვანეთ კვირის დღეები!: ").strip().lower()
# nexst_wiKbreik=dayof_wiiik.split()
# for dayof_wiiik in nexst_wiKbreik :
#     if dayof_wiiik[0]=="1":
#         print(f"{dayof_wiiik} ორშაბათი! ")
#     elif dayof_wiiik[0]=="2":
#         print(f"{dayof_wiiik} სამშაბათი! ")
#     elif dayof_wiiik[0]=="3":
#         print(f"{dayof_wiiik} ოთხშაბათი! ")   
#     elif dayof_wiiik[0]=="4":
#         print(f"{dayof_wiiik} ხუთშაბათი! ")
#     elif dayof_wiiik[0]=="5":
#         print(f"{dayof_wiiik} პარასკევი! ")
#     elif dayof_wiiik[0]=="6":
#         print(f"{dayof_wiiik} შაბათი! ")    
#     elif dayof_wiiik[0]=="7":
#         print(f"{dayof_wiiik} კვირა! ")  
#     else :
#         print("არ არსებობს!")


# DAV N17
# number_print =int(input("Enter number!: "))
# if number_print > 50:
#     print(f" result: {number_print * 5}")
# else:
#     print(f"the square of a number: {number_print * number_print}")

# DAV N18 

# enter_PAsworld = input("Enter pasworld!: ").strip().lower()

# if enter_PAsworld =="":
#     print("objact is clear!:")
# elif enter_PAsworld == "goa123":
#     print(f"{enter_PAsworld}: Password is correct!")
# else:
#     print("Incorrect password! ")



# DAV N19 
# num1=int(input("შეიყვანეთ რიცხვი:! "))

# count = 0
# for i in  range(1 , num1 + 1):
#     count+=i
#     print(count)


