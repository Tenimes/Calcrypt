from calendar import *
from random import *

months = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'r', 's', 't', 'u', 'v', 'y', 'z', 'q', 'x', 'w', ' ']
encrypted_alphabet = ([[0, 1, 1, 0], [1, 0, 0, 1], [1, 1, 1, 1], [1, 0, 0, 1]],
                      [[1, 0, 0], [1, 1, 0], [1, 0, 1], [1, 1, 0]],
                      [[0, 1, 1], [1, 0, 0], [1, 0, 0], [0, 1, 1]],
                      [[1, 1, 0], [1, 0, 1], [1, 0, 1], [1, 1, 0]],
                      [[0, 1, 1, 0], [1, 1, 1, 1], [1, 0, 0, 0], [0, 1, 1, 1]],
                      [[1, 1, 1], [1, 0, 0], [1, 1, 0], [1, 0, 0]],
                      [[1, 1, 1], [1, 1, 0], [1, 0, 1], [1, 1, 1]],
                      [[1, 0, 1], [1, 1, 1], [1, 0, 1]],
                      [[1], [1], [1], [1]],
                      [[1], [1], [1]],
                      [[0, 1], [0, 1], [1, 1]],
                      [[1, 0, 1], [1, 1, 0], [1, 1, 0], [1, 0, 1]],
                      [[1, 0], [1, 0], [1, 1]],
                      [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1]],
                      [[1, 0, 0, 1], [1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 1]],
                      [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
                      [[1, 1, 0], [1, 0, 1], [1, 1, 0], [1, 0, 0]],
                      [[1, 1, 0], [1, 0, 1], [1, 1, 0], [1, 0, 1]],
                      [[0, 1, 0], [1, 0, 1], [0, 0, 1], [0, 1, 0]],
                      [[1, 1, 1], [0, 1, 0], [0, 1, 0]],
                      [[1, 0, 1], [1, 0, 1], [1, 1, 1]],
                      [[1, 0, 1], [1, 0, 1], [0, 1, 0]],
                      [[1, 0, 1], [0, 1, 0], [0, 1, 0]],
                      [[1, 1, 1], [0, 0, 1], [0, 1, 0], [1, 1, 1]],
                      [[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1]],
                      [[1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]],
                      [[1, 0, 1], [0, 1, 0], [1, 0, 1]],
                      [[0, 1, 0], [1, 0, 1], [0, 1, 0]])


class calcrypt:
    def __init__(self):
        self.txt_created = False
        self.key_generated = False

    def createTxt(self, path='none', sameLine=False, lineBreak=238):
        self.path = path
        self.txt_created = True
        self.sameLine = sameLine
        self.lineBreak = lineBreak
        if self.lineBreak < 1:
            raise ValueError("LineBreak argument must be higher than 0!")
        if(self.path != 'none'):
            self.txtfile = open(self.path, 'w')
        else:
            self.txtfile = open("encrypted.txt", 'w')

    def encrypt(self, text, txt=False, returnList=False):
        self.txt = txt
        self.list = returnList
        self.text = text
        self.text = self.text.strip()
        self.text = self.text.lower()
        self.letters = list(self.text)
        self.encrypted_text = []
        if self.txt:
            if self.txt_created == False:
                raise RuntimeError(
                    "The 'txt' argument is given 'true' in the encrypt function, but no txt file has been opened. Use the 'createTxt' function to fix the error.")
        self.numbers = [4, 5, 6, 7, 8, 9]
        self.key = ''
        for num in range(4):
            self.num = choice(self.numbers)
            self.numbers.remove(self.num)
            self.key += str(self.num)
        self.key_generated = True
        for letter in self.letters:
            self.year = randrange(1000, 3000)
            self.month = choice(months)
            self.calendar = monthcalendar(self.year, self.month)
            self.encrypted_letter = []
            for i in range(len(self.calendar)):
                self.calendar[i] = [
                    value for value in self.calendar[i] if value != 0]
            if letter in alphabet:
                self.index = alphabet.index(letter)
            else:
                raise NameError(
                    "Undefined character! Please do not use special characters.")
            self.column = len(encrypted_alphabet[self.index][0])
            self.row = len(encrypted_alphabet[self.index])
            self.encrypted_letter_str = ""
            self.random_row = randrange(len(self.calendar)+1-self.row)
            self.loop = True
            while(self.loop):
                if(len(self.calendar[0]) >= self.column and self.random_row == 0):
                    if len(self.calendar[0]) > self.column:
                        self.random_column = randrange(
                            0, len(self.calendar[0])-self.column+1)
                    else:
                        self.random_column = 0
                    for r in range(self.row):
                        for c in range(self.column):
                            if encrypted_alphabet[self.index][r][c] == 1:
                                if r > 0:
                                    self.encrypted_letter.append(
                                        self.calendar[r][c+self.random_column+(7-len(self.calendar[0]))])
                                else:
                                    self.encrypted_letter.append(
                                        self.calendar[r][c+self.random_column])
                                self.loop = False
                elif(self.random_row == 1 and self.row == 3) or (((self.random_row == 2 and self.row == 3) or (self.random_row == 1 and self.row == 4)) and len(self.calendar) == 6):
                    self.random_column = randrange(7-self.column)
                    for r in range(self.row):
                        for c in range(self.column):
                            if encrypted_alphabet[self.index][r][c] == 1:
                                self.encrypted_letter.append(
                                    self.calendar[r+1][c+self.random_column])
                                self.loop = False
                elif(self.random_row != 0 and len(self.calendar[-1]) >= self.column):
                    if(len(self.calendar[-1]) > self.column):
                        self.random_column = randrange(
                            len(self.calendar[-1])-self.column)
                    else:
                        self.random_column = 0
                    for r in range(self.row):
                        for c in range(self.column):
                            if encrypted_alphabet[self.index][r][c] == 1:
                                self.encrypted_letter.append(
                                    self.calendar[r+self.random_row][c+self.random_column])
                                self.loop = False
                else:
                    self.random_row = randrange(
                        len(self.calendar)+1-self.row)
            if (self.month // 10) == 0:
                self.encrypted_letter_str = '0' + str(self.month)
            else:
                self.encrypted_letter_str = str(self.month)
            shuffle(self.encrypted_letter)
            for l in range(len(self.encrypted_letter)):
                if(self.encrypted_letter[l] // 10) == 0:
                    self.encrypted_letter_str += '0' + \
                        str(self.encrypted_letter[l])
                else:
                    self.encrypted_letter_str += str(
                        self.encrypted_letter[l])
            self.encrypted_letter_str += str(self.year) + str(self.key)
            self.encrypted_text.append(self.encrypted_letter_str)
        self.encrypted_text_str = ""
        self.encrypted_text[-1] = self.encrypted_text[-1][0:-4]
        for eWord in self.encrypted_text:
            for eLetter in eWord:
                self.encrypted_text_str += eLetter
        if(self.list):
            if self.txt:
                raise RuntimeError("Output cannot be both list and on txt!")
            else:
                return self.encrypted_text
        else:
            if self.txt:
                if self.sameLine == False:
                    self.mLine = 0
                    for m in self.encrypted_text_str:
                        self.txtfile.write(m)
                        self.mLine += 1
                        if self.mLine >= self.lineBreak:
                            self.txtfile.write('\n')
                            self.mLine = 0
                    self.txtfile.close()
                    return self.encrypted_text_str
                else:
                    self.txtfile.write(self.encrypted_text_str)
                    self.txtfile.close()
                    return self.encrypted_text_str
            else:
                return self.encrypted_text_str

    def getKey(self):
        if self.key_generated:
            return self.key
        else:
            raise RuntimeError(
                "No key has been created! Are sure about did you use encrypt function?")

    def decryptString(self, text, key):
        self.crypting_key = key
        self.clean_txt = str(text).strip()
        self.clean_txt = str(self.clean_txt).split(str(self.crypting_key))
        self.decrypted_text = []
        for word in self.clean_txt:
            self.dList = [word[i:i+2] for i in range(0, len(word), 2)]
            self.dMonth = int(self.dList[0])
            self.dYear = int(self.dList[-2]+self.dList[-1])
            self.dList = self.dList[1:-2]
            self.dList.sort()
            self.dList = [int(x) for x in self.dList]
            self.dCalendar = monthcalendar(self.dYear, self.dMonth)
            self.min_index = 7
            self.max_index = 0
            for number in self.dList:
                for week in self.dCalendar:
                    for day in week:
                        if number == day:
                            if week.index(number) < self.min_index:
                                self.min_index = week.index(number)
                            if week.index(number) > self.max_index:
                                self.max_index = week.index(number)
            self.decrypted_letter_list = []
            self.decrypted_list = []
            for week in self.dCalendar:
                if[c for c in week if c in self.dList]:
                    for day in week:
                        if day in self.dList:
                            self.decrypted_list.append(1)
                        else:
                            if self.max_index >= week.index(day) >= self.min_index:
                                self.decrypted_list.append(0)
                            elif week.index(day) >= self.max_index:
                                if not self.decrypted_list == []:
                                    self.decrypted_letter_list.append(
                                        self.decrypted_list)
                                self.decrypted_list = []
                if not self.decrypted_list == []:
                    self.decrypted_letter_list.append(self.decrypted_list)
                    self.decrypted_list = []
            if self.decrypted_letter_list in encrypted_alphabet:
                self.dIndex = encrypted_alphabet.index(
                    self.decrypted_letter_list)
            else:
                raise RuntimeError(
                    "An error occurs while decrypting the code. Check your alphabet and encrypted alphabet or key.")
            self.decrypted_text.append(alphabet[self.dIndex])
        self.decrypted_text_str = ''.join(map(str, self.decrypted_text))
        return self.decrypted_text_str

    def decryptTxt(self, path, key):
        self.path = path
        self.txtText = ''
        try:
            with open(self.path, 'r+') as file:
                self.txtFile = file.read().splitlines()
                for line in self.txtFile:
                    self.txtText += line
                file.close()
        except:
            raise ValueError(
                "Unvalid path! Can not open txt file at ", self.path)
        self.crypting_key = key
        self.clean_txt = self.txtText.strip()
        self.clean_txt = str(self.clean_txt).split(str(self.crypting_key))
        self.decrypted_text = []
        print(self.clean_txt)
        for word in self.clean_txt:
            self.dList = [word[i:i+2] for i in range(0, len(word), 2)]
            self.dMonth = int(self.dList[0])
            self.dYear = int(self.dList[-2]+self.dList[-1])
            self.dList = self.dList[1:-2]
            self.dList.sort()
            self.dList = [int(x) for x in self.dList]
            self.dCalendar = monthcalendar(self.dYear, self.dMonth)
            self.min_index = 7
            self.max_index = 0
            for number in self.dList:
                for week in self.dCalendar:
                    for day in week:
                        if number == day:
                            if week.index(number) < self.min_index:
                                self.min_index = week.index(number)
                            if week.index(number) > self.max_index:
                                self.max_index = week.index(number)
            self.decrypted_letter_list = []
            self.decrypted_list = []
            for week in self.dCalendar:
                if[c for c in week if c in self.dList]:
                    for day in week:
                        if day in self.dList:
                            self.decrypted_list.append(1)
                        else:
                            if self.max_index >= week.index(day) >= self.min_index:
                                self.decrypted_list.append(0)
                            elif week.index(day) >= self.max_index:
                                if not self.decrypted_list == []:
                                    self.decrypted_letter_list.append(
                                        self.decrypted_list)
                                self.decrypted_list = []
                if not self.decrypted_list == []:
                    self.decrypted_letter_list.append(self.decrypted_list)
                    self.decrypted_list = []
            if self.decrypted_letter_list in encrypted_alphabet:
                self.dIndex = encrypted_alphabet.index(
                    self.decrypted_letter_list)
            else:
                raise RuntimeError(
                    "An error occurs while decrypting the code. Check your alphabet and encrypted alphabet or key.")
            self.decrypted_text.append(alphabet[self.dIndex])
        self.decrypted_text_str = ''.join(map(str, self.decrypted_text))
        return self.decrypted_text_str


class calcryptWinfo:
    def __init__(self):
        self.txt_created = False
        self.key_generated = False

    def createTxt(self, path='none', sameLine=False, lineBreak=238):
        self.path = path
        self.txt_created = True
        self.sameLine = sameLine
        self.lineBreak = lineBreak
        if self.lineBreak < 1:
            raise ValueError("LineBreak argument must be higher than 0!")
        if(self.path != 'none'):
            self.txtfile = open(self.path, 'w')
        else:
            self.txtfile = open("encrypted.txt", 'w')

    def encrypt(self, text, txt=False, returnList=False):
        self.txt = txt
        self.list = returnList
        self.text = text
        self.text = self.text.strip()
        self.text = self.text.lower()
        self.letters = list(self.text)
        self.encrypted_text = []
        if self.txt:
            if self.txt_created == False:
                raise RuntimeError(
                    "The 'txt' argument is given 'true' in the encrypt function, but no txt file has been opened. Use the 'createTxt' function to fix the error.")
        self.numbers = [4, 5, 6, 7, 8, 9]
        self.key = ''
        for num in range(4):
            self.num = choice(self.numbers)
            self.numbers.remove(self.num)
            self.key += str(self.num)
        self.key_generated = True
        for letter in self.letters:
            self.year = randrange(1000, 3000)
            self.month = choice(months)
            self.calendar = monthcalendar(self.year, self.month)
            self.encrypted_letter = []
            for i in range(len(self.calendar)):
                self.calendar[i] = [
                    value for value in self.calendar[i] if value != 0]
            if letter in alphabet:
                self.index = alphabet.index(letter)
            else:
                raise NameError(
                    "Undefined character! Please do not use special characters.")
            self.column = len(encrypted_alphabet[self.index][0])
            self.row = len(encrypted_alphabet[self.index])
            self.encrypted_letter_str = ""
            self.random_row = randrange(len(self.calendar)+1-self.row)
            print(self.calendar)
            print(self.random_row)
            self.loop = True
            while(self.loop):
                if(len(self.calendar[0]) >= self.column and self.random_row == 0):
                    if len(self.calendar[0]) > self.column:
                        self.random_column = randrange(
                            0, len(self.calendar[0])-self.column+1)
                        print(self.random_column)
                    else:
                        self.random_column = 0
                    for r in range(self.row):
                        for c in range(self.column):
                            if encrypted_alphabet[self.index][r][c] == 1:
                                if r > 0:
                                    self.encrypted_letter.append(
                                        self.calendar[r][c+self.random_column+(7-len(self.calendar[0]))])
                                else:
                                    self.encrypted_letter.append(
                                        self.calendar[r][c+self.random_column])
                                print(
                                    "letter: " + letter + ", encrypted letter: ", end='')
                                print(self.encrypted_letter)
                                self.loop = False
                elif(self.random_row == 1 and self.row == 3) or (((self.random_row == 2 and self.row == 3) or (self.random_row == 1 and self.row == 4)) and len(self.calendar) == 6):
                    self.random_column = randrange(7-self.column)
                    for r in range(self.row):
                        for c in range(self.column):
                            if encrypted_alphabet[self.index][r][c] == 1:
                                self.encrypted_letter.append(
                                    self.calendar[r+1][c+self.random_column])
                                print(
                                    "letter: " + letter + ", encrypted letter: ", end='')
                                print(self.encrypted_letter)
                                self.loop = False
                elif(self.random_row != 0 and len(self.calendar[-1]) >= self.column):
                    if(len(self.calendar[-1]) > self.column):
                        self.random_column = randrange(
                            len(self.calendar[-1])-self.column)
                    else:
                        self.random_column = 0
                    for r in range(self.row):
                        for c in range(self.column):
                            if encrypted_alphabet[self.index][r][c] == 1:
                                self.encrypted_letter.append(
                                    self.calendar[r+self.random_row][c+self.random_column])
                                print(
                                    "letter: " + letter + ", encrypted letter: ", end='')
                                print(self.encrypted_letter)
                                self.loop = False
                else:
                    self.random_row = randrange(
                        len(self.calendar)+1-self.row)
            if (self.month // 10) == 0:
                self.encrypted_letter_str = '0' + str(self.month)
            else:
                self.encrypted_letter_str = str(self.month)
            shuffle(self.encrypted_letter)
            for l in range(len(self.encrypted_letter)):
                if(self.encrypted_letter[l] // 10) == 0:
                    self.encrypted_letter_str += '0' + \
                        str(self.encrypted_letter[l])
                else:
                    self.encrypted_letter_str += str(
                        self.encrypted_letter[l])
            self.encrypted_letter_str += str(self.year) + str(self.key)
            print("encrypted str: " + self.encrypted_letter_str)
            self.encrypted_text.append(self.encrypted_letter_str)
        self.encrypted_text_str = ""
        self.encrypted_text[-1] = self.encrypted_text[-1][0:-4]
        for eWord in self.encrypted_text:
            for eLetter in eWord:
                self.encrypted_text_str += eLetter
        if(self.list):
            if self.txt:
                raise RuntimeError("Output cannot be both list and on txt!")
            else:
                return self.encrypted_text
        else:
            if self.txt:
                if self.sameLine == False:
                    self.mLine = 0
                    for m in self.encrypted_text_str:
                        self.txtfile.write(m)
                        self.mLine += 1
                        if self.mLine >= self.lineBreak:
                            self.txtfile.write('\n')
                            self.mLine = 0
                    self.txtfile.close()
                    return self.encrypted_text_str
                else:
                    self.txtfile.write(self.encrypted_text_str)
                    self.txtfile.close()
                    return self.encrypted_text_str
            else:
                return self.encrypted_text_str

    def getKey(self):
        if self.key_generated:
            return self.key
        else:
            raise RuntimeError(
                "No key has been created! Are sure about did you use encrypt function?")

    def decryptString(self, text, key):
        self.crypting_key = key
        self.clean_txt = str(text).strip()
        self.clean_txt = str(self.clean_txt).split(str(self.crypting_key))
        self.decrypted_text = []
        print(self.clean_txt)
        for word in self.clean_txt:
            self.dList = [word[i:i+2] for i in range(0, len(word), 2)]
            self.dMonth = int(self.dList[0])
            self.dYear = int(self.dList[-2]+self.dList[-1])
            print(self.dList)
            self.dList = self.dList[1:-2]
            self.dList.sort()
            self.dList = [int(x) for x in self.dList]
            self.dCalendar = monthcalendar(self.dYear, self.dMonth)
            print(self.dCalendar)
            print(self.dList)
            self.min_index = 7
            self.max_index = 0
            for number in self.dList:
                for week in self.dCalendar:
                    for day in week:
                        if number == day:
                            if week.index(number) < self.min_index:
                                self.min_index = week.index(number)
                            if week.index(number) > self.max_index:
                                self.max_index = week.index(number)
            self.decrypted_letter_list = []
            self.decrypted_list = []
            print(self.min_index, self.max_index)
            for week in self.dCalendar:
                if[c for c in week if c in self.dList]:
                    for day in week:
                        if day in self.dList:
                            self.decrypted_list.append(1)
                        else:
                            if self.max_index >= week.index(day) >= self.min_index:
                                self.decrypted_list.append(0)
                            elif week.index(day) >= self.max_index:
                                if not self.decrypted_list == []:
                                    self.decrypted_letter_list.append(
                                        self.decrypted_list)
                                self.decrypted_list = []
                if not self.decrypted_list == []:
                    self.decrypted_letter_list.append(self.decrypted_list)
                    self.decrypted_list = []
            print("decrypted list:", end='')
            print(self.decrypted_list)
            print("decrypted letter list:", end='')
            print(self.decrypted_letter_list)
            if self.decrypted_letter_list in encrypted_alphabet:
                self.dIndex = encrypted_alphabet.index(
                    self.decrypted_letter_list)
            else:
                raise RuntimeError(
                    "An error occurs while decrypting the code. Check your alphabet and encrypted alphabet or key.")
            print(alphabet[self.dIndex])
            self.decrypted_text.append(alphabet[self.dIndex])
        print(self.decrypted_text)
        self.decrypted_text_str = ''.join(map(str, self.decrypted_text))
        print(self.decrypted_text_str)
        return self.decrypted_text_str

    def decryptTxt(self, path, key):
        self.path = path
        self.txtText = ''
        try:
            with open(self.path, 'r+') as file:
                self.txtFile = file.read().splitlines()
                for line in self.txtFile:
                    self.txtText += line
                file.close()
                print("Txt file opened in 'Read' mode.")
        except:
            raise ValueError(
                "Unvalid path! Can not open txt file at ", self.path)
        self.crypting_key = key
        self.clean_txt = self.txtText.strip()
        self.clean_txt = str(self.clean_txt).split(str(self.crypting_key))
        self.decrypted_text = []
        print(self.clean_txt)
        for word in self.clean_txt:
            self.dList = [word[i:i+2] for i in range(0, len(word), 2)]
            self.dMonth = int(self.dList[0])
            self.dYear = int(self.dList[-2]+self.dList[-1])
            print(self.dList)
            self.dList = self.dList[1:-2]
            self.dList.sort()
            self.dList = [int(x) for x in self.dList]
            self.dCalendar = monthcalendar(self.dYear, self.dMonth)
            print(self.dCalendar)
            print(self.dList)
            self.min_index = 7
            self.max_index = 0
            for number in self.dList:
                for week in self.dCalendar:
                    for day in week:
                        if number == day:
                            if week.index(number) < self.min_index:
                                self.min_index = week.index(number)
                            if week.index(number) > self.max_index:
                                self.max_index = week.index(number)
            self.decrypted_letter_list = []
            self.decrypted_list = []
            print(self.min_index, self.max_index)
            for week in self.dCalendar:
                if[c for c in week if c in self.dList]:
                    for day in week:
                        if day in self.dList:
                            self.decrypted_list.append(1)
                        else:
                            if self.max_index >= week.index(day) >= self.min_index:
                                self.decrypted_list.append(0)
                            elif week.index(day) >= self.max_index:
                                if not self.decrypted_list == []:
                                    self.decrypted_letter_list.append(
                                        self.decrypted_list)
                                self.decrypted_list = []
                if not self.decrypted_list == []:
                    self.decrypted_letter_list.append(self.decrypted_list)
                    self.decrypted_list = []
            print("decrypted list:", end='')
            print(self.decrypted_list)
            print("decrypted letter list:", end='')
            print(self.decrypted_letter_list)
            if self.decrypted_letter_list in encrypted_alphabet:
                self.dIndex = encrypted_alphabet.index(
                    self.decrypted_letter_list)
            else:
                raise RuntimeError(
                    "An error occurs while decrypting the code. Check your alphabet and encrypted alphabet or key.")
            print(alphabet[self.dIndex])
            self.decrypted_text.append(alphabet[self.dIndex])
        print(self.decrypted_text)
        self.decrypted_text_str = ''.join(map(str, self.decrypted_text))
        print(self.decrypted_text_str)
        return self.decrypted_text_str
