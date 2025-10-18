from colorama import init, Fore, Style
init()

#This line was added to commit this file

class ConsoleHandler():
    def __init__(self):
        self.self = self
        self.commandList = ["q", "conf"]

    def execute(self, command, args):
        if command == "q":
            exit()
        elif command == "conf":
            if args[0] == "-all":
                print("showing everything..")
            elif args[0] == "-transmitter":
                print("showing transmitter...")
            elif args[0] == "-recievier":
                print("showing recievier...")
            elif args[0] == "-protocol":
                print("showing protocol...")
            else:
                print(Fore.RED + "Error: not autorized argument\n" + str(command) + " " + str(args[0]) + "<- HERE" + Style.RESET_ALL)

    def checkCommand(self, l):
        line = l.split(" ")

        command = line[0]
        args = line[1:]

        for i in range(len(self.commandList)):
            if command == self.commandList[i]:
                self.execute(command, args)
            elif len(self.commandList)-1 == i:
                print(Fore.RED + "Error: command not founded\n" + str(command) + "<-HERE" + Style.RESET_ALL)

console = ConsoleHandler()

while True:
    console.checkCommand(input())