import re
from .constants import VALUE_REGEX

intent = 0



def to_xml(obj):
    if type(obj) == tuple:
        serialized = []
        for el in obj:
            global intent
            intent += 1
            isType = False
            if type(el) == tuple:
                isType = True
                serialized.append(
                    f"\n"
                    + ((intent - 1) * "\t")
                    + f"<{type(el).__name__}>"
                    + (isType * intent * "\t")
                    + f"{to_xml(el)}"
                    + (isType * '\n')
                    + (isType * (intent - 1) * "\t")
                    + f"</{type(el).__name__}> "
                )
            else:
                serialized.append(
                    f"\n"
                    + ((intent - 1) * "\t")
                    + f"<str>"
                    + (isType * intent * "\t")
                    + f"{to_xml(el)}"
                    + (isType * '\n')
                    + (isType * (intent - 1) * "\t")
                    + f"</str> "
                )
            intent -= 1
        res = "".join(serialized)
        return f"{res}"
    else:
        return f"{str(obj)}"

string_count = 0
depth = 0

# def from_xml(data: list[str]):

#     if len(data) == 0 or data[1] == "<tuple/>":
#         return tuple()
#     result = []
#     temp_tuple = []
#     global depth, string_count
#     result.append(from_xml_utility(data))
#     return tuple(result)    

def from_xml(data: str):
    if data == '<tuple></tuple>':
        return tuple()
    elif data[:7] == '<tuple>':
        data = data[7:-9]
        if data[-1] == ' ':
            data = data[:-1]

        parsed = []
        depth = 0
        substr = ""
        for i in data:
            if i == '<' or i == '>':
                depth += 1
            elif i == '/':
                depth -= 4
            elif depth == 0:
                parsed.append(from_xml(substr))
                substr = ""
                continue

            substr += i
        parsed.append(from_xml(substr))
        return tuple(parsed)
    
    elif data[:5] == '<str>':
        parsed = []
        ind = data.find('</str>')
        if data[ind + 6:] != "":
            parsed.append(from_xml(data[5:ind]))
            parsed.append(from_xml(data[ind + 6:]))
        else:
            return data[5:ind]
        return tuple(parsed)
    else:
        return data





    # if len(data) == 0 or data[1] == "<tuple/>":
    #     return tuple()
    # if "<tuple>" in data[0]:
    #     data = data[1:len(data) - 1]
    #     result = []
    #     depth = 0
    #     sublist = []
    #     temp_tuple = []
    #     quote = False

    #     for string in data:
    #         if "<tuple>" in string:
    #             depth += 1
    #         elif "<tuple/>" in string:
    #             depth -= 1
    #         elif "TYPE" in string or "VALUE" in string:
    #             temp_tuple.append(re.search(VALUE_REGEX, string).group(1))
    #         elif len(temp_tuple) > 0 and (temp_tuple[0] == 'TYPE' or temp_tuple[0] == 'VALUE') and depth == 0:
    #             temp_tuple.append(re.search(VALUE_REGEX, string).group(1))
    #             if len(temp_tuple) == 2:
    #                 result.append(tuple(temp_tuple))
    #                 temp_tuple.clear()
    #             sublist = []
    #             continue
    #         # sublist.append(string)
        
    #     # result.append(from_xml_utility(sublist))
    #     return tuple(result)
    # else:
    #     return data[1:len(data) - 1]

    # while True:
    #     string_count += 1
    #     if "<tuple/>" in data[i]:
    #         break
    #     if "<tuple>" in data[i]:
    #         res, counter = from_xml_utility(data[string_count:len(data) - string_count])
    #         temp_tuple.append(res)
    #     else:
    #         value = re.search(VALUE_REGEX, data[i]).group(1)
    #         temp_tuple.append(value)
    #     if (counter != 0):
    #         i += counter - 1
    #     else:
    #         i += 1
    # return tuple(temp_tuple), i

        
    # result = []
    # temp_tuple = []
    # global string_count, depth
    # data = data[string_count:len(data) - string_count]
    # for string in data:
    #     string_count += 1
    #     if "<tuple>" in string:
    #         depth += 1
    #     if not "<tuple>" in string and not "<tuple/>" in string:
    #         if depth > 1:
    #             temp_tuple.append(from_xml(data[string_count:len(data) - string_count]))
    #             continue
    #         value_str = re.search(VALUE_REGEX, string).group(1)
    #         temp_tuple.append(value_str)
    #     elif "<tuple/>" in string:
    #         depth -= 1
    #         if len(temp_tuple) != 0:
    #             result.append(tuple(temp_tuple))
    #             temp_tuple.clear()
    # if len(temp_tuple) != 0:
    #     result.append(tuple(temp_tuple))
    # return tuple(result)

