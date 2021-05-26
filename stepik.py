tree = {}
first_num = None
rq_depth = 0
max_depth = 0
space_indent = 0

def build_tree(x, cur_num, cur_depth=0):
    global tree
    global first_num
    global rq_depth
    global max_depth
    if tree == {}:
        tree[x] = {"left" : None, "right" : None, "lay" : 0}
        first_num = x
        return 0
    else:
        if cur_num == "start":
            cur_num = first_num
            cur_depth = 0
        if int(x) < int(cur_num):
            next_side = "left"
        else:
            next_side = "right"
        if tree[cur_num][next_side] == None:
            tree[cur_num][next_side] = x
            tree[x] = {"left" : None, "right" : None, "lay" : cur_depth+1}
            if cur_depth+1 > max_depth:
                max_depth = cur_depth+1
            return 0
        else:
            next_num = tree[cur_num][next_side]
            next_depth = tree[cur_num]["lay"]+1
            build_tree(x, next_num, next_depth)

def get_input_num():
    while (True):
        input_element = input()
        if input_element.isdigit():
            return input_element
        else:
            print("Введено некорректное значение. Попробуйте снова.")

def search_for_element(x, cur_num):
    global tree
    global first_num
    global max_depth
    global space_indent
    if cur_num == "start":
        cur_num = first_num
        indent = (max_depth+1)*2
        space_indent = ""
        for i in range(0, indent):
            space_indent += " "
        print(space_indent+cur_num)
    if x < cur_num:
        next_side = "left"
    elif x > cur_num:
        next_side = "right"
    else:
        print("Такой элемент есть")
        return 0
    if tree[cur_num][next_side] == None:
        print("Такого элемента в дереве нет")
        return 1
    else:
        next_num = tree[cur_num][next_side]
        if next_side == "left":
            space_indent = space_indent[:-1]
            print(space_indent+"/")
            space_indent = space_indent[:-1]
            print(space_indent + next_num)
        else:
            space_indent += " "
            print(space_indent + "\\")
            space_indent += " "
            print(space_indent + next_num)
        search_for_element(x, next_num)

def lay_decrease(x):
    global tree
    tree[x]["lay"] -= 1
    if tree[x]["right"]!=None:
        lay_decrease(tree[x]["right"])
    if tree[x]["left"]!=None:
        lay_decrease(tree[x]["left"])

def get_nearest_element(x,prev_num = first_num):
    global tree
    if tree[x]["left"]!=None:
        rez = get_nearest_element(tree[x]["left"], x)
        return rez
    else:
        if tree[x]["right"]==None:
            if tree[prev_num]["left"]==x:
                cur_side = "left"
            else:
                cur_side = "right"
            tree[prev_num][cur_side] = None
            return x
        else:
            cur_side = "right"
            if tree[prev_num]["left"] == x:
                tree[prev_num]["left"] = tree[x][cur_side]
            else:
                tree[prev_num]["right"] = tree[x][cur_side]
            return x

def delete_element(x, cur_num = "start", prev_num = None):
    global tree
    global first_num
    global max_depth
    global space_indent
    if cur_num == "start":
        cur_num = first_num
        prev_num = first_num
    if x < cur_num:
        next_side = "left"
    elif x > cur_num:
        next_side = "right"
    else:
        if (tree[x]["right"] == None)and(tree[x]["left"] == None):
            del tree[x]
            if tree[prev_num]["left"] == x:
                tree[prev_num]["left"] = None
            else:
                tree[prev_num]["right"] = None
        elif (tree[x]["right"] == None)or(tree[x]["left"] == None):
            if tree[x]["right"] != None:
                cur_side = "right"
            else:
                cur_side = "left"
            print(prev_num)
            if tree[prev_num]["left"] == x:
                tree[prev_num]["left"] = tree[x][cur_side]
            else:
                tree[prev_num]["right"] = tree[x][cur_side]
            print(tree[x][cur_side])
            lay_decrease(tree[x][cur_side])
            if x == first_num:
                first_num = tree[x][cur_side]
            del tree[x]
        else:
            rezult = get_nearest_element(tree[x]["right"], cur_num)
            if tree[prev_num]["left"] == x:
                cur_side = "left"
            else:
                cur_side = "right"
            tree[prev_num][cur_side] = rezult
            if tree[x]["left"]!=None:
                tree[rezult]["left"] = tree[x]["left"]
            if tree[x]["right"] != None:
                tree[rezult]["right"] = tree[x]["right"]
            tree[rezult]["lay"] = tree[x]["lay"]
            if x == first_num:
                first_num = rezult
            del tree[x]
        return 0
    if tree[cur_num][next_side] == None:
        print("Такого элемента в дереве нет")
        return 1
    else:
        previous_num = cur_num
        next_num = tree[cur_num][next_side]
        delete_element(x, next_num, previous_num)

def add_element(x, cur_num = "start"):
    global tree
    global first_num
    global max_depth
    global space_indent
    if cur_num == "start":
        cur_num = first_num
    if x < cur_num:
        next_side = "left"
    elif x > cur_num:
        next_side = "right"
    else:
        print("Такой элемент есть")
        return 0
    if tree[cur_num][next_side] == None:
        tree[cur_num][next_side] = x
        tree[x] = {"left": None, "right": None, "lay": tree[cur_num]["lay"]+1}
        if tree[x]["lay"] > max_depth:
            max_depth = tree[x]["lay"]
        return 1
    else:
        next_num = tree[cur_num][next_side]
        add_element(x, next_num)

def get_indent_string():
    global rq_depth
    indent_string = ""
    sum = 0
    for i in range(1, rq_depth+1):
        sum += pow(2, i)
    sum += rq_depth
    for i in range(0, sum):
        indent_string += " "
    return indent_string

  # ПРИМЕРЫ ЧИСЛОВЫХ ПОСЛЕДОВАТЕЛЬНОСТЕЙ
  # 9 5 3 1 4 7 6 8
  # 9 5 3 1 4 7 6 8 15 12 10 13 17 16 18

def display_tree():
    global tree
    global first_num
    global max_depth
    global space_indent
    global rq_depth
    print("Максимальная глубина = "+str(max_depth))
    rq_depth = max_depth
    indent = pow(2, rq_depth)
    first_rez = get_indent_string()
    print(first_rez+first_num)
    rq_depth -= 1
    cur_list = list() #пишем текущие элементы строки
    prev_list = list()
    prev_list.append(first_num)
    while(True):
        for i in prev_list:
            if i != None:
                cur_list.append(tree[i]["left"])
                cur_list.append(tree[i]["right"])
            else:
                cur_list.append(None)
                cur_list.append(None)
        prev_list.clear()
        prev_list = cur_list.copy()
        cur_string = get_indent_string()
        pair = 0
        iter = 0
        for i in cur_list:
            if iter != 0:
                if pair == 0:
                    for j in range(0, (indent * 2 - 1)):
                        cur_string += " "
                    pair = 1
                else:
                    for j in range(0, (indent * 2 + 1)):
                        cur_string += " "
                    pair = 0
            else:
                pair = 1
            if i != None:
                cur_string += i
            else:
                cur_string += " "
            iter += 1
        print(cur_string)
        next_indent = int(indent / 2)
        cur_list.clear()
        indent = next_indent
        del cur_string
        if rq_depth != -1:
            rq_depth -= 1
        else:
            break

def main():
    global rq_depth
    print("Введите числовую последовательность. Ввод будет прекращен после введения не числовых значений.")
    input_list = input()+" "
    num = ""
    for cur_num in input_list:
        if cur_num != " ":
            num += cur_num
        elif num != "":
            if num.isdigit():
                build_tree(num, "start")
            num = ""
    while(True):
        print("Выполнить действия с бинарным деревом: ")
        print("1 - Поиск элемента")
        print("2 - Удаление элемента")
        print("3 - Добавление элемента")
        print("4 - Вывести графическое отображение дерева")
        cur_action = input()
        if cur_action == "1":
            print("Введите искомый элемент")
            searching_element = get_input_num()
            search_for_element(searching_element, "start")
        elif cur_action == "2":
            print("Введите элемент для удаления")
            deleting_element = get_input_num()
            delete_element(deleting_element)
            display_tree()
        elif cur_action == "3":
            print("Введите элемент для добавления")
            additing_element = get_input_num()
            add_element(additing_element)
            display_tree()
        elif cur_action == "4":
            display_tree()
        else:
            print("Введено неккоректное значение")

main()