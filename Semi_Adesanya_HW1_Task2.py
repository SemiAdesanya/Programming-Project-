# Task 2: Simulate a back, forward, visit and quit feature(s) of a standard web browser
# using two stacks to keep track of the pages visited while going back and forward.
import sys
import io

def browser():
    back = []                              # the pages we can go BACK to
    forward = []                           # the pages we can go FORWARD to
    current = "http://www.google.com/"     # the browser starts on this homepage...it's the default page

    while True:
        try:
            line = input().strip()
        except EOFError:                   # for when the input ends without quiting
            break

        parts = line.split()
        if not parts:                     # To check for blank lines
            print("Error: empty command")
            continue

        command = parts[0]

        

        if command == "QUIT":
            break

        elif command == "VISIT":
            if len(parts) != 2:    # also for missing url or too many words
                print("Error: VISIT needs only one URL")
                continue
            if len(parts[1]) > 50:
                print("Error: URL is longer than 50 characters")
                continue
            back.append(current)   # old page goes on the back stack
            current = parts[1]     # new page becomes the current page
            forward.clear()        # visiting something new erases the forward history as shown in the sample
            print(current)

        elif command == "BACK":
            if not back:
                print("Ignored")
            else:
                forward.append(current)
                current = back.pop()
                print(current)
                
        elif command == "FORWARD":
            if not forward:
                print("Ignored")
            else:
                back.append(current)
                current = forward.pop()
                print(current)

        else:
            print("Error: Invalid command '" + command + "'") # for misspelled or unknown commands

        

        


# ---------- Driver code ----------
if __name__ == "__main__":
    print("Type commands (VISIT <url>, BACK, FORWARD, QUIT):")

    sample_input = """
    VISIT http://www.gmail.com/
    VISIT http://www.facebook.com/
    BACK
    BACK
    BACK
    FORWARD
    VISIT http://acm.sgu.ru/
    BACK
    BACK
    FORWARD
    FORWARD
    FORWARD
    VISIT http://www.facebook.com/
    FORWARD
    VISIT http://www.facebook.com/ http://www.facebook.com/
    VISIT http://www.abcdefghijklmmnopqrstuvwxyzabcdefghiklmnopqrstuvwxyzabcdefghijklmnop.com/
    BAK
    
    QUIT
    """
     # to make input() read from the sample input instead of the keyboard
    sys.stdin = io.StringIO(sample_input.strip())
    browser()
    
