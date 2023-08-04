'''
Function to convert the string included with number will
multipled of the suffix string.
'''
def string_format(input_string: str) -> str:

    '''
    If the last character of the string is numeric,
    then the input is invalid (not a valid string)
    Example: "12adbchr1rtry5"
    '''
    if len(input_string) < 1 or input_string.isnumeric():
        return f"{input_string} is not a valid input"
    
    '''
    If the 1st character of the string is not numeric, then
    will consider the 1st character of the string as '1'.
    Example - Input: "aaa2bcd"
    Expected Output: "aaabcdbcd"

    string_list: It used to prepare the string till the next numeric character found.
    '''
    if input_string[0].isalpha():
        string_list = [1]
    else:
        string_list = []

    '''
    Output_string: Contains the expected output of the input string
    '''
    output_string = ""

    '''
    Iterate of the input string and strore the numeric number with suffix string.
    and finally updated the output string with each iteration.
    '''
    for i in input_string:
        if i.isnumeric():
            if string_list:
                if len(string_list) > 1:
                    output_string += string_list[0] * string_list[1]
                    string_list = []
                    string_list.append(int(i))
                elif type(string_list[0]) == int:
                    string_list[0] = (string_list[0] * 10) + int(i)
            else:
                string_list.append(int(i))
        elif i.isalpha():
            if len(string_list) > 1:
                string_list[1] += i
            else:
                string_list.append(i)

    if len(string_list) > 1:
        output_string += string_list[0] * string_list[1]
    return output_string

# Take the user input of string from user
input_string: str = input("Enter a string which contains numeric value ::: ")

# Call the string_format function and print the output
print(string_format(input_string))