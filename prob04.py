def main():
    times = int(input("How many times? "))
    for i in range(times):
        a = input("Miles traveled? ")
        b= input("Minutes elapsed? ")
        b = float(b)/60
        c = float(a)/float(b)
        print (c)


main()
