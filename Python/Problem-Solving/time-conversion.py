if __name__ == '__main__':
    s = input()
    time= s[8:]

    if time == "AM":
        # return s[0:8]
        print("ss")
    elif time == "PM":
        # return (int(s[0:2])+12) + s[2:]
        print(str((int(s[0:2])+12)) + s[2:8])
        print("malem")