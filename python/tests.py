stri=str(input("Введите строку, состоящую из 0 и 1. Длина не должна превышать 1 000 000 символов: "))

    
 
str1 = '1'
str0 = '0'
step = len(str1)
for i in range(len(stri) - step + 1):
    if str1 != stri[i : i + step]:
        if str0 != stri[i : i + step]:
            print("Введены символы, не равные 0 и 1")
            quit()
        
    
    
def press(stri):
    blocks=[]
    tmp=''
    for a in stri:
        tmp=tmp+a
        if not tmp in blocks:
            blocks.append(tmp)
            tmp=''
 
    blocks.append(tmp)        
    return blocks
      
print(press(stri))