import discord, time, socket, geocoder, random, datetime, hashlib
from discord.ext import commands
client = discord.Client()
response = False
a = ""
b = ""
#i didnt want to write the cuss words so i just did this lol
bad_word1_l1 = "u"
bad_word1_l2 = "k"
bad_word1_l3 = "c"
bad_word1_l4 = "f"
badword1 = bad_word1_l4 + bad_word1_l1 + bad_word1_l3 + bad_word1_l2
bad_word2_l1 = "t"
bad_word2_l2 = "h"
bad_word2_l3 = "s"
bad_word2_l4 = "i"
badword2 = bad_word2_l3 + bad_word2_l2 + bad_word2_l4 + bad_word2_l1
badword3_l1 = "s"
badword3_l2 = "p"
badword3_l3 = "s"
badword3_l4 = "y"
badword3_l5 = "u"
badword3 = badword3_l2 + badword3_l5 + badword3_l1 + bad_word1_l3 + badword3_l4
badword4_l1 = "u"
badword4_l2 = "c"
badword4_l3 = "t"
badword4_l4 = "n"
badword4 = badword4_l2 + badword4_l1 + badword4_l4 + badword4_l3
badword5_l1 = "g"
badword5_l2 = "n"
badword5_l3 = "a"
badword5_l4 = "g"
badword5_l5 = "i"
badword5 = badword5_l2 + badword5_l5 + badword5_l1 + badword5_l4 + badword5_l3
badword6_l1 = "i"
badword6_l2 = "b"
badword6_l3 = "c"
badword6_l4 = "t"
badword6_l5 = "h"
badword6 = badword6_l2 + badword6_l1 + badword6_l4 + badword6_l3 + badword6_l5
badwords = [badword1, badword2, badword3, badword4, badword5, badword6]
response2 = False
def binarytostr(binary):
    thing = binary.split()
    binarytostrdo(thing)
def strtobinary(phrase):
    while True:
        try:
            def translate(phrase):
                translation = ""
                for letter in phrase:
                    if letter in "a":
                        translation = translation + " 01100001"
                    if letter in "b":
                        translation = translation + " 01100010"
                    if letter in "c":
                        translation = translation + " 01100011"
                    if letter in "d":
                        translation = translation + " 01100100"
                    if letter in "e":
                        translation = translation + " 01100101"
                    if letter in "f":
                        translation = translation + " 01100110"
                    if letter in "g":
                        translation = translation + " 01100111"
                    if letter in "h":
                        translation = translation + " 01101000"
                    if letter in "i":
                        translation = translation + " 01101001"
                    if letter in "j":
                        translation = translation + " 01101010"
                    if letter in "k":
                        translation = translation + " 01101011"
                    if letter in "l":
                        translation = translation + " 01101100"
                    if letter in "m":
                        translation = translation + " 01101101"
                    if letter in "n":
                        translation = translation + " 01101110"
                    if letter in "o":
                        translation = translation + " 01101111"
                    if letter in "p":
                        translation = translation + " 01110000"
                    if letter in "q":
                        translation = translation + " 01110001"
                    if letter in "r":
                        translation = translation + " 01110010"
                    if letter in "s":
                        translation = translation + " 01110011"
                    if letter in "t":
                        translation = translation + " 01110100"
                    if letter in "u":
                        translation = translation + " 01110101"
                    if letter in "v":
                        translation = translation + " 01110110"
                    if letter in "w":
                        translation = translation + " 01110111"
                    if letter in "x":
                        translation = translation + " 01111000"
                    if letter in "y":
                        translation = translation + " 01111001"
                    if letter in "z":
                        translation = translation + " 01111010"

                    if letter in "A":
                        translation = translation + " 01000001"
                    if letter in "B":
                        translation = translation + " 01000010"
                    if letter in "C":
                        translation = translation + " 01000011"
                    if letter in "D":
                        translation = translation + " 01000100"
                    if letter in "E":
                        translation = translation + " 01000101"
                    if letter in "F":
                        translation = translation + " 01000110"
                    if letter in "G":
                        translation = translation + " 01000111"
                    if letter in "H":
                        translation = translation + " 01001000"
                    if letter in "I":
                        translation = translation + " 01001001"
                    if letter in "J":
                        translation = translation + " 01001010"
                    if letter in "K":
                        translation = translation + " 01001011"
                    if letter in "L":
                        translation = translation + " 01001100"
                    if letter in "M":
                        translation = translation + " 01001101"
                    if letter in "N":
                        translation = translation + " 01001110"
                    if letter in "O":
                        translation = translation + " 01001111"
                    if letter in "P":
                        translation = translation + " 01010000"
                    if letter in "Q":
                        translation = translation + " 01010001"
                    if letter in "R":
                        translation = translation + " 01010010"
                    if letter in "S":
                        translation = translation + " 01010011"
                    if letter in "T":
                        translation = translation + " 01010100"
                    if letter in "U":
                        translation = translation + " 01010101"
                    if letter in "V":
                        translation = translation + " 01010110"
                    if letter in "W":
                        translation = translation + " 01010111"
                    if letter in "X":
                        translation = translation + " 01011000"
                    if letter in "Y":
                        translation = translation + " 01011001"
                    if letter in "Z":
                        translation = translation + " 01011010"
                    if letter in "1":
                        translation = translation + " 00110001"
                    if letter in "2":
                        translation = translation + " 00110010"
                    if letter in "3":
                        translation = translation + " 00110011"
                    if letter in "4":
                        translation = translation + " 00110100"
                    if letter in "5":
                        translation = translation + " 00110101"
                    if letter in "6":
                        translation = translation + " 00110110"
                    if letter in "7":
                        translation = translation + " 00110111"
                    if letter in "8":
                        translation = translation + " 00111000"
                    if letter in "9":
                        translation = translation + " 00111001"
                    if letter in "0":
                        translation = translation + " 00110000"
                    if letter in " ":
                        translation = translation + " 00100000"
                    if letter in ".":
                        translation = translation + " 00101110"
                    if letter in "'":
                        translation = translation + " 00100111"
                    if letter in "?":
                        translation = translation + " 00111111"
                    if letter in "(":
                        translation = translation + " 00101000"
                    if letter in ")":
                        translation = translation + " 00101001"
                    if letter in "!":
                        translation = translation + " 00100001"
                    if letter in ",":
                        translation = translation + " 00101100"
                    if letter in "[":
                        translation = translation + " 01011011"
                    if letter in "]":
                        translation = translation + " 01011101"
                    if letter in "+":
                        translation = translation + " 00101011"
                    if letter in '"':
                        translation = translation + " 00100010"
                    else:
                        pass
                return translation
            phrase = translate(phrase)
            return phrase
            break
        except:
            pass
def strtobinarynospace(phrase):
    while True:
        try:
            def translate(phrase): #slightly different
                translation = ""
                for letter in phrase:
                    if letter in "a":
                        translation = translation + "01100001"
                    if letter in "b":
                        translation = translation + "01100010"
                    if letter in "c":
                        translation = translation + "01100011"
                    if letter in "d":
                        translation = translation + "01100100"
                    if letter in "e":
                        translation = translation + "01100101"
                    if letter in "f":
                        translation = translation + "01100110"
                    if letter in "g":
                        translation = translation + "01100111"
                    if letter in "h":
                        translation = translation + "01101000"
                    if letter in "i":
                        translation = translation + "01101001"
                    if letter in "j":
                        translation = translation + "01101010"
                    if letter in "k":
                        translation = translation + "01101011"
                    if letter in "l":
                        translation = translation + "01101100"
                    if letter in "m":
                        translation = translation + "01101101"
                    if letter in "n":
                        translation = translation + "01101110"
                    if letter in "o":
                        translation = translation + "01101111"
                    if letter in "p":
                        translation = translation + "01110000"
                    if letter in "q":
                        translation = translation + "01110001"
                    if letter in "r":
                        translation = translation + "01110010"
                    if letter in "s":
                        translation = translation + "01110011"
                    if letter in "t":
                        translation = translation + "01110100"
                    if letter in "u":
                        translation = translation + "01110101"
                    if letter in "v":
                        translation = translation + "01110110"
                    if letter in "w":
                        translation = translation + "01110111"
                    if letter in "x":
                        translation = translation + "01111000"
                    if letter in "y":
                        translation = translation + "01111001"
                    if letter in "z":
                        translation = translation + "01111010"

                    if letter in "A":
                        translation = translation + "01000001"
                    if letter in "B":
                        translation = translation + "01000010"
                    if letter in "C":
                        translation = translation + "01000011"
                    if letter in "D":
                        translation = translation + "01000100"
                    if letter in "E":
                        translation = translation + "01000101"
                    if letter in "F":
                        translation = translation + "01000110"
                    if letter in "G":
                        translation = translation + "01000111"
                    if letter in "H":
                        translation = translation + "01001000"
                    if letter in "I":
                        translation = translation + "01001001"
                    if letter in "J":
                        translation = translation + "01001010"
                    if letter in "K":
                        translation = translation + "01001011"
                    if letter in "L":
                        translation = translation + "01001100"
                    if letter in "M":
                        translation = translation + "01001101"
                    if letter in "N":
                        translation = translation + "01001110"
                    if letter in "O":
                        translation = translation + "01001111"
                    if letter in "P":
                        translation = translation + "01010000"
                    if letter in "Q":
                        translation = translation + "01010001"
                    if letter in "R":
                        translation = translation + "01010010"
                    if letter in "S":
                        translation = translation + "01010011"
                    if letter in "T":
                        translation = translation + "01010100"
                    if letter in "U":
                        translation = translation + "01010101"
                    if letter in "V":
                        translation = translation + "01010110"
                    if letter in "W":
                        translation = translation + "01010111"
                    if letter in "X":
                        translation = translation + "01011000"
                    if letter in "Y":
                        translation = translation + "01011001"
                    if letter in "Z":
                        translation = translation + "01011010"
                    if letter in "1":
                        translation = translation + "00110001"
                    if letter in "2":
                        translation = translation + "00110010"
                    if letter in "3":
                        translation = translation + "00110011"
                    if letter in "4":
                        translation = translation + "00110100"
                    if letter in "5":
                        translation = translation + "00110101"
                    if letter in "6":
                        translation = translation + "00110110"
                    if letter in "7":
                        translation = translation + "00110111"
                    if letter in "8":
                        translation = translation + "00111000"
                    if letter in "9":
                        translation = translation + "00111001"
                    if letter in "0":
                        translation = translation + "00110000"
                    if letter in " ":
                        translation = translation + "00100000"
                    if letter in ".":
                        translation = translation + "00101110"
                    if letter in "'":
                        translation = translation + "00100111"
                    if letter in "?":
                        translation = translation + "00111111"
                    if letter in "(":
                        translation = translation + "00101000"
                    if letter in ")":
                        translation = translation + "00101001"
                    if letter in "!":
                        translation = translation + "00100001"
                    if letter in ",":
                        translation = translation + "00101100"
                    if letter in "[":
                        translation = translation + "01011011"
                    if letter in "]":
                        translation = translation + "01011101"
                    if letter in "+":
                        translation = translation + "00101011"
                    if letter in '"':
                        translation = translation + "00100010"
                    else:
                        pass
                return translation
            phrase = translate(phrase)
            return phrase
            break
        except:
            pass
def binarytostrnospace(binary):
    while True:
            thing = list(binary)
            list_count = len(thing)
            binary_count = 1
            result = ""
            stop = False
            try:
                checker = int(thing[0])
            except:
                print("[+] You need to put proper binary code without spaces.")
                break
            break

    while not stop:
        try:
            for i in range(8):
                result = result + thing[0]
                del thing[0]
                binary_count += 1
            result = result + " "
            if binary_count == list_count:
                thing = result.split()
                list_count = len(thing)
                translation = binarytostrdo(result.split())
                return translation
                stop = True
                break
            if stop:
                break
        except IndexError:
            break
def binarytostrdo(thing):
    while True:
        try:
            list_count = len(thing)
            print(list_count)
            list_binary = ["01000001", "01000010", "01000011", "01000100", "01000101", "01000110", "01000111",
                           "01001000",
                           "01001001", "01001010", "01001011", "01001100", "01001101", "01001110", "01001111",
                           "01010000",
                           "01010001", "01010010", "01010011", "01010100", "01010101", "01010110", "01010111",
                           "01011000",
                           "01011001", "01011010"]
            list_binary2 = ["01100001", "01100010", "01100011", "01100100", "01100101", "01100110", "01100111",
                            "01101000",
                            "01101001", "01101010", "01101011", "01101100", "01101101", "01101110", "01101111",
                            "01110000",
                            "01110001", "01110010", "01110011", "01110100", "01110101", "01110110", "01110111",
                            "01111000",
                            "01111001", "01111010"]
            list_binary3 = ["00110001", "00110010", "00110011", "00110100", "00110101", "00110110", "00110111",
                            "00111000", "00111001", "00110000"]
            binary_space = "00100000"
            binary_period = "00101110"
            binary_apostraphe = "00100111"
            binary_quest = "00111111"
            binary_parenthases = ["00101000", "00101001"]  # ( )
            list_binary11 = ["1000001", "1000010", "1000011", "1000100", "1000101", "1000110", "1000111",
                             "1001000",
                             "1001001", "1001010", "1001011", "1001100", "1001101", "1001110", "1001111",
                             "1010000",
                             "1010001", "1010010", "1010011", "1010100", "1010101", "1010110", "1010111",
                             "1011000",
                             "1011001", "1011010"]
            list_binary22 = ["1100001", "1100010", "1100011", "1100100", "1100101", "1100110", "1100111",
                             "1101000",
                             "1101001", "1101010", "1101011", "1101100", "1101101", "1101110", "1101111",
                             "1110000",
                             "1110001", "1110010", "1110011", "1110100", "1110101", "1110110", "1110111",
                             "1111000",
                             "1111001", "1111010"]
            list_binary33 = ["0110001", "0110010", "0110011", "0110100", "0110101", "0110110", "0110111",
                             "0111000", "0111001", "0110000"]
            binary_space2 = "0100000"
            binary_period2 = "0101110"
            binary_apostraphe2 = "0100111"
            binary_quest2 = "0111111"
            binary_parenthases2 = ["0101000", "0101001"]  # ( )
            binary_exclamation = "00100001"
            binary_exclamation2 = "0100001"
            binary_comma = "00101100"
            binary_comma2 = "0101100"
            binary_sqaurebracks = ['01011011', "01011101"]#[]
            binary_sqaurebracks2 = ['1011011', "1011101"]
            binary_plus = "00101011"
            binary_plus2 = "0101011"
            binary_quot = "00100010"
            binary_quot2 = "0100010"
            translation = ""
            for i in range(list_count):
                if thing[i] == list_binary[0] or thing[i] == list_binary11[0]:
                    translation = translation + "A"
                elif thing[i] == list_binary[1] or thing[i] == list_binary11[1]:
                    translation = translation + "B"
                elif thing[i] == list_binary[2] or thing[i] == list_binary11[2]:
                    translation = translation + "C"
                elif thing[i] == list_binary[3] or thing[i] == list_binary11[3]:
                    translation = translation + "D"
                elif thing[i] == list_binary[4] or thing[i] == list_binary11[4]:
                    translation = translation + "E"
                elif thing[i] == list_binary[5] or thing[i] == list_binary11[5]:
                    translation = translation + "F"
                elif thing[i] == list_binary[6] or thing[i] == list_binary11[6]:
                    translation = translation + "G"
                elif thing[i] == list_binary[7] or thing[i] == list_binary11[7]:
                    translation = translation + "H"
                elif thing[i] == list_binary[8] or thing[i] == list_binary11[8]:
                    translation = translation + "I"
                elif thing[i] == list_binary[9] or thing[i] == list_binary11[9]:
                    translation = translation + "J"
                elif thing[i] == list_binary[10] or thing[i] == list_binary11[10]:
                    translation = translation + "K"
                elif thing[i] == list_binary[11] or thing[i] == list_binary11[11]:
                    translation = translation + "L"
                elif thing[i] == list_binary[12] or thing[i] == list_binary11[12]:
                    translation = translation + "M"
                elif thing[i] == list_binary[13] or thing[i] == list_binary11[13]:
                    translation = translation + "N"
                elif thing[i] == list_binary[14] or thing[i] == list_binary11[14]:
                    translation = translation + "O"
                elif thing[i] == list_binary[15] or thing[i] == list_binary11[15]:
                    translation = translation + "P"
                elif thing[i] == list_binary[16] or thing[i] == list_binary11[16]:
                    translation = translation + "Q"
                elif thing[i] == list_binary[17] or thing[i] == list_binary11[17]:
                    translation = translation + "R"
                elif thing[i] == list_binary[18] or thing[i] == list_binary11[18]:
                    translation = translation + "S"
                elif thing[i] == list_binary[19] or thing[i] == list_binary11[19]:
                    translation = translation + "T"
                elif thing[i] == list_binary[20] or thing[i] == list_binary11[20]:
                    translation = translation + "U"
                elif thing[i] == list_binary[21] or thing[i] == list_binary11[21]:
                    translation = translation + "V"
                elif thing[i] == list_binary[22] or thing[i] == list_binary11[22]:
                    translation = translation + "W"
                elif thing[i] == list_binary[23] or thing[i] == list_binary11[23]:
                    translation = translation + "X"
                elif thing[i] == list_binary[24] or thing[i] == list_binary11[24]:
                    translation = translation + "Y"
                elif thing[i] == list_binary[25] or thing[i] == list_binary11[25]:
                    translation = translation + "Z"

                elif thing[i] == list_binary2[0] or thing[i] == list_binary22[0]:
                    translation = translation + "a"
                elif thing[i] == list_binary2[1] or thing[i] == list_binary22[1]:
                    translation = translation + "b"
                elif thing[i] == list_binary2[2] or thing[i] == list_binary22[2]:
                    translation = translation + "c"
                elif thing[i] == list_binary2[3] or thing[i] == list_binary22[3]:
                    translation = translation + "d"
                elif thing[i] == list_binary2[4] or thing[i] == list_binary22[4]:
                    translation = translation + "e"
                elif thing[i] == list_binary2[5] or thing[i] == list_binary22[5]:
                    translation = translation + "f"
                elif thing[i] == list_binary2[6] or thing[i] == list_binary22[6]:
                    translation = translation + "g"
                elif thing[i] == list_binary2[7] or thing[i] == list_binary22[7]:
                    translation = translation + "h"
                elif thing[i] == list_binary2[8] or thing[i] == list_binary22[8]:
                    translation = translation + "i"
                elif thing[i] == list_binary2[9] or thing[i] == list_binary22[9]:
                    translation = translation + "j"
                elif thing[i] == list_binary2[10] or thing[i] == list_binary22[10]:
                    translation = translation + "k"
                elif thing[i] == list_binary2[11] or thing[i] == list_binary22[11]:
                    translation = translation + "l"
                elif thing[i] == list_binary2[12] or thing[i] == list_binary22[12]:
                    translation = translation + "m"
                elif thing[i] == list_binary2[13] or thing[i] == list_binary22[13]:
                    translation = translation + "n"
                elif thing[i] == list_binary2[14] or thing[i] == list_binary22[14]:
                    translation = translation + "o"
                elif thing[i] == list_binary2[15] or thing[i] == list_binary22[15]:
                    translation = translation + "p"
                elif thing[i] == list_binary2[16] or thing[i] == list_binary22[16]:
                    translation = translation + "q"
                elif thing[i] == list_binary2[17] or thing[i] == list_binary22[17]:
                    translation = translation + "r"
                elif thing[i] == list_binary2[18] or thing[i] == list_binary22[18]:
                    translation = translation + "s"
                elif thing[i] == list_binary2[19] or thing[i] == list_binary22[19]:
                    translation = translation + "t"
                elif thing[i] == list_binary2[20] or thing[i] == list_binary22[20]:
                    translation = translation + "u"
                elif thing[i] == list_binary2[21] or thing[i] == list_binary22[21]:
                    translation = translation + "v"
                elif thing[i] == list_binary2[22] or thing[i] == list_binary22[22]:
                    translation = translation + "w"
                elif thing[i] == list_binary2[23] or thing[i] == list_binary22[23]:
                    translation = translation + "x"
                elif thing[i] == list_binary2[24] or thing[i] == list_binary22[24]:
                    translation = translation + "y"
                elif thing[i] == list_binary2[25] or thing[i] == list_binary22[25]:
                    translation = translation + "z"

                elif thing[i] == list_binary3[0] or thing[i] == list_binary33[0]:
                    translation = translation + "1"
                elif thing[i] == list_binary3[1] or thing[i] == list_binary33[1]:
                    translation = translation + "2"
                elif thing[i] == list_binary3[2] or thing[i] == list_binary33[2]:
                    translation = translation + "3"
                elif thing[i] == list_binary3[3] or thing[i] == list_binary33[3]:
                    translation = translation + "4"
                elif thing[i] == list_binary3[4] or thing[i] == list_binary33[4]:
                    translation = translation + "5"
                elif thing[i] == list_binary3[5] or thing[i] == list_binary33[5]:
                    translation = translation + "6"
                elif thing[i] == list_binary3[6] or thing[i] == list_binary33[6]:
                    translation = translation + "7"
                elif thing[i] == list_binary3[7] or thing[i] == list_binary33[7]:
                    translation = translation + "8"
                elif thing[i] == list_binary3[8] or thing[i] == list_binary33[8]:
                    translation = translation + "9"
                elif thing[i] == list_binary3[9] or thing[i] == list_binary33[9]:
                    translation = translation + "0"
                elif thing[i] == binary_space or thing[i] == binary_space2:
                    translation = translation + " "
                elif thing[i] == binary_period or thing[i] == binary_period2:
                    translation = translation + "."
                elif thing[i] == binary_apostraphe or thing[i] == binary_apostraphe:
                    translation = translation + "'"
                elif thing[i] == binary_quest or thing[i] == binary_quest2:
                    translation = translation + "?"
                elif thing[i] == binary_parenthases[0] or thing[i] == binary_parenthases2[0]:
                    translation = translation + "("
                elif thing[i] == binary_parenthases[1] or thing[i] == binary_parenthases2[1]:
                    translation = translation + ")"
                elif thing[i] == binary_exclamation or thing[i] == binary_exclamation2:
                    translation = translation + "!"
                elif thing[i] == binary_comma or thing[i] == binary_comma2:
                    translation = translation + ","
                elif thing[i] == binary_sqaurebracks[0] or thing[i] == binary_sqaurebracks2[0]:
                    translation = translation + "["
                elif thing[i] == binary_sqaurebracks[1] or thing[i] == binary_sqaurebracks2[1]:
                    translation = translation + "]"
                elif thing[i] == binary_plus or thing[i] == binary_plus2:
                    translation = translation + "+"
                elif thing[i] == binary_quot or thing[i] == binary_quot2:
                    translation = translation + '"'
                else:
                    pass
            return translation
            break
        except:
            break
bot = commands.Bot(command_prefix='!')
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    print("Ready to begin doing tasks.")

@client.event
async def on_message(message):
    if message.content.startswith('?info'):
        await message.channel.send(f'Welcome to Squid Bot {message.author.mention}. This bot has been coded by DrSquid™#7711. In this bot there are some random features that you can do. Please note that this bot is still in development. Do ?help if you want to get started on anything.')
        await message.author.send(f'Welcome to Squid Bot {message.author.mention}. This bot has been coded by DrSquid™#7711. In this bot there are some random features that you can do. Please note that this bot is still in development. Do ?help if you want to get started on anything.')
    elif message.content.startswith('?help'):
        await message.channel.send(f'Here is a list of commands that you can use:\n```?help - This is displayed by this command\n?info - Gives info about bot.\n?devFavPkm - gives some of the devs favorite pokemon.\n?yoinkIP <domain_name> - Obtains the IP of a domain name(DO NOT USE THIS FOR NEFARIOUS PURPOSES)\n?trackIP <domain_name> - Tracks a given IP Address\n?special - Very special command. Try it out!\n?strtobinary <string> - Translates a string into binary\n?binarytostr <binary> - Translates binary into strings\n?strtobinary2 <binary> - Also translates binary into strings(slightly different)\n?diceRoll <first_num> <second_num> - Rolls a random number from the inputted range.\n?tts <string> - Sends a tts message\n?punch <entity> - Punches whatever is in the arguements\n?shrek - Spams the whole shrek movie script\n?beemovie - Spams the whole bee movie script\n?yeet <entity> - Yeets whatever is in the arguements\n?coinflip <heads/tails> - Flips an imaginary coin | This also does not require arguements.\n?devPCsetup - Check the devs PC setup\n?devFlex - Dev flexing his pokemon save file\n?wouldyourather - Asks a would you rather question\n?currenttime - Shows the current time in the devs time zone\n?slap <entity> - Slaps whatever is in the arguements\n?strtohash <string> - Encodes a string in an MD5 Hash\n?highfive <entity> - High fives whatever is in the arguments\n\na?kick <user> - Kicks a user from the server\na?ban <user> - Bans a user from the server```')
    elif message.content.startswith('?devFavPkm'):
        await message.channel.send('Some of the Developers favorite pokemon include: Mewtwo, Calyrex, Zacian, Sobble, Inteleon, Greninja, Charizard, Eternatus, Lucario, Rhydon, Lapras, Gengar, and Many more.')
    elif message.content.startswith('?yoinkIP'):
        msg = message.content
        msg = msg.split()
        if len(msg) == 2:
            try:
                ip = msg[1]
                ip1 = socket.gethostbyname(ip)
                await message.channel.send(f'IP of {ip} is: {ip1}')
            except:
                await message.channel.send(f'There was an error with getting the IP. Please try retyping the command.')
        else:
            await message.channel.send('You have entered the command incorrectly.\nUsage: ```?yoinkIP <domain_name>```')
    elif message.content.startswith('?trackIP'):
        msg = message.content
        msg = msg.split()
        if len(msg) == 2:
            try:
                ip = msg[1]
                ip = socket.gethostbyname(ip)
                ip = geocoder.ip(ip)
                await message.channel.send(f'Latitude and Longitude Coordinates Found: {ip.latlng}')
                await message.channel.send(f'Geolocation Info:```\n{ip.geojson}```')
            except:
                await message.channel.send(f'There was an error tracking the IP. Please try retyping the command.')
        else:
            await message.channel.send('You have entered the command incorrectly.\nUsage: ```?trackIP <domain_name>```')
    elif message.content.startswith('?special'):
        await message.channel.send(f'A very special thing is about to happen to you, {message.author.mention}!')
        time.sleep(4)
        file = open('rick_roll.txt', 'r')
        await message.channel.send('https://tenor.com/view/rickroll-dance-funny-you-music-gif-7755460')
        await message.channel.send(f'{message.author.mention} Imagine Getting Rick Rolled in {datetime.date.today().year} LMAO CANT RELATE LOL')
        time.sleep(3)
        for i in file.readlines():
            await message.channel.send(i, tts=True)
            time.sleep(3)
    elif message.content.startswith('?strtobinary'):
        msg = message.content
        msg = msg.split()
        del msg[0]
        if len(msg) >= 1:
            string = ""
            for i in msg:
                string = string + i + " "
            translation = strtobinarynospace(string)
            await message.channel.send(f'Translation to binary: {translation}')
        else:
            await message.channel.send(
                f'{message.author.mention}, you have entered the command incorrectly.\nUsage:```?strtobinary <string>```')
    elif message.content.startswith('?binarytostr'):
        msg = message.content
        msg = msg.split()
        del msg[0]
        if len(msg) >= 1:
            string = ""
            for i in msg:
                string = string + i + " "
            translation = binarytostrnospace(string)
            await message.channel.send(f'Translation from binary: {translation}')
        else:
            await message.channel.send(f'{message.author.mention}, you have entered the command incorrectly.\nUsage:```?binarytostr <binary>```')
    elif message.content.startswith('?binarytostr2'):
        msg = message.content
        msg = msg.split()
        del msg[0]
        if len(msg) >= 1:
            string = ""
            for i in msg:
                string = string + i + " "
            translation = binarytostrdo(string)
            await message.channel.send(f'Translation from binary: {translation}')
        else:
            await message.channel.send(f'{message.author.mention}, you have entered the command incorrectly.\nUsage:```?binarytostr2 <binary>```')
    elif message.content.startswith('?diceRoll'):
        msg = message.content
        msg = msg.split()
        del msg[0]
        if len(msg) != 2:
            await message.channel.send(f'{message.author.mention}, you have entered the command incorrectly.\nEnter them like this:```?diceRoll <first_num> <second_num>```')
        elif len(msg) == 2:
            try:
                first_num = int(msg[0])
                second_num = int(msg[1])
                result = random.randint(first_num, second_num)
                await message.channel.send(f'{message.author.mention}, your random number is: {result}')
            except:
                await message.channel.send(f'{message.author.mention}, you need to enter numbers for the command, and not str.')
    elif message.content.startswith('?tts'):
        msg = message.content
        msg = msg.split()
        del msg[0]
        if len(msg) == 0:
            await message.channel.send(f'{message.author.mention}, you have entered the command incorrectly.\nUsage:```?tts <string>```')
        else:
            result = ""
            for i in msg:
                result = result + i + " "
            await message.channel.send(f'{message.author.mention}: {result}', tts=True)
    elif f"{client.user.id}" in message.content:
        if message.author == client.user:
            pass
        else:
            await message.channel.send(f'{message.author.mention}, why did you @ me?')
    elif message.content.startswith('?punch'):
        msg = message.content
        msg = msg.split()
        del msg[0]
        if len(msg) >= 1:
            result = ""
            for i in msg:
                result = result + i + " "
            if f'{client.user.id}' in result:
                await message.channel.send(f'Are you seriously gonna punch me, {message.author.mention}?')
            elif f'{message.author.id}' in result:
                await message.channel.send(f'Dont punch yourself, {message.author.mention}!')
            else:
                await message.channel.send(f'{message.author.mention} has punched {result}!')
                await message.channel.send('https://i.imgur.com/ljXIKBF.gif?noredirect')
        else:
            await message.channel.send(f'{message.author.mention}, you have entered the command incorrectly.\nUsage:```?punch <entity>```')
    elif message.content.startswith('?shrek'):
        file = open('shrek.txt', 'r')
        for i in file:
            i = i.split()
            for item in i:
                await message.channel.send(item)
                time.sleep(0.8)
    elif message.content.startswith('?beemovie'):
        file = open('beemovie.txt', 'rb')
        for i in file:
            i = i.split()
            for item in i:
                item = item.decode()
                await message.channel.send(item)
                time.sleep(0.8)
    elif message.content.startswith('?yeet'):
        gifs = ['https://68.media.tumblr.com/3de7aaa7732a84ab7bd4d6b1cf789451/tumblr_oebuutb05G1rc0cy9o1_500.gif']
        msg = message.content
        msg = msg.split()
        del msg[0]
        if len(msg) >= 1:
            result = ""
            for i in msg:
                result = result + i + " "
            if f'{client.user.id}' in result:
                await message.channel.send(f'Are you seriously gonna yeet me, {message.author.mention}?')
            elif f'{message.author.id}' in result:
                await message.channel.send(f'Dont yeet yourself, {message.author.mention}!')
            else:
                await message.channel.send(f'{message.author.mention} has yeeted {result}!')
                await message.channel.send(gifs[random.randint(0, (len(gifs) - 1))])
        else:
            await message.channel.send(
                f'{message.author.mention}, you have entered the command incorrectly.\nUsage:```?yeet <entity>```')
    elif message.content.startswith('?coinflip'):
        flips = ['heads', 'tails']
        msg = message.content
        msg = msg.split()
        del msg[0]
        if len(msg) == 0:
            flips = ['heads', 'tails']
            flip = flips[random.randint(0, 1)]
            await message.channel.send(f'The coin has flipped on: {flip}')
        elif msg[0] not in flips:
            await message.channel.send(f'{message.author.mention}, you have entered the command incorrectly.\nUsage:```?coinflip <heads/tails> | This also does not require arguements.```')
        else:
            result = ""
            for i in msg:
                result = result + i + " "
            result = result.strip()
            flip = flips[random.randint(0,1)]
            if flip == result:
                await message.channel.send(f'You win! The coin has flipped on: {flip}')
            else:
                await message.channel.send(f'You lose. The coin has flipped on: {flip}')
    elif message.content.startswith('?devPCsetup'):
        await message.channel.send('```DrSquids PC Setup:\n\nComputer:\n\nIntel Core i7 2.60-4.50Ghz\nRTX 2080 Mobile GPU\n16GB 2667Mhz DDR4 RAM\n512GB SSD\n\nSetup:\n\n240Hz Laptop Screen\n75Hz 27inch BenQ Monitor\nRazer Laptop Keyboard\nMagic Keyboard\nSteel Series Rival 650 Wireless```')
    elif message.content.startswith('?devFlex'):
        await message.channel.send('https://media.discordapp.net/attachments/715858757745246300/797052256557334528/image0.jpg?width=1202&height=676')
        await message.channel.send('https://media.discordapp.net/attachments/715858757745246300/797052257074020362/image1.jpg?width=1202&height=676')
    elif message.content.startswith('?wouldyourather'):
        global response
        response = False
        aList = ['live on Mars', 'Live UnderWater', 'Be Mewtwo', 'Have Smallpp', 'choose B','choose A', 'play Minecraft', 'play Pokemon']
        bList = ['live on Moon', 'Be Mew', 'Have bigPP', 'choose A', 'Choose B']
        global a
        global b
        a = aList[random.randint(0, (len(aList) - 1))]
        b = bList[random.randint(0, (len(bList) - 1))]
        await message.channel.send(f'Would you rather: ```A) {a}``` or ```B) {b}```Answer below guys/girls!')
        response = True
    elif response:
        if message.content.lower() == 'a':
            await message.channel.send(f'{message.author.mention} would rather {a}!')
        if message.content.lower() == 'b':
            await message.channel.send(f'{message.author.mention} would rather {b}!')
    elif message.content.startswith('?currenttime'):
        await message.channel.send(f'The current time in DrSquids area is:```{datetime.datetime.today()}```')
    elif message.content.startswith('hello') or message.content.startswith('Hello') or message.content.startswith('hi') or message.content.startswith('Hi'):
        if message.author == client.user or 'hello there' in message.content.lower():
            pass
        else:
            global response2
            response2 = False
            await message.channel.send(f'Hello, {message.author.mention}.')
            roll = random.randint(1, 3)
            if roll == 2:
                await message.channel.send('How are you today?')
                response2 = True
    elif response2:
        good_response = ['good', 'great', 'nice', 'fine', 'excited', 'happy']
        ok_response = ['ok', 'idk', 'not sure', 'okay', 'moderate']
        sad_response = ['bad', 'sad', 'not good', 'unhappy', 'mad', 'not ok']
        msg = message.content
        msg = msg.split()
        for i in msg:
            if i in good_response:
                if message.content == 'not good':
                    pass
                elif message.author == client.user:
                    pass
                else:
                    await message.channel.send(f'Thats good to hear, {message.author.mention}.')
                    response2 = False
            elif i in ok_response:
                if message.author == client.user:
                    pass
                else:
                    await message.channel.send('Oh.')
                    response2 = False
            elif i in sad_response:
                if message.author == client.user:
                    pass
                else:
                    await message.channel.send(f'Hopefully you feel better soon, {message.author.mention}.')
                    response2 = False
        if 'thanks' in message.content.lower():
                if message.author == client.user:
                    pass
                else:
                    await message.channel.send('Youre Welcome.')
        elif 'how are you' in message.content.lower():
            if message.author == client.user:
                pass
            else:
                await message.channel.send('I am good, Thanks!')
    elif message.content.startswith('?slap'):
        msg = message.content
        msg = msg.split()
        del msg[0]
        if len(msg) == 1:
            if msg[0] != client.user.id:
                if f'{message.author.id}' in msg[0]:
                    await message.channel.send(f'Dont slap yourself, {message.author.mention}!')
                else:
                    await message.channel.send(f'{message.author.mention} has slapped {msg[0]}!')
                    await message.channel.send('https://media1.tenor.com/images/00c5fccb342d79bb56cf93c768534b5a/tenor.gif?itemid=4723816')
            else:
                await message.channel.send(f'Dont Slap me, {message.author.mention}!')
        else:
            await message.channel.send(f'{message.author.mention}, you have entered the command incorrectly.\nUsage:```?slap <entity>```')
    if "hello there" in message.content.lower():
        await message.channel.send('General Kenobi.')
    elif message.content.startswith('?strtohash'):
        msg = message.content
        msg = msg.split()
        del msg[0]
        result = ""
        for i in msg:
            result = result + i + " "
        result = result.strip()
        enc_result = result.encode('utf-8')
        digest = hashlib.md5(enc_result.strip()).hexdigest()
        await message.channel.send(f'The Hashed version of {result} is: {digest}')
    if badwords[0] in message.content.lower() or badwords[1] in message.content.lower() or badwords[2] in message.content.lower() or badwords[3] in message.content.lower() or badwords[4] in message.content.lower() or badwords[5] in message.content.lower():
        await message.channel.send(f'Watch your language, {message.author.mention}!')
        await message.delete()
    elif message.content.startswith('?highfive'):
        gifs = ['https://thumbs.gfycat.com/OldfashionedLawfulKangaroo-size_restricted.gif']
        msg = message.content
        msg = msg.split()
        del msg[0]
        if len(msg) >= 1:
            result = ""
            for i in msg:
                result = result + i + " "
            if f'{message.author.id}' in result:
                await message.channel.send(f'If you highfived yourself, you are basically clapping, {message.author.mention}!')
            else:
                await message.channel.send(f'{message.author.mention} has highfived {result}!')
                await message.channel.send(gifs[random.randint(0, (len(gifs) - 1))])
        else:
            await message.channel.send(f'{message.author.mention}, you have entered the command incorrectly.\nUsage:```?highfive <entity>```')

client.run('token')
