# by bidouille

def bencode(x):
    def ben(x):
        if type(x) == int:
            return f"i{x}e"            
            
        if type(x) == str:
            return f"{len(x)}:{x}"            
        
        if type(x) == list:
            new_list = [ben(i) for i in x]
            return f"l{''.join(new_list)}e"            
            
        if type(x) == dict:  
            new_dict_list = []
            for i in list(sorted(x.items())): 
                new_dict_list.append(f"{ben(i[0])}")
                new_dict_list.append(ben(i[1]))                     
            return f"d{''.join(new_dict_list)}e"      
    return bytes(ben(x), 'utf-8')
    
def bdecode(x):    
    x = x.decode('utf-8')    
    def bde(x, rest=0):
        y = x
        if y[0].isdigit():
            length = ""
            for i in y:
                if i != ":":
                    length += i    
                else:
                    y = y[len(length)+1:]
                    break
            s = y[0:int(length)]   
            rest = y[int(length):]                               
            return (s, rest)  

        if y[0] == "i":                        
            num = ""
            for i in y[1:]:
                if i.isdigit():
                    num += i
                else:
                    rest = y[len(num)+2:]          
                    break
            return (int(num), rest)
                
        if y[0] == "l":   
            new_list = []  
            y = y[1:]    
            while y: 
                vars = [i for i in bde(y)]
                if vars[0] == None:
                    return (new_list, vars[1])     
                new_list.append(vars[0]) 
                y = vars[1]               
            return new_list

        if y[0] == "d":
            new_dict = {}
            y = y[1:]
            while y:
                vars = [i for i in bde(y)]
                if vars[0] == None:
                    return (new_dict, vars[1])  
                new_dict[vars[0]] = bde(vars[1])[0]
                y = bde(vars[1])[1]        

        if y[0] == "e":            
            rest = y[1:]
            return (None, rest)  

    return bde(x)[0]
    
    
# txt = 'd1:ad2:id20:01234567890897653412e1:q4:ping1:t2:aa1:y1:qe'
# A = [int(s) for s in txt.split(":") if s.isdigit()]
# print(txt.split())
# print(A)
    
# print(bdecode(b'14:spamFOObar1234nadmiartaki'))
# print()
# print(bdecode(b'l4:spami42ee'))
# print()
# print(bdecode(b'i42eNADMIAR'))
# print()
# print(bdecode(b'd1:ad2:id20:01234567890897653412e1:q4:ping1:t2:aa1:y1:qe'))
# print(bdecode(b'li123e5:napisi456e5:czescl6:lista1i1337eee'))
# print(bdecode(b'd3:bar4:spam3:fooi42ee'))
print(bdecode(b'd3:bah4:pouf3:zool3:pood2:fo2:faeee'))

# {"bah": "pouf", "zoo": ["poo", {"fo":"fa"}]}

# print(bencode('spamFOObar1234'))
# print(bencode(42))
# print(bencode(['spam', 42]))
# print(bencode({"bar": "spam", "foo": 42}))
# print(bencode({'a': 'boo'}))
# print(bencode({'t': 'aa', 'y': 'q', 'q': 'ping', 'a': {'id': '01234567890897653412'}}))
# print(bencode([123, "napis", 456, "cześć", ["lista1", 1337]]))
