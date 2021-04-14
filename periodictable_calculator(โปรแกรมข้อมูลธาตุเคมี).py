from tkinter import *

me = Tk()
me.geometry("851x500")
me.title("Periodic table")
melabel = Label(me, text="Periodic table", bg='White', font=("Times", 30, 'bold'))
melabel.pack(side=TOP)
me.config(background='#f8d0d1')

textin = StringVar()
operator = ""

def clickbut(number):  # lambda:clickbut(1)
    global operator
    operator = operator + str(number)
    textin.set(operator)


def name():
    global operator
    if 0<int(operator) <= 118:
        all = {1: 'Hydrogen', 2: 'Helium', 3: 'lithium', 4: 'Beryllium', 5: 'Boron', 6: 'Carbon',
               7: 'Nitrogen', 8: 'Oxygen', 9: 'Fluorine', 10: 'Neon', 11: 'Sodium', 12: 'Magnesium',
               13: 'Aluminium', 14: 'Silicon', 15: 'Phosphorus', 16: 'Sulphur', 17: 'Chlorine',
               18: 'Argon', 19: 'Potassium', 20: 'Calcium', 21: 'Scandium', 22: 'Titanium',
               23: 'Vanadium', 24: 'Chromium', 25: 'Manganese', 26: 'Iron', 27: 'Cobalt', 28: 'Nickel',
               29: 'Copper', 30: 'Zinc', 31: 'Gallium', 32: 'Germanium', 33: 'Arsenic', 34: 'Selenium',
               35: 'Bromine', 36: 'Krypton', 37: 'Rubidium', 38: 'Strontium', 39: 'Yttrium',
               40: 'Zirconium', 41: 'Niobium', 42: 'Molybdenum', 43: 'Technetium', 44: 'Ruthenium',
               45: 'Rhodium', 46: 'Palladium', 47: 'Silver', 48: 'Cadmium', 49: 'Indium', 50: 'Tin',
               51: 'Antimony', 52: 'Tellurium', 53: 'Iodine', 54: 'Xenon', 55: 'Cesium', 56: 'Barium',
               57: 'Lanthanum', 58: 'Cerium', 59: 'Praseodymium', 60: 'Neodymium', 61: 'Promethium',
               62: 'Samarium', 63: 'Europium', 64: 'Gadolinium', 65: 'Terbium', 66: 'Dysprosium',
               67: 'Holmium', 68: 'Erbium', 69: 'Thulium', 70: 'Ytterbium', 71: 'Lutetium',
               72: 'Hafnium', 73: 'Tantalum', 74: 'Tungsten', 75: 'Rhenium', 76: 'Osmium',
               77: 'Iridium', 78: 'Platinum', 79: 'Gold', 80: 'Mercury', 81: 'Thallium', 82: 'Lead',
               83: 'Bismuth', 84: 'Polonium', 85: 'astatine', 86: 'Radon', 87: 'Francium',
               88: 'Radium', 89: 'Actinium', 90: 'Thorium', 91: 'Protactinium', 92: 'Uranium',
               93: 'Neptunium', 94: 'Plutonium', 95: 'Americium', 96: 'Curium', 97: 'Berkelium',
               98: 'Californium', 99: 'Einsteinium', 100: 'Fermium', 101: 'Mendelevium',
               102: 'Nobelium', 103: 'Lawrencium', 104: 'Rutherfordium', 105: 'Dubnium',
               106: 'Seaborgium', 107: 'Bohrium', 108: 'Hassium', 109: 'Meitnerium',
               110: 'Darmstudium', 111: 'Roentgenium', 112: 'Copernicium', 113: 'Nihonium',
               114: 'Flerovium', 115: 'Moscovium', 116: 'Livermorium', 117: 'Tennessine',
               118: 'Oganesson'}
        add =  all[int(operator)]
        textin.set(add)
        operator = ''
    else:
        textin.set('ERROR please enter number in range 1 to 118')
        operator = ''
def electron():
    global operator
    if 0 < int(operator) <= 118:
        all = {1: '1', 2: '2', 3: '2 1', 4: '2 2', 5: '2 3', 6: '2 4', 7: '2 5', 8: '2 6', 9: '2 7', 10: '2 8',
                11: '2 8 1', 12: '2 8 2 ', 13: '2 8 3', 14: '2 8 4', 15: '2 8 5', 16: '2 8 6', 17: '2 8 7', 18: '2 8 8',
                19: '2 8 8 1', 20: '2 8 8 2', 21: '2 8 9 2', 22: '2 8 10 2', 23: '2 8 11 2', 24: '2 8 13 1',
                25: '2 8 13 2', 26: '2 8 14 2', 28: '2 8 16 2', 29: '2 8 18 1', 30: '2 8 18 2', 31: '2 8 18 3',
                32: '2 8 18 4', 33: '2 8 18 5', 34: '2 8 18 6', 35: '2 8 18 7', 36: '2 8 18 8', 37: '2 8 18 8 1',
                38: '2 8 18 8 2', 39: '2 8 18 9 2', 40: '2 8 18 10 2', 41: '2 8 18 12 1', 42: '2 8 18 13 1',
                43: '2 8 18 13 2', 44: '2 8 18 15 1', 45: '3 8 18 16 13', 46: '2 8 18 18', 47: '2 8 18 18 1',
                48: '2 8 18 18 2', 49: '2 8 18 18 3', 50: '2 8 18 18 4', 51: '2 8 18 18 5', 52: '2 8 18 18 6',
                53: '2 8 18 18 7', 54: '2 8 18 18 8', 55: ' 2 8 18 18 8 1', 56: '2 8 18 18 8 2', 57: '2 8 18 18 9 2',
                58: ' 2 8 18 19 9 2', 59: '2 8 18 21 8 2', 60: '2 8 18 22 8 2', 61: '2 8 18 23 8 2',
                62: '2 8 18 24 8 2', 63: '2 8 18 25 8 2', 64: '2 8 18 25 9 2', 65: '2 8 18 27 8 2', 66: '2 8 18 28 8 2',
                67: '2 8 18 29 8 2', 68: '2 8 18 30 8 2', 69: '2 8 18 31 8 2', 70: '2 8 18 32 8 2',
                71: ' 2 8 18 32 9 2', 72: '2 8 18 32 10 2', 73: '2 8 18 32 11 2', 74: '2 8 18 32 12 2',
                75: '2 8 18 32 13 2', 76: '2 8 18 32 14 2', 77: '2 8 18 32 15 2', 78: '2 8 18 32 17 1',
                79: '2 8 18 32 18 1', 80: '2 8 18 32 18 2', 81: '2 8 18 32 18 3', 82: '2 8 18 32 18 4',
                83: '2 8 18 32 18 5', 84: '2 8 18 32 18 6', 85: '2 8 18 32 18 7', 86: '2 8 18 32 18 8',
                87: '2 8 18 32 18 8 1', 88: '2 8 18 32 18 8 2', 89: '2 8 18 32 18 9 2', 90: '2 8 18 32 18 10 2',
                91: '2 8 18 32 20 9 2', 92: '2 8 18 32 21 9 2', 93: '2 8 18 32 22 9 2', 94: '2 8 18 32 24 8 2',
                95: '2 8 18 32 25 8 2', 96: '2 8 18 32 25 9 2', 97: '2 8 18 32 27 8 2', 98: '2 8 18 32 28 8 2',
                99: '2 8 18 32 29 8 2', 100: '2 8 18 32 30 8 2', 101: '2 8 18 32 31 8 2', 102: '2 8 18 32 32 8 2',
                103: '2 8 18 32 32 8 3', 104: '2 8 18 32 32 10 2', 105: '2 8 18 32 32 11 2', 106: '2 8 18 32 32 12 2',
                107: '2 8 18 32 32 13 2', 108: '2 8 18 32 32 14 2', 109: '2 8 18 32 32 15 2', 110: '2 8 18 32 32 17 1',
                111: '2 8 18 32 32 18 1', 112: '2 8 18 32 32 18 2', 113: '2 8 18 32 32 18 3', 114: '2 8 18 32 32 18 4',
                115: '2 8 18 32 32 18 5', 116: '2 8 18 32 32 18 6', 117: '2 8 18 32 32 18 7', 118: '2 8 18 32 32 18 8'}
        add = all[int(operator)]
        textin.set(add)
        operator = ''
    else:
        textin.set('ERROR please enter number in range 1 to 118')
        operator = ''
def subshell():
    global operator
    if 0 < int(operator) <= 118:
        all = {1: '1s1', 2: '1s2', 3: '1s2 2s1', 4: '1s2 2s2', 5: '1s2 2s2 2p1', 6: '1s2 2s2 2p2',
                     7: '1s2 2s2 2p3', 8: '1s2 2s2 2p4', 9: '1s2 2s2 2p5', 10: '1s2 2s2 2p6', 11: '1s2 2s2 2p6 3s1',
                     12: '1s2 2s2 2p6 3s2', 13: '1s2 2s2 2p6 3s2 3p1', 14: '1s2 2s2 2p6 3s2 3p2',
                     15: '1s2 2s2 2p6 3s2 3p3', 16: '1s2 2s2 2p6 3s2 3p4', 17: '1s2 2s2 2p6 3s2 3p5',
                     18: '1s2 2s2 2p6 3s2 3p6', 19: '1s2 2s2 2p6 3s2 3p6 4s1', 20: '1s2 2s2 2p6 3s2 3p6 4s2',
                     21: '1s2 2s2 2p6 3s2 3p6 3d1 4s2', 22: '1s2 2s2 2p6 3s2 3p6 3d2 4s2',
                     23: '1s2 2s2 2p6 3s2 3p6 3d3 4s2', 24: '1s2 2s2 2p6 3s2 3p6 3d5 4s1',
                     25: '1s2 2s2 2p6 3s2 3p6 3d5 4s2', 26: '1s2 2s2 2p6 3s2 3p6 3d6 4s2',
                     27: '1s2 2s2 2p6 3s2 3p6 3d7 4s2', 28: '1s2 2s2 2p6 3s2 3p6 3d8 4s2',
                     29: '1s2 2s2 2p6 3s2 3p6 3d10 4s1', 30: '1s2 2s2 2p6 3s2 3p6 3d10 4s2',
                     31: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p1', 32: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p2',
                     33: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p3', 34: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p4',
                     35: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p5', 36: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6',
                     37: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 5s1', 38: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 5s2',
                     39: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d1 5s2', 40: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d2 5s2',
                     41: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d3 5s2', 42: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d5 5s1',
                     43: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d5 5s2', 44: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d7 5s1',
                     45: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d8 5s1', 46: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10',
                     47: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s1',
                     48: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2',
                     49: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p1',
                     50: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p2',
                     51: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p3',
                     52: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p4',
                     53: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p5',
                     54: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6',
                     55: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 6s1',
                     56: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 6s2',
                     57: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 5d1 6s2',
                     58: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f1 5s2 5p6 5d1 6s2',
                     59: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f3 5s2 5p6 6s2',
                     60: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f4 5s2 5p6 6s2',
                     61: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f5 5s2 5p6 6s2',
                     62: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f6 5s2 5p6 6s2',
                     63: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f7 5s2 5p6 6s2',
                     64: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f8 5s2 5p6 6s2',
                     65: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f9 5s2 5p6 6s2',
                     66: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f10 5s2 5p6 6s2',
                     67: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f11 5s2 5p6 6s2',
                     68: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f12 5s2 5p6 6s2',
                     69: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f13 5s2 5p6 6s2',
                     70: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 6s2',
                     71: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d1 6s2',
                     72: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d2 6s2',
                     73: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d3 6s2',
                     74: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d4 6s2',
                     75: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d5 6s2',
                     76: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d6 6s2',
                     77: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d7 6s2',
                     78: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d9 6s1',
                     79: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s1',
                     80: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2',
                     81: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p1',
                     82: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p2',
                     83: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p3',
                     84: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p4',
                     85: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p5',
                     86: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6',
                     87: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 7s1',
                     88: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 7s2',
                     89: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 6d1 7s2',
                     90: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 6d2 7s2',
                     91: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f2 6s2 6p6 6d1 7s2',
                     92: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f3 6s2 6p6 6d1 7s2',
                     93: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f4 6s2 6p6 6d1 7s2',
                     94: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f6 6s2 6p6 7s2',
                     95: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f7 6s2 6p6 7s2',
                     96: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f7 6s2 6p6 6d1 7s2',
                     97: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f9 6s2 6p6 7s2',
                     98: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f10 6s2 6p6 7s2',
                     99: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f11 6s2 6p6 7s2',
                     100: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f12 6s2 6p6 7s2',
                     101: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f13 6s2 6p6 7s2',
                     102: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 7s2',
                     103: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 7s2 7p1',
                     104: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d2 7s2',
                     105: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d3 7s2',
                     106: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d4 7s2',
                     107: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d5 7s2',
                     108: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d6 7s2',
                     109: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d7 7s2',
                     110: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d8 7s2',
                     111: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d9 7s2',
                     112: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d10 7s2',
                     113: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d10 7s2 7p1',
                     114: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d10 7s2 7p2',
                     115: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d10 7s2 7p3',
                     116: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d10 7s2 7p4',
                     117: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d10 7s2 7p5',
                     118: '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d10 7s2 7p6'}
        add = all[int(operator)]
        textin.set(add)
        operator = ''
    else:
        textin.set('ERROR please enter number in range 1 to 118')
        operator = ''
def clrbut():
    global operator
    textin.set('')
    operator = ''

metext = Entry(me, font=("Courier New", 12, 'bold'), textvar=textin, width=82, bd=5, bg='powder blue')
metext.pack()

but1 = Button(me, padx=14, pady=14, bd=4, bg='#ed0779', command=lambda: clickbut(1), text="1",
              font=("Courier New", 16, 'bold'))
but1.place(x=317, y=100)

but2 = Button(me, padx=14, pady=14, bd=4, bg='#ed0779', command=lambda: clickbut(2), text="2",
              font=("Courier New", 16, 'bold'))
but2.place(x=317, y=170)

but3 = Button(me, padx=14, pady=14, bd=4, bg='#ed0779', command=lambda: clickbut(3), text="3",
              font=("Courier New", 16, 'bold'))
but3.place(x=317, y=240)

but4 = Button(me, padx=14, pady=14, bd=4, bg='#ed0779', command=lambda: clickbut(4), text="4",
              font=("Courier New", 16, 'bold'))
but4.place(x=382, y=100)

but5 = Button(me, padx=14, pady=14, bd=4, bg='#ed0779', command=lambda: clickbut(5), text="5",
              font=("Courier New", 16, 'bold'))
but5.place(x=382, y=170)

but6 = Button(me, padx=14, pady=14, bd=4, bg='#ed0779', command=lambda: clickbut(6), text="6",
              font=("Courier New", 16, 'bold'))
but6.place(x=382, y=240)

but7 = Button(me, padx=14, pady=14, bd=4, bg='#ed0779', command=lambda: clickbut(7), text="7",
              font=("Courier New", 16, 'bold'))
but7.place(x=447, y=100)

but8 = Button(me, padx=14, pady=14, bd=4, bg='#ed0779', command=lambda: clickbut(8), text="8",
              font=("Courier New", 16, 'bold'))
but8.place(x=447, y=170)

but9 = Button(me, padx=14, pady=14, bd=4, bg='#ed0779', command=lambda: clickbut(9), text="9",
              font=("Courier New", 16, 'bold'))
but9.place(x=447, y=240)

but0 = Button(me, padx=14, pady=14, bd=4, bg='#ed0779', command=lambda: clickbut(0), text="0",
              font=("Courier New", 16, 'bold'))
but0.place(x=317, y=310)

butclear = Button(me, padx=14, pady=14, bd=4, bg='#ef602c', text="DELETE", command=clrbut, font=("Courier New", 16, 'bold'))
butclear.place(x=382, y=310)

name = Button(me, padx=80, pady=14, bd=4, bg='#f7ef8a', command=name, text="name", font=("Courier New", 16, 'bold'))
name.place(x=10, y=385)

electron = Button(me, padx=80, pady=14, bd=4, bg='#f7ef8a', command=electron, text="electron", font=("Courier New", 16, 'bold'))
electron.place(x=257, y=385)

subshell = Button(me, padx=80, pady=14, bd=4, bg='#f7ef8a', command=subshell, text="subshell", font=("Courier New", 16, 'bold'))
subshell.place(x=554, y=385)
me.mainloop()