datalist = []
cont = "true"

while cont == "true":
    datalist.append(float(input("> ")))
    datalist.sort()
    print("MIN: ", datalist[0], "MAX: ", datalist[-1])
