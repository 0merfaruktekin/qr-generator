from capacity import QR_CAPACITY
def smallest_version(data,en_mode,er_mode):
    character_num=len(data)
    for i in range(40):
        if QR_CAPACITY[i][er_mode][en_mode]>=character_num:
            return i+1
    print("Hata")

def count_indicator(data_len:int,version:int,en_mode:int):
    raw=bin(data_len)[2::1]
    if version in range(1,10):
        match en_mode:
            case 0:  #Numeric Mode
                length=10
                return "0"*(length-len(raw))+raw
            case 1: #Alphanumeric Mode
                length=9
                return "0"*(length-len(raw))+raw
            case 2: #Byte Mode
                length=8
                return "0"*(length-len(raw))+raw
            case 3: #Kanji Mode
                length=8
                return "0"*(length-len(raw))+raw
    elif version in range(10,27):
        match en_mode:
            case 0:
                length=12
                return "0"*(length-len(raw))+raw
            case 1:
                length=11
                return "0"*(length-len(raw))+raw
            case 2:
                length=16
                return "0"*(length-len(raw))+raw
            case 3:
                length=10
                return "0"*(length-len(raw))+raw
    elif version in range(27,41):
        match en_mode:
            case 0:
                length=14
                return "0"*(length-len(raw))+raw
            case 1:
                length=13
                return "0"*(length-len(raw))+raw
            case 2:
                length=16
                return "0"*(length-len(raw))+raw
            case 3:
                length=12
                return "0"*(length-len(raw))+raw
    return 0

def numeric_encoding(data):
    length=len(data)
    groups=[]
    converted=[]
    output=""
    for i in range(0,length,3):
        try:
            groups.append(data[i:i+3])
        except:
            groups.append(data[i::1])
    for item in groups:
        if len(item)==3 and item[0]!=0:
            temp=bin(int(item))[2::1]
            converted.append("0"*(10-len(temp))+temp)
        elif len(item)==2 and item[0]!=0:
            temp=bin(item)[2::1]
            converted.append("0"*(7-len(temp))+temp)
        elif len(item)==1 and item[0]!=0:
            temp=bin(int(item))[2::1]
            converted.append("0"*(4-len(temp))+temp)
        else:
            temp=bin(int(item))
            index=temp.find("0")
            if index==0:
                temp=bin(item)[7::1]
                converted.append("0"*(7-len(temp))+temp)
            else:
                temp=bin(int(item))[7::1]
                converted.append("0"*(4-len(temp))+temp)

    for a in converted:
        output+=a
        
    return output


def encode_data(data,en_mode,er_mode):
    data_len=len(data)
    version=smallest_version(data,en_mode,er_mode)
    char_count_indicator=count_indicator(data_len,version,en_mode)
    match en_mode:
        case 0:
            encoded=numeric_encoding(data)
    return 0
a=smallest_version("Hello Worlda",1,"L")
print(numeric_encoding("8675309"))
