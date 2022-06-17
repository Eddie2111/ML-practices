def opration(string):
    result = '';
    for i in range(len(string)):
        if string[i] == ',':
            temp_val1 = string[0:i].replace(" ", "");
            temp_val2 = string[i+1:len(string)].replace(" ", "");
    if len(temp_val1)==len(temp_val2):        
        for i in range (len(temp_val1)):
            result += temp_val1[i]+temp_val2[i];
    if len(temp_val1)>len(temp_val2):
        for i in range (len(temp_val2)):
            result += temp_val1[i]+temp_val2[i];
        result += temp_val1[len(temp_val2):len(temp_val1)];
    if len(temp_val1)<len(temp_val2):
        for i in range (len(temp_val1)):
            result += temp_val1[i]+temp_val2[i];
        result += temp_val2[len(temp_val1):len(temp_val2)];    
    return result;

if __name__ == "__main__":
    string = input("Enter your string: ");        
    print(opration(string));
