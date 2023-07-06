import os
import time

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

#======================================================================================================================#

def clean_s() -> None:
    time.sleep(0)
    os.system('CLS')

def exit_menu():
    while True:
        out_submenu = input("\texit -> ")
        if not out_submenu:
            os.system('CLS')
            return True
        break
    return out_submenu

def print_menu(ind_pos, arr, name_f="", ind_menu: int=""):
    print("\nMenu:") if name_f == '' else None
    for i in range(len(arr)):
        if i == ind_pos:
            print("-> {}{} {}".format((str(ind_menu + 1) + '.') if name_f == "report" else '', str(i+1) + '.', arr[i][0]))
            continue
        print("   {}{} {}".format((str(ind_menu + 1) + '.') if name_f == "report" else '', str(i+1) + '.', arr[i][0]))

def receive_pos(ind_pos=0):
    min_ind, max_ind = 0, 4

    while True:
        direct = input(" ")

        # increment & decrement
        if not direct:
            return ind_pos, direct
        elif direct == 'W' or direct == 'w':
            ind_pos += 1
        elif direct == 'S' or direct == 's':
            ind_pos -= 1
        else:
            print("ERROR!")
            print(" \"w\" - Down, \"s\" - Up: ->", end='')
            continue

        # check position
        if ind_pos < min_ind:
            ind_pos = max_ind
        elif ind_pos > max_ind:
            ind_pos = min_ind

        return ind_pos, direct

#======================MENU FUNCTION=============================#

def find_wordUp(ind, menu, txt_in):
    title = ("\n {}. {}:".format(ind + 1, menu[ind][0]))

    while True:
        print(title)
        word = input("\tsearch Up word -> ")
        word = word.capitalize()
        ind, pos = 0, 0

        while True:
            ind = txt_in.find(word, ind+len(word))
            if ind == -1:
                break
            pos += 1
            print("\t{} ind = {}".format(pos, ind))

        if not txt_in.count(word):
            print(" \"{}\" is absent".format(word))

        temp = exit_menu()
        if type(temp) == bool and temp:
            break
        clean_s()

def find_word(ind, menu, txt_in):
    title = ("\n {}. {}:".format(ind + 1, menu[ind][0]))

    while True:
        print(title)
        word = input(" search word -> ")

        word = word.lower()
        txt_in = txt_in.lower()
        ind, pos = 0, 0

        while True:
            ind = txt_in.find(word, ind + len(word))
            if ind == -1:
                break
            pos += 1
            print("\t{} ind = {}".format(pos, ind))

        if not txt_in.count(word):
            print(" \"{}\" is absent".format(word))

        temp = exit_menu()
        if type(temp) == bool and temp:
            break
        clean_s()

def reverse_word(ind, menu, txt_in):
      print("\n {}. {}:".format(ind + 1, menu[ind][0]))

      arr_strT = txt_in.split('.')
      arr_temp = []

      for strL in arr_strT:
            strL = strL.split(' ')
            strL = list(reversed(strL))
            strL = ' '.join(strL)
            arr_temp.append(strL)

      txt_in = '.'.join(arr_temp)
      print(txt_in)

      while True:
          temp = exit_menu()
          if type(temp) == bool and temp:
              break
          print("\tERROR")
      clean_s()

def num_symbol(ind, menu, txt_in):
    print("\n {}. {}:".format(ind + 1, menu[ind][0]))

    arr_symbol = []
    ind, num = 0, 0
    for i in txt_in:
        if not i.isalnum():
            arr_symbol.append(i)

    arr_symbol = ''.join(arr_symbol)

    while ind < len(arr_symbol):
        if arr_symbol.count(arr_symbol[ind]) > 1:
            arr_symbol = arr_symbol.replace(arr_symbol[ind], '', 1)
            continue
        ind += 1

    arr_symbol = list(arr_symbol)
    print(" Txt. punctuation: ", arr_symbol)
    xTab = '\t'
    for i in arr_symbol:
        num = txt_in.count(i)
        if num > 0:
            print("\t\'{}\' = {}{}p.c.".format(i, num, xTab if num > 9 else xTab + xTab))

    while True:
        temp = exit_menu()
        if type(temp) == bool and temp:
            break
        print("\tERROR")
    clean_s()

def exit_txt(ind, menu, txt_in=None):
    print("\n {}. {}:".format(ind + 1, menu[ind][0]))
    return True

#=============================MAIN=============================#

ind_menu = 0
strTxt = strT

menu_f = {
    0: ["Find word Up", find_wordUp],
    1: ["Find word", find_word],
    2: ["Reverse word", reverse_word],
    3: ["Punctuation", num_symbol],
    4: ["Exit", exit_txt]
}

while True:
    print_menu(ind_menu, menu_f)
    print(" \"w\" - Down, \"s\" - Up: ->", end='')
    ind_menu, operation = receive_pos(ind_menu)
    clean_s()

    if not operation:
        tempValue = menu_f[ind_menu][1](ind_menu, menu_f, strTxt)
        if type(tempValue) == bool and tempValue:
            break
