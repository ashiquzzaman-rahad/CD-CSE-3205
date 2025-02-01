import re

def fileRead(filePath: str)-> str:
    with open (filePath, 'r') as file:
        arr: str = file.read()
    file.close()
    return arr

def fileWrite(filePath: str, tokens: list)-> None:
    with open (filePath, 'w+') as file:
        for token in tokens:
            file.write(token)
    file.close()

def commentDel(code: str) -> list:
    code_new: list = []
    comment_begin: int = -1
    comment_end: int = -1

    for i in range(len(code)):
        if code[i] == '/' and code[i+1] == '/':
            j: int = i
            length: int = 0
            comment_begin = i
            j += 1
            while code[j] != "\n":
                j += 1
                length += 1
            comment_end = comment_begin + length
        if i <= comment_end:
            continue
        else:
            code_new.append(code[i]) 
    return code_new

def multiCommentDel(code: str) -> list:
    code_new: list = []
    start: int = -1
    length: int = 0
    turn: bool = True

    for i in range(len(code)):
        if turn:
            if (code[i] == "/" and code[i+1] == "*"):
                start = i+3
                j: int = start
                length = 3
                while (j < len(code)-1):
                    if code[j] == '*' and code[j+1] == "/":
                        break
                    else:
                        length += 1
                        j += 1
                length += 3
                turn = False
        if length == 0:
            turn = True
            code_new.append(code[i])
        else:
            length -= 1
            
    return code_new  

def keywordFind(tokens: list, keyWords: list) -> list:
    keywordFound: list = []
    skip: int = -1
    for i in range(len(tokens)):
        if i <= skip:
            continue
        if tokens[i] in keyWords:
            if tokens[i] == 'else' and tokens[i+1] == 'if':
                skip = i + 1
                keywordFound.append('else if')
            else:
                keywordFound.append(tokens[i])

    return keywordFound

def symbolFind(arr: str, symbol_dict: dict) -> list: 
    symbolList: list = []
    arr_len: int = len(arr)
    temp: int = -1

    for i in range(arr_len):
        if i == temp:
            continue

        if(arr[i] == '=' and arr[i+1] == '='):
            symbolList.append('==')
            temp = i + 1
        elif(arr[i] == '+' and arr[i+1] == '='):
            symbolList.append('+=')
            temp = i + 1
        elif(arr[i] == '+' and arr[i+1] == '+'):
            symbolList.append('++')
            temp = i + 1
        else:
            for key in symbol_dict.keys():
                if(key == arr[i]):
                    symbolList.append(arr[i])
        
    return symbolList

def variableFind() ->dict:
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
                    # print(variable)
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
                # print(variable)
                dict_new = {variable : "int"}
                variables.update(dict_new)
                j += 1

        if tokens[i] == 'float':
            j = i + 1
            while not(';' in tokens[j]):
                if (tokens[j] >= 'a' and tokens[j] <= 'z') or (tokens[j] >= 'A' and tokens[j] <= 'Z') or tokens[j] == '_':
                    variable = tokens[j]
                    # print(variable)
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
                # print(variable)
                dict_new = {variable : "float"}
                variables.update(dict_new)
                j += 1

        if tokens[i] == 'bool':
            j = i + 1
            while not(';' in tokens[j]):
                if (tokens[j] >= 'a' and tokens[j] <= 'z') or (tokens[j] >= 'A' and tokens[j] <= 'Z') or tokens[j] == '_':
                    if(tokens[j] != 'true' and tokens[j] != 'false'):
                        variable = tokens[j]
                        # print(variable)
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
                # print(variable)
                dict_new = {variable : "bool"}
                variables.update(dict_new)
                j += 1

        if tokens[i] == 'char':
            j = i + 1
            while not(';' in tokens[j]):
                if (tokens[j] >= 'a' and tokens[j] <= 'z') or (tokens[j] >= 'A' and tokens[j] <= 'Z') or tokens[j] == '_':
                    variable = tokens[j]
                    # print(variable)
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
                # print(variable)
                dict_new = {variable : "char"}
                variables.update(dict_new)
                j += 1

    return variables


def numericFind() -> list:
    numerics: list = []
    typeNums: list = []
    arr: str = fileRead("finalComDelC.txt")
    tokens: list = re.split(r'[ \n\'\"\(\)\{\}\;\,\;]', arr)
    print(tokens)
    for token in tokens:
        try:
            float(token)
            typeNum: str = ''
            if(token.isnumeric()):
                typeNum = 'Integer Number'
            else:
                typeNum = 'Real Number'
            numerics.append(token)
            typeNums.append(typeNum)

        except ValueError:
            pass
    
    return numerics, typeNums

def main():
    code: str = fileRead("codeC.txt")
    code_new:list = commentDel(code)
    fileWrite("comDelC.txt",code_new)
    new_code: str = fileRead("comDelC.txt")
    code_new = multiCommentDel(new_code)
    fileWrite("finalComDelC.txt",code_new)
    arr: str = fileRead("finalComDelC.txt")
    tokens: list = re.split(r'[ \n\'\"\(\)\{\}\;\,]', arr)
    keyWords: list = ['if', 'else', 'for', 'int', 'float', 'char', 'bool', 'return', 'const']
    # print(tokens)

    symbol_dict: dict = {
                            '#' : 'Hash',
                            '<' : 'Less than',
                            '<' : 'Greater than',
                            '.' : 'Dot',
                            ',' : 'Comma',
                            '(' : 'Opening parenthesis',
                            ')' : 'Closing parenthesis',
                            '{' : "Opening Braces",
                            '}' : "Closing Braces",
                            "'" : "Inveted comma",
                            ";" : "Semicolon",
                            "=" : "Assignment",
                            "==" : "Equal",
                            "+" : "Addition",
                            "-" : "Subtraction",
                            "*" : "Multiplication",
                            "/" : "Division",
                            "+=" : 'Addition assignment',
                            "++" : 'Increment'
                        }

    symbols: list = symbolFind(arr, symbol_dict)
    print(symbols)
    code_new.append('\nKeywords\n')
    keyWord_found: list = keywordFind(tokens, keyWords)
    print(keyWord_found)
    for keyword in keyWord_found:
        code_new.append(keyword + '\n')

    code_new.append("\nSymbols \n")
    for symbol in symbols:
        for s in symbol_dict.keys():
            if symbol == s:
                names = f"{s} ----- {symbol_dict[s]}\n"
                code_new.append(names)

    code_new.append("\nVariables\n")
    variables: dict = variableFind()
    for k, v in variables.items():
        names = f"{k} ---- {v}\n"
        code_new.append(names)
    print(variables)

    code_new.append("\n\t\t\t\t\tSymbol Table\n")
    code_new.append('-----------------------------------------------------------------------------\n')
    code_new.append(f"{'Symbol':20}|{'Token':20}|{'Data type':20}|{'Pointer to Symbol Table Entry':50}\n")
    code_new.append('-----------------------------------------------------------------------------\n')
    pointer: int = 1
    for variable in variables.keys():
        if (variable != ''):
            symbol = f"{variable}\t\t|\t\tid\t\t|\t\t{variables[variable]}\t\t\t|\t\t\t\t\t{pointer}\n"
            code_new.append('-----------------------------------------------------------------------------\n')
            code_new.append(symbol)
            pointer += 1
    
    numerics, typeNums = numericFind()
    print(numerics)
    print(typeNums)

    code_new.append("\n\n\t\t\t\t\tTOKENS\n\n")
    code_new.append('-----------------------------------------------------------------------------\n')
    code_new.append("Lexemes\t\t\t|\t\t\tToken Name\t\t\t|\t\t\tAttribute Value\n")
    code_new.append('-----------------------------------------------------------------------------\n')

    for symbol in symbols:
        if symbol == '+' or symbol == '-' or symbol == '*' or symbol == '/' or symbol == '=':
            names = f"{symbol}\t\t\t|\t\t\tOperator\t\t\t|\t\t\t{symbol_dict[symbol]}\n"
        else:
            names = f"{symbol}\t\t\t|\t\t\tSpecial symbol\t\t|\t\t{symbol_dict[symbol]}\n"
        code_new.append(names)
        code_new.append('-----------------------------------------------------------------------------\n')
    
    for keyword in keyWord_found:
        names = f"{keyword}\t\t\t|\t\t\t{keyword}\n"
        code_new.append(names)
        code_new.append('-----------------------------------------------------------------------------\n')

    for variable in variables.keys():
        names = f"{variable}\t\t|\t\t\tid\t\t|\tpointer to symbol table entry\n"
        code_new.append(names)
        code_new.append('-----------------------------------------------------------------------------\n')

    for i in range(len(numerics)):
        names = f"{numerics[i]}\t\t|\t\t{typeNums[i]}\t|\tconstant\n"
        code_new.append(names)
        code_new.append('-----------------------------------------------------------------------------\n')

    fileWrite("finalC.txt", code_new) 

if __name__ == "__main__":
    main()