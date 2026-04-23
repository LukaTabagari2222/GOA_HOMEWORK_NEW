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


# 1) შექმენით სია სადაც ჩამოწერეთ 4 ბოსტნეულს, შემდეგ თქვენთვის ყველაზე 2 არასასურველი ამ სიიდან ჩაანცვლეთ ახალი ელემენტებით

# 2) მომხმარებელს შემოატანინეთ რიცხვი 0-იდან 4-მდე და შეინახეთ ის "user_choice"-ის ცვლადში, შემდეგ ბოსტნეულსი სიიდან დაუბეჭდეთ ის ელემენტი რომელიც მომხმარებელმა აირჩია, ესეიგი იმ user_choice ინდექსზე მყოფი ელემენტი სიაში

# 3) ახსენით რას ნიშნავს რომ list და string არის დალაგებული მიმდევრობები, კომენტარებით დაწერეთ მათ თვისებებს შორის განსხვავებები. მოიყვანეთ მაგალითები

# 4) შექმენით სია რომელშიც ჩამოწერეთ რიცხვებს 1-იდან 20-ის ჩათვლით. slicing-ის საშვალებით გამოიტანეთ რიხცები 5-იდან 10-მდე

# 5) შექმენით სია ციური სხეულებზე სიტყვებით და შემდეგ გამოიტანეთ მხოლოდ ის ელემენტები, რომლებიც ლუწ ინდექსებზე დგანან

# 6) შექმენით სია 0-დან 15-მდე რიცხვებით. გამოიტანეთ მხოლოდ ის რიცხვები, რომლებიც კენტ ინდექსებზე დგანან

# 7) შექმენით string რომელშიც შეინახავთ თქვენს სახელსა და გვარს, შემდეგ ცალ ცალკე გამოიტანეთ ამ სტრინგიდან ჯერ სახელი და შემდეგ გვარი slicing-ის საშვალებით

# 😎 მომხმარებელს შემოატანინეთ სიტყვა, შემდეგ if-ით შეამოწმეთ ეს სიტყვა თუ თავისი თავის ტოლია როდესაც შემოაბრუნებთ (slicing-ის დახმარებით), თუ ასეა დაბეჭდეთ რომ განსაკუთრებული (ასეთ სიტყვებს palindrome ჰქვია) სიტყვაა, სხვა შემთხვევაში კი დაბეჭდეთ რომ ჩვეულებრივი სიტყვაა

# 9) შექმენით სიტყვების სია, შემდეგ მის შემობრუნებულ ვერსიას გადაუარეთ for ციკლით, დაბეჭდეთ ყოველი მეორე ელემენტი (რომ გაიგოთ ყოველი მეორე აიღეთ ცვლადი რომელიც თავიდან 0 იქნება, ყოველ გამეორებაზე კი გაზრდით ერთით და შეამოწმეთ ლუწია თუ კენტი)

# 10) მომხმარებელს შემოატანინეთ სიტყვა და დაბეჭდეთ ის შებრუნებულად

# 11) შექმენით ცვლადი რომელშიც შეინახავთ თქვენთვის სასურველ string-ს, უნდა იყოს მინიმუმ 20 სიმბოლო, შემდეგ slicing-ის საშვალებით დაბეჭდეთ ეს string ხუთგვარად შემდეგი პირობებით: