str1 = "The Wako R&D Center in January, 1984 began the basic research on a new drive system, as a means of achieving a shift from Honda’s FF " \
       "(front-engine/front-wheel drive) vehicle type to another format. In those days, FF was the mainstream of Honda cars, and Honda models used " \
       "it to ensure superior interior comfort and accommodations."

str2 = "However, the development team believed a change in drive format could enhance the flexibility of frame design and packaging. " \
      "Therefore, the focus of research was to be to an underfloor, midship-engine rear-wheel drive (UMR) format. " \
      "This could combine higher packaging efficiency along with the sporting characteristics with which rear drive was associated." \
      "During the test drive, the team members were amazed by the unique handling of the car, which differed greatly from the original FF specification. " \
      "The UMR-version City, in fact, demonstrated superior performance characteristics. Unfortunately, further development had to be set aside because the " \
      "level of technology then available to Honda placed certain limits on the car’s ability to present any real advantage over the normal FF version." \
      "However, although the project was shelved, the team members simply could not forget the exhilaration they had experienced with the UMR experiment. " \
      "Moreover, comments had been raised by supporters at the evaluation meetings that the rear-drive City’s dynamic performance should somehow be replicated." \
      "The emphasis in research was therefore modified from drive format to dynamic performance - that which was typically achieved with a vehicle having a lower center of gravity, meaning a sportscar." \
      "\It’s the dream of every development engineer to create a sportscar,\" said Shigeru Uehara, who was engaged in the development project as LPL. " \
      "\"The people who proposed changing the research direction at the evaluation meetings must also have had that dream." \
      "\"In 1983, another step was taken, in the form of a prototype car fashioned from a CR-X as a means of testing dynamic performance from various perspectives. " \
      "This was also the year Honda made its much-heralded return to the F-1 Series. " \
      "Thus, of course, spirits were high at the R&D Center, in anticipation of the possibility that Honda might indeed build sportscars. " \
      "Coincidentally, this had often been a subject of discussion at board meetings.\"I think the company wanted a car that could bridge its mass production FF models and F-1 cars,\" Uehara recalled. " \
      "\"They needed a car that would become the new face of Honda. Plus, we’d been contacted several times by those who were planning the Acura Division at American Honda concerning similar requests." \
      "\"Honda’s development engineers finally found an outlet for the passions when in the fall of 1985 the creation of a new sportscar began in earnest."

strT = str1 + str2
# Task1
# word = "Honda"
# ind = 0
# while True:
#       ind = strT.find(word, ind+len(word))
#       if ind == -1:
#             break
#       print("ind = ", ind)

# Task2
# strT = strT.lower()
# word = "honda"
# ind = 0
# while True:
#       ind = strT.find(word, ind+len(word))
#       if ind == -1:
#             break
#       print("ind = ", ind)

# Task3
# strT2 = "Hello"
# strT2 = list(strT2)
# print(strT2)
# strT2 = list(reversed(strT2))
# print(strT2)

# strT = "During the test drive. During the test drive."
# arr_strT = strT.split('.')
# arr_temp = []
#
# for strL in arr_strT:
#       strL = strL.split(' ')
#       strL = list(reversed(strL))
#       strL = ' '.join(strL)
#       # print(strL)
#       arr_temp.append(strL)
#
# strT = '.'.join(arr_temp)
# print(strT)

# Task 4

arr_symbol = []
ind, num = 0, 0
for i in strT:
      if not i.isalnum():
            arr_symbol.append(i)

arr_symbol = ''.join(arr_symbol)

while ind < len(arr_symbol):
      if arr_symbol.count(arr_symbol[ind]) > 1:
            arr_symbol = arr_symbol.replace(arr_symbol[ind], '', 1)
            continue
      ind += 1
arr_symbol = list(arr_symbol)
print("Txt. punctuation: ", arr_symbol)
xTab = '\t'
for i in arr_symbol:
      num = strT.count(i)
      if num > 0:
            print("\'{}\' = {}{}p.c.".format(i, num, xTab if num > 9 else xTab+xTab))
