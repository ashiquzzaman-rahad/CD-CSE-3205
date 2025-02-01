import re

def fileRead(filePath: str)-> str:
    with open (filePath, 'r') as file:
        arr: str = file.read()
    file.close()
    return arr

def main():
    arr: str = fileRead("finalComDelC.txt")
    tokens: list = re.split(r'[ \n\'\"\(\)\{\}\;\,\;]', arr)
    print(tokens)
    for token in tokens:
        try:
            float(token)
            print(token,1)
        except ValueError:
            pass
    
if __name__ == "__main__":

    main()