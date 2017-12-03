""" print dialoge is function which can be used to print proper convesation
between any two person """

def save_dialog(file):
    men = []
    other = []
    try:
        for item in file:
            try :
                (person,dialog)= item.split(':',1)
                if person =='Man':
                    men.append(dialog)
                elif person == 'Other Man':
                    other.append(dialog)
            except ValueError :
                pass
    except IOError as arr:
        print("file doesnot exist "+ str(arr))

    try:
        with open('men_dialog.txt','w')as men_dialog:
            print(men,file=men_dialog)
        with open('other_dialog.txt','w')as other_dialog:
            print(other,file=other_dialog)

    except:
        print("File Error")

    

    
        
