# DAV N1
# num1 = int(input("sheiynaet ricxi: "))
# if num1 > 0 and  num1 % 2 == 0:
#     print("The  number is positive and even.")

# else:
#     print("The number is positive and odd")


# DAV N2
# num1=int(input("sheybnet ricxvi: "))
# while num1 > 0:
#  print(num1)
#  num1 = int(input("შეიყვანე რიცხვი: "))

# DAV N3
# number =int(input("Enter Numbre: "))
# for i in range(number):
#   number =int(input("Enter Numbre: "))
#   if number > 3:
#     print("Acess Granted")
#     break
#   else:
#     print("ACess Denied")

# DAV N3 2
#   როგრო შეიძ₾ება  3 შეცდომის შემდეგ ფორ ციკლით აღმოვაჩინთ სეცდომა თუ ის ეარ შეიყვაენს რაც ჩვენ გვინდ
# break xვიყენებ რადგან მოხდეს შეწყვეტა ზუსტდა მაშნ როედასც მე მინდა და რძედაც მემიედ ათავიდა ინპუტი გარეთ მქონდა
# და არ გამოდიდა მეერ შიგნით შევიტანე რადგან ციკლს აღექვა აქ ნესტინგი გამოვიყენე რადგან 2-ოვე მეთოდი დამიკმაყოფილს
# ამის გარშე მხოლდმ ერთ If შეამოწმებდა და მორეჩებოდ ამიტომაც გამოვიყე ნესტინგი შემდენ ვეიბნები ვატვკევიებ რეინჯით
# ყველა შესაძ₾ოვარიანტს ანუ 100ლიმიტი გავიზარდე  ამით და ვეუბნები რომ 100 დატრალება აქვა ანუ 100 ჯერ შუძლია
# ნახოს ველიუ შემდეგ ვუმატებ ქოუნთით ანუ რადგან აქ შევიტანე ეს ნიშNავას რომ ავტომატურად მოიმატებს 1 ით
# რამდენინფოსაც შევიყვან ინპუტშ შემდეგ ვეძებ სწორი სიტყვას თუ პირველივეზე შეიყვანეს სწპრი სიტყვა მაშინ ბრეკით
# ვაჩერებ თუ არადა 3 ცდას ვუტოვებ თუ მეტა 3 ზე მაშნ გაწყვიტვა სციკლს და დააბრუნებს პასუხის
# count = 0
# for i in range(100):
#     inp = input("შეიყნაეთ ინფორმაცია: ")
#     count += 1
#     if inp == "luka":
#         print("Aces Granted:")
#         break
#     elif count > 3:
#         break
#     else:
#         print("Aces Denied:")


# DAV N4
# frutcis=["ვაშლი", "მსხალი", "ატამი", "ბანანი"]
# print(frutcis[2])


# DAV N5
# number_arey =[10,20,30,40,50]
# next_Changed=number_arey[1]=25
# print(number_arey)


# DAV N6
# veliu_eror=int(input("sheuyvanet ricxvebu: "))

# list_aey=["წითელი","ყვითელი","მწვანე","თეთრი","იასამნისფერი"]
# if veliu_eror==0:
#    print(list_aey[0])
# elif veliu_eror==1:
#    print(list_aey[1])
# elif veliu_eror==2:
#    print(list_aey[2])
# elif veliu_eror==3:
#    print(list_aey[3])
# elif veliu_eror==4:
#    print(list_aey[4])
# else:
#    print("Error bro")


# DAV N6.2
# lists_long=int(input("sheuyvanet ricxvebi: "))

# list_aey=["წითელი","ყვითელი","მწვანე","თეთრი","იასამნისფერი"]
# for i in range(len(list_aey)):
#  if i == lists_long:
#     print(list_aey[i])

# DAV N7
# enimals_list=["lomi","vefxvi","mainmuni","pingvini","mgeli"]
# roasted = enimals_list.pop()
# next_arr=enimals_list.append("gemi")
# print(enimals_list)

# DAV N7.2
# enimals_list=["lomi","vefxvi","mainmuni","pingvini","mgeli"]
# if len(enimals_list) > 15:
#     enimals_list.pop()
#     print(enimals_list)

# else:
#     enimals_list.pop()
#     enimals_list.append("gemi")
#     print(enimals_list)


# DAV N7.3
# enimals_list=["lomi","vefxvi","mainmuni","pingvini","mgeli"]
# cont=0
# for i in enimals_list:
#     cont += 1
#     enimals_list.pop()
#     enimals_list.append("gemi")
#     break
# print(enimals_list)


# DAV N8
# ამ კოდშ გამოვიყენე ძალიან მატივი და კარგი რამ უბრალოდ ვეუბენბირომ i გახდეს num რაც ნიNშავს რომ ეს ლისტი
# ავტომატურად ხდება იმ  შინანარსისმქონე რასაც შევიყვან num ში ანუ როდეასც შევიყვან 0 ადგება და  მთელი
# ლისტი გახდეაბ 0 დაშეიცვლება 0 ინდექსზე არსებული ელემენტ 1 შევიყვან და ეგ შეიცვლება
# ანუ i შემოივლის ყვეალ ელემენტს მასივში თავიდან მეგონა რომ ი შცვლიდა ყვლეა ელემნტს ერთ დროულად
#  რადგან i გადის ლისტის ყვეალ ელემენტს: და იქნებოდა მხოლოდო ოქროსფერი თუმცა როდეწასც გამოვიყენე  if i == num ესნიშნავს რომ i ვუტოლებ num
# და num -ში რასაც შევიყვან ავტომატურად ის ინდექასიგახდეაბ i და  შეიცვლება მხოლოდ ის ინდექსი როემლსაც
# შევიყვან num-ში
# num=int(input("sheiyvanet ricxvi: "))
# colr_list=["tetri", "shavi","mwvane","yviteli","witeli"]

# for i in range(len(colr_list)):
#     if i == num :
#      colr_list[i]="oqroasjsa"
#      print(colr_list)


# DAV N9
# nume_input=int(input("sheiyvanet ricxvebi: "))

# if nume_input % 2==0:
#     print("es aris luwi ricxvebi bro")
# else:
#     print("es ricxvi aris kenti")


# DAV N10
# elif nume_input>=15:
#     print("It's Warm")
# elif nume_input>=20:
#     print("It'saaa Warm")
# ამის მერორე ფორმაა ზემოთ
# nume_input=int(input("sheiyvanet ricxvebi: "))

# if nume_input >30:
#     print("It,s hot")


# elif  15 <=nume_input >=20 :
#     print("It's Warm")
# else:
#     print("It's Cold")


# DAV  N11
# num=int(input("sheiyvanet ricxevbi: "))
# if num == 0:
#     print("Negative")
# elif  num % 2 == 0:
#     print("Positive odd")
# else:
#     print("Positive even")


# DAV N12
# next_int=int(input("sheiiyvanet ricxvebi: "))
# for i in range(next_int):
#     if i % 2 == 0:
#         print(f"{i} Even")
#     else:
#      print(f"{i} Odd")


# DAV N12.2
# num = int(input("sheiyvanet ricxvi: "))

# count = abs(num)

# if num % 2 == 0:
#     for i in range(count):
#         print(f"{i} Even")
# else:
#     for i in range(count):
#         print(f"{i} Odd")


# DAV N13
# positive = 0
# negative = 0
# zero = 0
# for i in range(10):
#     num = int(input("sheiyvanet ricxvi: "))

#     if num > 0:
#         positive += 1
#     elif num < 0:
#         negative += 1
#     else:
#         zero += 1
# print("Positive:", positive)
# print("Negative:", negative)
# print("Zero:", zero)


# DAV N14
# fruits = ["apple", "banana", "orange", "grape"]
# fruits[1]="kivi"
# print(fruits)

# DAV N14.2
# fruits = ["apple", "banana", "orange", "grape"]
# for i in fruits:
#     if i=="banana":
#       fruits.remove(i)
#       fruits.append("kivi")
# print(fruits)

# DAV N15
# nums = [4, 8, 12, 16, 20]
# res=0

# for i in range(len(nums)):
#     if i==0:
#       res+=nums[i]
#     elif i==len(nums)-1:
#          res+=nums[i]
# print(res)

# DAV N16
# lists_big=[1,2,3,4,5,6,8,9,12,13,33,122,111]
# for i in lists_big:
#     print(i)

# DAV N17
# lists_big=[1,2,3,4,5,6,8,9,12,13,33,122,111]

# for i in lists_big:
#     if i % 2 == 0:
#         print(i)


# DAV N18
# lists_big=[1,2,3,4,5,6,8,9,12,13,33,122,111]
# total=0
# for i in lists_big:
#     if i % 2 == 0:
#      total+=i

# print(total)


# DAV N19
# lists_big=[1,2,3,4,5,6,8,9,12,13,33,122,111,112,114,1112,11012,1243]
# for i in  lists_big :
#      if i > 6:
#         print(i)


# DAV N20
# question=input("sheiyvanet tqasti: ")

# for i in question:
#     i.split(" ")
#     print(i)

# DAV N21
# lists_big=[1,2,3,4,5,6,8,9,12,13,33,122,111,112,114,1112,11012,1243]

# for i in range(len(lists_big)):
#     if i < 3:
#      print(lists_big[i])


# DAV N21.2
# lists_big=[1,2,3,4,5,6,8,9,12,13,33,122,111,112,114,1112,11012,1243]

# for i in range(3):
#     print(lists_big[i])


# DAV N22
# for i in range(50,200):
#     print(i)


# DAV  N23
# for i in range(300):
#     if i % 2 ==0:
#         print(i)


# DAV N24
# for i in range(100,150):
#     if i % 2 !=0:
#         print(i)


# DAV N25
# conect=1
# while conect < 50:
#     conect+=1
#     print(conect)


# DAV N26
# coment=20
# while coment < 60:
#     coment +=5
#     print(coment)

# DAV  N27
# num = input("sheiyvanet gvri: ").strip()
# for i in num:
#     print(f"${i} მისი გვარია: ")


# DAV N28
# ამ შემთვევეაშ გამვიყენე მარტივი რამ ჯერ შევადარე თვითონ ნუმ რადგან ციკლშ არ იჭერდა ყვეალფერს ერთა შემდეგ ვეუყბნები:
# რომ  თუ ი გაყოფილი 2 ზე ნაშთი არის 0 მაშნ გამოიტანის ის როცხვები რომლებიც 2 ზე უნაშთოდ იყოფა
# ანუ ყოველი მე 2 რიცხვი რისშ დეგადაც გამოაქსვ კიდეც
# num = int(input("sheiyvanet ricxvebi: "))

# if num == 0:
#     print(f"$ {num} Out of stock")
# else:
#     for i in range(num):
#         if i % 2 == 0:
#             print(f" ${i} You have bought the drink")


# DAV N29
# number=50
# while number > 20:
#     number-=3
#     if number ==20:
#         print(f"${number} shesrulebulia")
#     print(number)

# DAV  N30
# num=150
# while num >0:
#     num-=1
#     print(f"${num} next numbers:")


# DAV N1

# fructis=["qindzi","mwvanili","kombosto","cahrkhali"]
# fructis[0]="prasi"
# fructis[3]="stapilo"
# print(fructis)

# DAV N1.2
# fructis = ["qindzi", "mwvanili", "kombosto", "cahrkhali"]
# new_items = ["apple", "banana"]

# for i in range(len(fructis)):
#     if i >= len(fructis) - 2:
#         fructis[i] = new_items[i - (len(fructis) - 2)]

# print(fructis)


# DAV N3
# როგრო რეაგირებს ლსიტები სტინგებზე  მათში სტრონგებს აქვთ კნკრეტული რიგები რაც იშNავს იმას რომ
# როდეასც ვწერთ რაიმე სიტყვას ეს სიტყვა იშლება და ინომრება მაგ :
# l="luka"
# print(l[0])//l
# print(l[1])//u
# print(l[2])//k
# print(l[3])//a

# DAV N4
# lsists=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(lsists[4:10])

# DAV N5
# cosmos = ["marsi", "venerea", "dedamiwa", "saturn", "uran", "neftum"]

# for i in cosmos:
#     if len(i) % 2 == 0:
#         print(f"${i} luwia")
#     else:
#         print(f"${i} kentia")


# DAV N 6
# listnumber=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# for i in listnumber:
#     if i % 2==1:
#      print(f"${i} kentia")


# DAV N7
# person="Luka Tabagari"
# for i in person:
#     print(i[0:1])

# DAV N8
# userpolidorm = input("sheiyvanet sityva: ").strip()
# if userpolidorm == userpolidorm[::-1]:
#     print(f"${userpolidorm} POLIDORM:")
# else:
#     print("NO POLIDORM:")


# DAV N9
# words = ["gaarjoba", "gagimarjos", "mgeli", "lomi", "vefxvi"]
# rest_words = words[::-1]
# count = 0
# for words in rest_words:
#     count += 1
#     if count % 2 == 0:
#         print(f"${count} luwia")
#     else:
#         print(f"${count} kentia")

# DAV N10
# userreturn=input("sheiyvanet sityva: ").strip()
# nexst_wordreturn=userreturn[::-1]
# print(nexst_wordreturn)

# DAV N11
# big_words="georgia is biutiful  l like programing languages"
# first=big_words[0:7]
# first=big_words[:]
# first=big_words[::-1]
# first=big_words[:10]
# first=big_words[:-28]
# print(first)