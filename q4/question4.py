def fac(n) :
    if n <= 1:
        return n
    else:
        return n * fac(n - 1)

def main() :
    for i in range (0, 15, 2):
        print(str(i) + "! = " + str(fac(i)))

if __name__ == '__main__':
    main()