# comment(remark)
# name = "Vivek"
# i = 0
# exit()


class Interpreter:
    def __init__(self):
        self.variables = dict()
        self.is_running = True

    def execute(self, line):
        split_line = line.split()

        if len(split_line) > 0 and split_line[0] == '#':
            return
        if len(split_line) > 2 and split_line[1] == '=':
            self.variables[split_line[0]] = split_line[2]
        if len(split_line) > 0 and split_line[0] == 'exit()':
            self.is_running = False

        print("Line: ", line)
        print("Variable: ", self.variables)     # changing,volatile,Variable


def main():
    interpreter = Interpreter()

    print("Hello!")

    while interpreter.is_running:
        x = input('>>> ')
        interpreter.execute(x)


main()
