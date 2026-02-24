# N1 bolean მონაცემთა ტიპი არის ისეთი მონაცემები რაზედაც არის ზოგადად პროგრამირება დაფუძნებული
# კი ან არა Trut ან False  ყველაზე მარტივად რომ ავხსნა
# ვიტყვი შედეგს რო როდეაც რაიმეს აქვს შნაარის და არ არის ცარიელი მაშნ აღიქმება ლოგიკურად სიმართლედ
# აუ თუ x=0 დაამს შევიყვან  ბულეანში მაშინ მეტუვის რომ ეს არის ტყუილი
# ხოლო მას რომ ქონდეს მნიშვნელობა რიცხვი გარდა 0 ისა ის აღიქმებოდა როგორც სიმართლედ:
# სტრინგებზეც ეგრეა როდესც რაიმე არის ცარიელი x="" იქნება აღქმული როგრც ტყუილი False
# ხოლო რომ ქონდეს მნიშვნელობა მაშინ აუ ველიუ არ იყოს ცარიელი იქნებოდა True


# N2 binar code ბინარული კოდი არი ლოგიკური კი არა ანუ 0-ები და 1-ები
# ლოგიკური 0  ნიშნავს არაფერეს უარყოფას False-ეს ხოლო ლოგიკური 1 ნიშნასვ True
# ერთი მაგალითი შეიძლება მოვიყვანოთ რომ როდესაც შუქი აინთება ისე არის 1 ანუ მოქმდება სწორა შესრულდა
# ხოლო როდესაც ჩაქრება გადხება 0 და ჩაქრება სინათლე ანუ ცარიელი იქნება


# N3bool function ბულ ფიუნქცია არის ბოლიანის ფუნქცია ანუ True False ტიპის
# თუ რაღაც არის ინფორმაცია აღიქმება 1-True ხოლო თუ ცარიელია აღიქმება 0 ად და დაბრუნდება False
# x = "Hello"
# print(bool(x))//True

# y = 15
# print(bool(y))//True

# x = ""
# print(bool(x))//False

# y = 0
# print(bool(y))//False


# N4
# a=input("შეიყვანეთ პირველი რიცხვი")
# b=input("შეიყვანეთ მეორე რიცხვი!")

# if len(a)==0 or len(b)==0 :
#     print("გთხოვ შეიყვანოთ მნიშვნელობები!")
# elif a == b:
#     first=int(a)
#     second=int(b)
#     print("მიღებულა პასუხი")

# else :
#     print("დაფირქსირდა შეცდომა!")


# N5

# firstNumber=input("შეიყვანეთ პირველი რიცხვი!")
# seconndNumber=input("შეიყვანეთ მეორე რიცხვი!")
# firstNumber=int(firstNumber)
# seconndNumber=int(seconndNumber)

# if firstNumber > seconndNumber :
#     print("პირველი რიცხვი მეტია მეორეზე!")

# elif seconndNumber > firstNumber:
#     print("მერე რიცხვი მეტია პირველზე!")
# else :
#     print("დაფიქსირდა შეცდომა!")

# N6
# punCh_string=input("შეიყვანეთ პაროლი!")
# neW_stirng=punCh_string.title()

# if neW_stirng =="Python":
#     print("მიღებულია!")
# else  :
#     print("გთხოვთ ზუსტად შეიყვანოთ პაროლი!")


# punCh_string=input("შეიყვანეთ პაროლი!").strip()
# neW_stirng=list(punCh_string)

# if neW_stirng[0] == "p":
#     print("")
#     if "".join(neW_stirng) == "Python":
#       print("მიღებულია პაროლი!")

#     else:
#         print("გთხოვთ ზუსტად შეიყვანოთ პაროლი!")
# else:
#     print("გთხოვთ ზუსტად შეიყვანოთ პაროლი!")


# N7

# inpuT_Number = input("შეიყვანეთ რიცხვი!").strip()

# if not inpuT_Number.isdigit():
#     print("გთხოვთ შეიყვანოთ მხოლოდ რიცხვები!")
# else:
#     inpuT_Number = int(inpuT_Number)
#     if inpuT_Number > 100:
#         print("მეტია 100-ზე")
#     else:
#         print("არ არის მეტი 100-ზე")


# N8

# pasworLd_inp=input("შეიყვანეთ პაროლი").strip()

# if pasworLd_inp =="" :
#     print("შეიყვანეთ პაროლიი!!!")
# elif  pasworLd_inp.startswith("Python123") :
#     print("მიღებულია!")

# else :
#     print("errrr!")


# N9
# comparIsOn_inp=input("შეიყვანეთ პირევლი რიცხი!")
# comparIsOn_inpp=input("შეიყვანეთ მეორე რიცხი!")
# comparIsOn_inp=int(comparIsOn_inp)
# comparIsOn_inpp=int(comparIsOn_inpp)

# if comparIsOn_inp > comparIsOn_inpp :
#     print("პირველი რიცხვი მეტია მე 2 რიცხვზე")
# elif comparIsOn_inp < comparIsOn_inpp :
#     print("პირველი რიცხვი ნაკლებიე მე 2 რიცხვზე ")
# elif comparIsOn_inp == comparIsOn_inpp:
#     print("ტოლი რიცხვებია")
# else :
#     print("error")

# N10

# str1 = input("შეიყვანეთ ერთი სიტყვა!").strip()
# str2 = input("შეიყვანეთ ერთი სიტყვა!").strip()
# str3 = input("შეიყვანეთ ერთი სიტყვა!").strip()
# str4 = input("შეიყვანეთ ერთი სიტყვა!").strip()
# str5 = input("შეიყვანეთ ერთი სიტყვა!").strip()

# word_List = f"{str1} {str2} {str3} {str4} {str5}"
# lists_Gap = word_List.split(" ")

# if len(str1.split()) > 1:
#     print(f" 0  Index აქვს ერთძე მეტი ველიუ!{str1}")
# else:
#     print(f"Indexი 0 სწორია: {str1}")

#     if len(str2.split()) > 1:
#         print(f"პირველ Index აქვს ერთზე მეტი ველიუ!{str2}")
#     else:
#         print(f"Indexი 1 სწორია {str2}")

#         if len(str3.split()) > 1:
#             print(f"2 Index აქვს ერთზე მეტი ველიუ!{str3}")
#         else:
#             print(f"Index 2 სწორია {str3}")

#             if len(str4.split()) > 1:
#                 print(f"3 Index აქვს ერთზე მეტი ველიუ!{str4}")
#             else:
#                 print(f"index 3 is True")

#                 if len(str5.split()) > 1:
#                     print(f" 4 Index აქვს ერთზე მეტი ველიუ!{str5}")
#                 else:
#                     print("index 4 სწორია!")


# ამ კოდიშ მთვარრი გარდამტეხი როლს თამაშიბს  len(str5.split()) > 1 ეს ხაზი რადგან
# როდესც ვწერ len ეს ნიშNავს რომ მე ვათვლევინებ რაღაცას მატემატიკურად ხოლო str5 ეს ნიშNავს რომ კონკრეტულად ამაზე
# ვათვლევინებ შემდეგ რაც შეეხება split() ეს ამ შემთვევეაშ ესე მოქდმებს რომ სადაც ნახავას სფეისს
# აღიქვამს სხავ სიტყვად ჩვეულებრივად მსგავსად მოქმდებს split(" ") -ეს თუმცა ამ შეთვევაში
# მხოლოოდ სოლიტი და ფრჩხილები აკეთებს ამას ხოლო შედმეგ ვეუბენბით რომ თუ ის მეტია 1 ზე
# ანუ თუ მოხდა ისე რომ ერთის გარდა ჩაიწერა სხვა სიტუვა ანუ დაფიქქსირდა სფეისი მაშინ ხდეა
# უკვე შესაბამის პასუხსი დაბურნებაც თუ არადა esle ერთვება სააქმეში


# N11
# number1 = input("შეიყვანეთ პირველი რიცხვი: ")
# number2 = input("შეიყვანეთ მეორე რიცხვი: ")


# number3 = input("შეიყვანეთ მეორე რიცხვი:")
# number4 = input("შეიყვანეთ მეორე რიცხვი:")

# symbols = input("შეიყვანეთ სიმბოლოები (/ * - +): ")



# if number1 == "" or number2 == "" or number3 == "" or number4 == "":
#     print("გთხოვთ შეიყვანოთ რიცხვები:")
# else:
#     number1 = int(number1)
#     number2 = int(number2)
#     number3 = int(number3)
#     number4 = int(number4)


# if symbols == "+":
#    print(number1 + number2 +number3 + number4)

# elif symbols == "-":
#      print(number1 - number2 - number3 - number4) 

# elif symbols == "*":
#     print(number1 * number2 * number3 * number4)

# elif symbols == "/":
#      print(number1 / number2 / number3 / number4)

# else :
#     print("არასწორი ოპერატორი")

# # }


# N12
# porveli varianTi
# bull = True
# number=1121
# numbeRs=2.2
# stR_Ing="l lkie my work"

# print(type(bull))
# print(type(number))
# print(type(numbeRs))
# print(type(stR_Ing))


# meroe varianTi
# bole_An=True
# Number_Rr=10
# NUmbers=1.2
# Strin_Gs="UFC-CHAMP"

# if type(bole_An)  != bool:
#     print("ERROR")
# else :
#     print("it's bUl_Ean")

#     if type(Number_Rr) != int:
#         print("ERROR")
#     else:
#         print("it's int NUmber")

#         if type(NUmbers) != float:
#               print("ERROR")
#         else:
#             print("It'S float N_Umber")

#         if type(Strin_Gs) != str:
#              print("ERROR")
#         else:
#             print("It'S St_Ri_NG")



# N13

# first_boy=input("შეიყვანეთ ტექსტი:")
# second_Boy= input("შეკყვანეთ ტექსტი:")

# if first_boy !=second_Boy:
#     print("მონცემები არ ემთხვევეა ერთმანეთს!")
# else:
#     print("იდენტურია")



# N14
# num1=input("შეიყვანეთ რიხვები!").strip()
# # num1=int(num1)
# num2=input("შეიყვანეთ რიხვები!").strip()
# # num2=int(num2)
# num3=input("შეიყვანეთ რიხვები!").strip()
# # num3=int(num3)

# if num1.isdigit()  and num2.isdigit() and num3.isdigit() :
#     print("მიღებულია")
# else:
#     print("მიუღებელია")



# num1 = input("შეიყვანეთ რიცხვი 1: ").strip()
# num2 = input("შეიყვანეთ რიცხვი 2: ").strip()
# num3 = input("შეიყვანეთ რიცხვი 3: ").strip()


# if not num1.isdigit():
#     print(f"შეცდომა: '{num1}' რიცხვი არ არის")
# elif int(num1) != 30:
#     print(f"რიცხვი {num1} არ ემთხვევა 30-ს")
# elif not num2.isdigit():
#     print(f"შეცდომა: '{num2}' რიცხვი არ არის")
# elif int(num2) != 40:
#     print(f"რიცხვი {num2} არ ემთხვევა 40-ს")
# elif not num3.isdigit():
#     print(f"შეცდომა: '{num3}' რიცხვი არ არის")
# elif int(num3) != 50:
#     print(f"რიცხვი {num3} არ ემთხვევა 50-ს")
# else:
#     print("!ყველა რიცხვი სწორია!")





# სულ ჯამშ არის 15 დავალება რაც გავაკეთე