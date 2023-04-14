def pobierzLiczbe(str):
    ret=''
    for lit in str:
        if lit >= '0' and lit <= '9':
            ret+=lit
            continue
        if lit > '9' and len(ret)==0:
            continue
        if (lit == '.' or lit == ',') and '.' not in ret:
            ret+='.'
        elif (lit == '-' or lit == '+') and len(ret) == 0:
            ret+=lit
        else:
            break
    #if '.' in ret:
    #    return float(ret)
    #return int(ret)
    
    return float(ret) if '.' in ret else int(ret)
    pass

def wykonajDzialanie:

#suma=0
#while True:
#    x=pobierzLiczbe(input("Podaj kolejną liczbę: "))
#    if x==0:
#        break
#    suma+=x
#    pass
#print("Suma wynosi: ", suma)
