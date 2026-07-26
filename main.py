from pdb import main

from scanner import Portscanner

target = input("Target (IP/Domain): ")

start = int(input("start Port: "))
end = int(input("End Port: "))

scanner = Portscanner(target, start, end)

scanner.scan()

if __name__ == "__main__":
    main()