import re

def fileRead(filePath: str)-> str:
    with open (filePath, 'r') as file:
        arr: str = file.read()
    file.close()
    return arr

def main():
    variable: str = ''
    variables: dict = {}
    arr: str = fileRead("finalComDelC.txt")
    tokens: list = re.split(r'[ \n\(\)\{\}\,]', arr)
    # print(tokens)
    len_token: int = len(tokens)
    main_code_index: int = 0
    for i in range(len_token):
        if tokens[i] == 'main':
            main_code_index = i + 1
            break
    j: int = 0
    for i in range(main_code_index, len_token):
        # print(tokens[i])
        if i <= j:
            continue
        if tokens[i] == 'int':
            j = i + 1
            while not(';' in tokens[j]):
                if (tokens[j] >= 'a' and tokens[j] <= 'z') or (tokens[j] >= 'A' and tokens[j] <= 'Z') or tokens[j] == '_':
                    variable = tokens[j]
                    print(variable)
                    dict_new = {variable : "int"}
                    variables.update(dict_new)
                j += 1
            if(tokens[j] >= 'a' and tokens[j] <= 'z') or (tokens[j] >= 'A' and tokens[j] <= 'Z') or tokens[j] == '_':
                variable = tokens[j]
                temp = ""
                if variable[len(variable) - 1] == ';' or variable[len(variable) - 1] == ',':
                    for l in range(len(variable) - 1):
                        temp += variable[l]
                    variable = temp
                    temp = ''
                print(variable)
                dict_new = {variable : "int"}
                variables.update(dict_new)
                j += 1

        if tokens[i] == 'float':
            j = i + 1
            while not(';' in tokens[j]):
                if (tokens[j] >= 'a' and tokens[j] <= 'z') or (tokens[j] >= 'A' and tokens[j] <= 'Z') or tokens[j] == '_':
                    variable = tokens[j]
                    print(variable)
                    dict_new = {variable : "float"}
                    variables.update(dict_new)
                j += 1
            if(tokens[j] >= 'a' and tokens[j] <= 'z') or (tokens[j] >= 'A' and tokens[j] <= 'Z') or tokens[j] == '_':
                variable = tokens[j]
                temp = ""
                if variable[len(variable) - 1] == ';' or variable[len(variable) - 1] == ',':
                    for l in range(len(variable) - 1):
                        temp += variable[l]
                    variable = temp
                    temp = ''
                print(variable)
                dict_new = {variable : "float"}
                variables.update(dict_new)
                j += 1

        if tokens[i] == 'bool':
            j = i + 1
            while not(';' in tokens[j]):
                if (tokens[j] >= 'a' and tokens[j] <= 'z') or (tokens[j] >= 'A' and tokens[j] <= 'Z') or tokens[j] == '_':
                    if(tokens[j] != 'true' and tokens[j] != 'false'):
                        variable = tokens[j]
                        print(variable)
                        dict_new = {variable : "bool"}
                        variables.update(dict_new)
                j += 1
            if(tokens[j] >= 'a' and tokens[j] <= 'z') or (tokens[j] >= 'A' and tokens[j] <= 'Z') or tokens[j] == '_':
                if(tokens[j] != 'true' and tokens[j] != 'false' and tokens[j] != 'true;' and tokens[j] != 'false;'):
                    variable = tokens[j]
                    temp = ""
                if variable[len(variable) - 1] == ';' or variable[len(variable) - 1] == ',':
                    for l in range(len(variable) - 1):
                        temp += variable[l]
                    variable = temp
                    temp = ''
                print(variable)
                dict_new = {variable : "bool"}
                variables.update(dict_new)
                j += 1

        if tokens[i] == 'char':
            j = i + 1
            while not(';' in tokens[j]):
                if (tokens[j] >= 'a' and tokens[j] <= 'z') or (tokens[j] >= 'A' and tokens[j] <= 'Z') or tokens[j] == '_':
                    variable = tokens[j]
                    print(variable)
                    dict_new = {variable : "char"}
                    variables.update(dict_new)
                j += 1
            if(tokens[j] >= 'a' and tokens[j] <= 'z') or (tokens[j] >= 'A' and tokens[j] <= 'Z') or tokens[j] == '_':
                variable = tokens[j]
                temp = ""
                if variable[len(variable) - 1] == ';' or variable[len(variable) - 1] == ',':
                    for l in range(len(variable) - 1):
                        temp += variable[l]
                    variable = temp
                    temp = ''
                print(variable)
                dict_new = {variable : "char"}
                variables.update(dict_new)
                j += 1

    print(variables)
            # variable = ""

        
                
                

if __name__ == "__main__":
    main()