""" print dialoge is function which can be used to print proper convesation
between any two person """

def print_dialog(file):
    try:
        for item in file:
            #if not item.find(':')==-1:
            try :
                (person,dialog)= item.split(':',1)
                print(person,end='')
                print(" said",end ='')
                print(dialog,end='')
            #else :
            except:
                print("") 
    except:
        pass

    finally :
        pass
    
        
