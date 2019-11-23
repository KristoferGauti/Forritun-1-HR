'''

   _ _ _ _ _  _ _      _ _      _ _ _ _ _ _        _ _ _       _ _ _ __ _ _ _         _ _ _ _                                                                        
 ////- - - -  ||||     ||||     ||||- - - -       - - - -      - - - -- - - -       - - - - \\\\        
////          ||||     ||||     ||||            ////   \\\\         ||||          ////                                               
||||          ||||_ _ _||||     ||||_ _ _ _    ////_ _ _\\\\        ||||          \\\\_ _ _ _                                                           
||||          ||||- - -||||     ||||- - - -    ||||- - -||||        ||||             - - - -\\\\                                                       
\\\\          ||||     ||||     ||||           ||||     ||||        ||||                    ////                                     
 \\\\_ _ _ _  ||||     ||||     ||||_ _ _ _    ||||     ||||        ||||          \\\\_ _ _////                                                    
   - - - - -  ||||     ||||     - - - - - -    ||||     ||||        ||||            - - - - -                                                      

Efnisyfirlit:
  1. Dictionaries
  2. Klassar
  3. Good functions
  4. Str format

─████████───
─██░░░░██───
─████░░██───
───██░░██───
───██░░██───
───██░░██───
───██░░██───
───██░░██───
─████░░████─
─██░░░░░░██─
─██████████─

Dictionaries
{

    líta svona út:

    d = {
        <key>: <value>,
        <key>: <value>,
        .
        .
        .
        <key>: <value>
    }

    # Taka fyrir hvert einasta key er value.

    # Value getur verið list, tuple, int, str.

    # Key getur ekki verið list


    # Random stöff sem hægt er að gera:
    nem = {
        "bla": "ymir",
        "2": "jason",
        3: "gardar",
        False: "kristo"
    }

    print(nem["bla"])
    >>> ymir

    print(nem[3])
    >>> gardar

    nem[69]="bjartur"
    print(nem)
    >>> {"bla": "ymir", "2": "jason", 3: "gardar", False: "kristo", 69: "bjartur"}

    print(69 in nem)
    >>> True

    print(nem.get(False))
    >>> kristo

    print(nem.get(420))
    >>> None

    # Useful að geta breytt í lista:

    list(nem.items())
    >>> [("bla": "ymir"), ("2": "jason"), (3: "gardar"), (False: "kristo"), (69: "bjartur")]

    nem.values() >>> gefur values
    nem.keys()   >>> gefur keys

    nem.pop(key) >>> fjarlægir úr dictionary

    removed = nem.pop(69) # Tekur í burtu item sem hefur key 69
    print(removed) # Er samt ennþá hægt að geyma það sem tekið var úr
    >>> bjartur

    print(nem)
    >>> {"bla": "ymir", "2": "jason", 3: "gardar", False: "kristo"}

    nem.popitem() # Tekur síðasta úr dictionary
    print(nem)
    >>> {"bla": "ymir", "2": "jason", 3: "gardar"}

    # Hægt er að update'a dictionary með öðru dictionary eða með lista af tuplum t.d.:
    d1 = {'a': 10, 'b': 20, 'c': 30}
    d2 = {'b': 200, 'd': 400}
    d1.update(d2)

    print(d1)
    >>> {'a': 10, 'b': 200, 'c': 30, 'd': 400}
}
─██████████████─
─██░░░░░░░░░░██─
─██████████░░██─
─────────██░░██─
─██████████░░██─
─██░░░░░░░░░░██─
─██░░██████████─
─██░░██─────────
─██░░██████████─
─██░░░░░░░░░░██─
─██████████████─

Klassar
{
    # 1. Byrjunargildi
    # Alltaf að byrja á að skoða öll skipti sem kallað er á klassan
    # Hvað er sett inn í hann sem byrjunargildi?
    
    # 2. Hvaða breytur?
    # Næst skal gera __init__ fall sem tekur inn þau gildi sem skref 1 biður um.
    # Á að nota local breytur? self.__local eða global? self.global
    # ALLTAF! nota klassabreytur ef það er hægt. T.d. MIN = 0
    # Ef MIN = 0 er notað er hægt að kalla á þá breytu með self.MIN
    
    # 3. Prent fall
    # Það á pottþétt alltaf að gera __str__ fall svo það er næst.
    # Hér er gott að laga allar breytur áður en þær verða prentaðar fyrir test cases
    # Kannski þarf að vinna með lista, þá þarf að breyta honum í str. t.d. ''.join(listi)

    # 4. Eitt skref í einu
    # Ekki gera allann Klassan í einu. Byrjum á að renna yfir hvað á að framkvæma. 
    # þeir biðja líklegast fyrst á að gera prent, virkar það? já gegjað hvað er næst?
    # næst er að gera move() fall þá græjar maður það, fær það rétt og heldur áfram í næsta fall

    # CLASS OPERATORS
        +	__add__(self, other)
        –	__sub__(self, other)
        *	__mul__(self, other)
        /	__truediv__(self, other)
        //	__floordiv__(self, other)
        %	__mod__(self, other)
        **	__pow__(self, other)

        <	__lt__(self, other)
        >	__gt__(self, other)
        <=	__le__(self, other)
        >=	__ge__(self, other)
        ==	__eq__(self, other)
        !=	__ne__(self, other)

    # Hér sést dæmi um klassa

    class Bug:
        MAP_SIZE = 20
        MIN = 1
        MAX = MAP_SIZE
        BUG = "b"
        EMPTY = "x"

        def __init__(self, position = 1):
            self.__position = position
            self.__rotation = 1
        
        def __str__(self):
            self.__position = MAX if self.__position > MAX else MIN if self.__position < MIN else self.__position

            # Þessi kóði að neðan er að gera það sama og kóðinn hér að ofan

            if self.__position > MAX:
                self.__position = MAX
            if self.__position < MIN:
                self.__position = MIN

            return "".join([BUG if self.__position == x + 1 else EMPTY for x in range(self.MAP_SIZE)])
            

            # Þessi kóði að neðan er að gera það sama og list comprehensionið hér að ofan
            mapList = []
            for x in range(self):
                if self.__position == x + 1:
                    aList.append(BUG)
                else:
                    aList.append(EMPTY)
            mapStr = "".join(mapList)
            
            return mapStr

        def move(self):
            # Rotation er annað hvort mínus 1 eða plúss einn, með því að bæta því 
            # við self.__position fer hann annað hvort til hægri(+1) eða til vinsti(-1)
            self.__position += self.__rotation 

        def turn(self):
            self.__rotation *= -1

        def __gt__(self, other):
            return self.__position > other.__position

        def __add__(self, other):
            return Bug(self.__position + other.__position)
}
─██████████████─
─██░░░░░░░░░░██─
─██████████░░██─
─────────██░░██─
─██████████░░██─
─██░░░░░░░░░░██─
─██████████░░██─
─────────██░░██─
─██████████░░██─
─██░░░░░░░░░░██─
─██████████████─
'''
#class RandomStuffsFyrirLokaprof():
def alphabet():
    """Returns the alphabetical uppercase letters"""
    ascii_upper_letters = []
    for i in range(65,91): #for x in range(97,123) for the lowercase letters
        ascii_upper_letters.append(chr(i))

    return ascii_upper_letters

def convert_2D_list_to_1D_list(aTwoDimentionalList):
    aOneDimentionalList = [x for sublist in aTwoDimentionalList for x in sublist]
    return aOneDimentionalList

def check_if_a_list_is_full(a_list):
    """Check if full"""
    return len(set(a_list)) == 1

def open_file(filename):
    """Opens a file and returns it
    File not found returns False"""
    try:
        file_obj = open(filename, "r", encoding="utf-8")
        return file_obj
    except FileNotFoundError:
        print("File {} not found!".format(filename))
        return False

def get_max(the_dict):
    """The dictionary should be like 
    {key : [item1, item2], key2 : [item3, item4, item5]}
    It returns the max key and max length of a list"""

    max_val, max_name = 0, ""

    for name, country_list in the_dict.items():
        curr_val = len(country_list)
        if curr_val > max_val:
            max_val, max_name = curr_val, name

        return max_val, max_name

def print_lines(file_obj):
    """Returns a dictionary 
    {name : [country1, country2, country3], 
    name2 : [country1, country2, country3]}"""

    flight_dictionary = {}
    for line in file_obj:
        name, country = line.split()
        if name in flight_dictionary:
            flight_dictionary[name] += [country]
        else:
            flight_dictionary[name] = [country] 

    return flight_dictionary

def dict_to_list(aDict):
    return list(aDict.items())

def sort_list_by_second_value_in_list(aList):
    def sort_by_second(aList): return aList[1]
    return sorted(aList, key = sort_by_second, reverse=True)

def open_csv_file(fileName):
    # Þarf að gera "import csv" efst í skjali

    with open(fileName) as csvFile:
        return csv.reader(csvFile, delimiter = ',')

def print_map_with_a_position(target):
    LENGTH = 10
    EMPTY = 'x'
    POS = 'o'

    mapList = []
    for place in range(1, LENGTH + 1):
        if place == target:
            mapList.append(POS)
        else:
            mapList.append(EMPTY)
    mapStr = "".join(mapList)
    
    return mapStr

    return "".join([POS if place == target else EMPTY for place in range(1, LENGTH + 1)])

def switch_keys_and_values(dictList):
    """ Takes in list that has sublist, with two items inside:
    [["hommi", "19"],["faggi", "34"],["prump", "69"]]
    """
    switchedList = []
    for sublist in dictList:
        key = sublist[0]
        value = sublist[1]
        switchedList.append([value, key])
    return switchedList

def first_item_in_sublist_to_tuple(aList):
    newList = []
    for sublist in aList:
        key = sublist[0]
        value = sublist[1]
        if sublist == aList[0]:
            newList.append(tuple(key, value))
        else:
            newList.append(list(key, value))

    return newList

'''
─██████──██████─
─██░░██──██░░██─
─██░░██──██░░██─
─██░░██──██░░██─
─██░░██████░░██─
─██░░░░░░░░░░██─
─██████████░░██─
─────────██░░██─
─────────██░░██─
─────────██░░██─
─────────██████─
{
    Mismunandi bókstafi sem hægt er að skrifa í formatið {}
        s – strings
        d – decimal integers (base-10)
        f – floating point display
        c – character
        b – binary
        o – octal
        x – hexadecimal with lowercase letters after 9
        X – hexadecimal with uppercase letters after 9
        e – exponent notation
    
        <   :  left-align text in the field
        ^   :  center text in the field
        >   :  right-align text in the field

    {:.2f}.format(0.123) # Gefur 2 aukastafi >>> 0.12

    ADVANCED:
        format_spec ::=  [[fill]align][sign][#][0][width][,][.precision][type]
        fill        ::=  <any character>
        align       ::=  "<" | ">" | "=" | "^"
        sign        ::=  "+" | "-" | " "
        width       ::=  integer
        precision   ::=  integer
        type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
    
    '{:0>4.2f}'.format(0.123) # Gefur tvö núll og svo tvo aukastafi >>> 00.12
}
'''