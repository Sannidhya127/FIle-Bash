import os


def note_input(defaultvalue):
    # Create a textfile
    txtfile = open("txtfile.txt", "w")
    #
    # populate it with the default value
    txtfile.write(defaultvalue)
    txtfile.close()
    #
    # call Notepad
    os.system("notepad.exe txtfile.txt")
    # input("Just holding until notepad is close : ") (did not need this line)
    # get the Value Entered/Changed in Notepad
    txtfile = open("txtfile.txt", "r")
    func_value = txtfile.read()
    txtfile.close()
    return func_value
    # END DEF


note_input("Name")
