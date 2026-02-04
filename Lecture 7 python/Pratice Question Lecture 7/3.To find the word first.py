# WAF to find in which line of the file does the word "learning" occurs first.
# Print-1 if word not found


def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open ("pratice.txt","r")as f:
        while data:
            data = f.readline()
            if (word in data):
                print(line_no," ,This is its line number.")
                return
            line_no += 1

    return  

print(check_for_line())
