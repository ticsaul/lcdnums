INPUT_NUM = 'Write your number: '
ERROR = 'I\'m sorry, your number is not defined.'
LCD_NUMBERS = {
    0: [' _ ', '| |', '|_|'],
    1: ['   ', ' | ', ' | '],
    2: [' _ ', ' _|', '|_ '],
    3: [' _ ', ' _|', ' _|'],
    4: ['   ', '|_|', '  |'],
    5: [' _ ', '|_ ', ' _|'],
    6: [' _ ', '|_ ', '|_|'],
    7: ['__ ', '  |', '  |'],
    8: [' _ ', '|_|', '|_|'],
    9: [' _ ', '|_|', ' _|']
}

lines = 3
def drawLcdNumber(number):
    for line in range(0, lines):
        lineDrawed = ''
        for digit in number:
            lineDrawed += LCD_NUMBERS[ int(digit) ][line] + ' '
        print(lineDrawed)

inputNum = input(INPUT_NUM)
while inputNum != '':
    try:
        drawLcdNumber(inputNum)
        inputNum = input(INPUT_NUM)
    except KeyError:
        inputNum = ''
        print(ERROR)
    except ValueError:
        inputNum = ''
        print(ERROR)
