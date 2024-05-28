# language = ["css", "c++" , "pythoni" , "ruby" , "c"]

# print(language[2])

# favorite = language[0]

# print(language[0])

# print(language[-5])



# დავალება1) შევქმნათ სია საყვარელი კინოების ან სერიალების,რომელსაც შევინახავთ ცვლადში. საბოლოოდ გამოვიტანოთ სია.
favourite_movies = ["chinuri zodiaqo",  "harry potter" , "hobbit"]
print(favourite_movies)

# დავალება2) სიიდან დავბეჭდოთ ერთი კონკრეტული მნიშვნელობა index-ით
print(favourite_movies[2])

# დავალება 3) შევქმნათ მეორე ცვლადი, რომლის სახელი იქნება საყვარელი კინო და მის მნიშვნელობას წინა სიიდან წამოვიღებთ
favourite_film = (favourite_movies[1])

# დავალება4) მასივიდან ბოლო ელემენტი უარყოფითი index-ით წამოიღეთ. ასევე გამოიტანეთ ბოლოდან მეორე ელემენტი, ისევ მინუსიანი ინდექსით
favourite_film = (favourite_movies[-2])

# დავალება5) მომხმარებელს შევეკითხოთ საყვარელი მანქანის ბრენდი, რომელსაც შევინახავთ ცვლადში. შემდეგ ეს ცვლადი ჩასვით სიაში და გამოვიტანოთ print-ით, მაგ: print([brand_variable_name_here])
car_brends = ["bmw" , "audi", "golfi" , "mersedes"]

car_brend =input("what is your favourite car brend ")




language = ["css", "c++" , "pythoni" , "ruby" , "c"]

print(language[0:4])
print(language[0:5:2])




my_arrary = []
for number in range(50, 101):

    my_arrary.append(number)

    print(my_arrary[-10:])