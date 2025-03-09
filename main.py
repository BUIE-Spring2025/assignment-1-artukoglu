def int_to_roman(num):
    number_of_digits = len(str(num))
    
    
    output_list = []
    # 1 basamaklı sayı yazılırsa
    def ondalik(num1):
        if num1 == "0":
            return ""
        if num1 == "1":
            return "I"
        if num1 == "2":
            return "II"
        if num1 == "3":
            return "III"
        if num1 == "4":
            return "IV"
        if num1 == "5":
            return "V"
        if num1 == "6":
            return "VI"
        if num1 == "7":
            return "VII"
        if num1 == "8":
            return "VIII"
        if num1 == "9":
            return "IX"
    
    def yuzdelik(num2):
        if num2 == "1":
            return "X"
        if num2 == "2":
            return "XX"
        if num2 == "3":
            return "XXX"
        if num2 == "4":
            return "XL"
        if num2 == "5":
            return "L"
        if num2 == "6":
            return "LX"
        if num2 == "7":
            return "LXX"
        if num2 == "8":
            return "LXXX"
        if num2 == "9":
            return "XC"
        if num2 == "0":
            return ""

    def binlik(num3):
        if num3 == "1":
            return "C"
        if num3 == "2":
            return "CC"
        if num3 == "3":
            return "CCC"
        if num3 == "4":
            return "CD"
        if num3 == "5":
            return "D"
        if num3 == "6":
            return "DC"
        if num3 == "7":
            return "DCC"
        if num3 == "8":
            return "DCCC"
        if num3 == "9":
            return "CM"
        if num3 == "0":
            return ""

    def onbinlik(num4):
        if num4 == "1":
            return "M"
        if num4 == "2":
            return "MM"
        if num4 == "3":
            return "MMM"
        
    
    
    if number_of_digits == 1:
        
        return ondalik(str(num))
    
    if number_of_digits == 4:

        a = ondalik(str(num)[-1])

        b = yuzdelik(str(num)[-2])
        
        c = binlik(str(num)[-3])

        d = onbinlik(str(num)[-4])


        output_list.append(d)
        output_list.append(c)
        output_list.append(b)
        output_list.append(a)
        
        
        
        list = ""
        for i in output_list:
            
            list += i
        return list
    
    if number_of_digits == 2:

        a = ondalik(str(num)[-1])

        b = yuzdelik(str(num)[-2])
        
        

        output_list.append(b)
        output_list.append(a)
        
        
        list2 = ""
        for i in output_list:
            
            list2 += i
        return list2
    

    if number_of_digits == 3:

        a = ondalik(str(num)[-1])

        b = yuzdelik(str(num)[-2])
        
        c = binlik(str(num)[-3])


        output_list.append(c)
        output_list.append(b)
        output_list.append(a)
        
        
        
        list3 = ""
        for i in output_list:
            
            list3 += i
        return list3
    


        

        

        


    
    
    
    
    
    
    
    
    
