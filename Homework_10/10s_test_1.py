import telebot  # https://t.me/education_simple_calc_bot

bot = telebot.TeleBot("---------", parse_mode=None)

global max_pow
max_pow = []


@bot.message_handler(commands=['start'])
def send_welcome(message):

    bot.reply_to(message, "Отправьте полиномы, которые хотите сложить, с разделителем <<,>>. Например: 5*x^3 + 98*x^2 + 54*x + 4 = 0, 8*x^5 + 86*x^4 + 57*x^3 + 73*x^2 + 43*x + 16 = 0")


@bot.message_handler(func=lambda m: True)
def polinom_adding(message):

    str = message.text
    polinoms = str.split(",")
    res1 = str_polynom_to_tuple(polinoms[0])
    res2 = str_polynom_to_tuple(polinoms[1])
    answer = adding_polynoms(res1, res2)
    bot.reply_to(message, answer)


# раскладываем строку с полиномом в массив кортежей, где первое значение, второе степень
def str_polynom_to_tuple(polynom):
    global max_pow
    lst = []
    polynom = polynom.replace("*", "").replace("^", "").replace("=0", "").replace("= 0", "").replace("-", "+-")
    polynom = "".join(polynom.split())
    polynom = polynom.split("+")    
    for i in range(len(polynom)):
        if "x" in polynom[i]:
            cort = polynom[i].split("x")
            if cort[1] == "":
                cort[1] = "1"
            if int(cort[1]) not in max_pow:
                max_pow.append(int(cort[1]))
        else:
            cort = (polynom[i], "0")
            max_pow.append(0)
        if not cort[0] == '':
            lst.append(tuple(cort))
        lst.sort(key=lambda x: x[1])
        result = tuple(map(lambda x: (int(x[0]), int(x[1])), lst))
    max_pow = list(set(max_pow))
    return result


def adding_polynoms(polynom_1, polynom_2):
    global max_pow
    lst3 = []
    answ = ""
    for i in max_pow:  # складываем значения членов с одинаковыми степенями
        t_lst = ([x[0] for x in polynom_1 if x[1] == i] + [x[0] for x in polynom_2 if x[1] == i])        
        if len(t_lst) == 2:
            lst3.append(t_lst[0] + t_lst[1])
        elif len(t_lst) == 0:
            continue
        else:
            lst3.append(t_lst[0])
    for i in reversed(max_pow):  # собираем в строку вычисленный полином
        j = max_pow.index(i)
        match(i):
            case 0:
                if lst3[j] < 0:
                    answ += "- " + str(abs(lst3[j]))
                else:
                    answ += str(lst3[j])
            case 1:
                if lst3[j] < 0:
                    answ += "- " + str(abs(lst3[j])) + "*x" + " + "
                else:
                    answ += str(lst3[i]) + "*x" + " + "
            case default:
                if lst3[j] < 0:
                    answ += "- " + str(abs(lst3[j])) + "*x^" + str(i) + " + "
                else:
                    answ += str(lst3[j]) + "*x^" + str(i) + " + "
    answ += " = 0"
    answ = answ.replace(" + - ", " - ")
    max_pow = []
    return answ

bot.infinity_polling()
