from profanity_filter import ProfanityFilter

pf = ProfanityFilter()

def crossCheck(raw_para):
    for index, letter in enumerate(raw_para):
        if letter == '@':
            raw_para = raw_para[:index] + 'a' + raw_para[index+1:]
        if letter == '$':
            raw_para = raw_para[:index] + 's' + raw_para[index+1:]
        if letter == '#':
            raw_para = raw_para[:index] + 'h' + raw_para[index+1:]
        if letter == '!':
            raw_para = raw_para[:index] + 'i' + raw_para[index+1:]
        if letter == '*':
            raw_para = raw_para[:index] + 'i' + raw_para[index+1:]
        if letter == '5':
            raw_para = raw_para[:index] + 's' + raw_para[index+1:]
    return raw_para

def isProfane(raw_para):
    para = pf.censor(raw_para)
    if para != raw_para:
        return True
    else:
        para = pf.censor(crossCheck(raw_para))
        if para == raw_para:
            return False
        else:
            return True

if __name__ == "__main__":
    raw_para = input('Type a message: ')
    if isProfane(raw_para):
        print("Warning!... Profanity Detected!...")
