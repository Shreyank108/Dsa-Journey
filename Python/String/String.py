s="a4c5d6" 
output= "aaaacccccdddddd" 
i=0 
result = "" 
while i <len(s): 
    char= s[i] 
    i+=1  
    string_num =""
    while i<len(s) and s[i].isdigit() : 
        string_num+=s[i] 
        i+=1   
    converting_to_num= int(string_num)  
    result+=char*converting_to_num   
print(result) 
if result == output: 
    print("Result Matches") 
else : 
    print("Not Matched")