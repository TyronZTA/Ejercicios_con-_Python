"""Fizz Buzz"""

num= int(input("Ingrese un digito: "))


while num>0 and num<20:        
    """Acá simplemente lo limito para no hacer un bucle infinito"""
       
    if num%3==0:
        print("efervescencia")    
    elif num%5==0:
        print("zumbido")
    elif num%15==0:
        print("efervescencia")
    else:
        print(num)
    num+= 1