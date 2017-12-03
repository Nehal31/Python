""" save dialoge is function which can be used to save the dialoges in two file
it uses the pickle library module . pickle.dump() is used to write the file and
pickle.load() to read the file . picke process the binary files"""
def save_dialog(file):
    import pickle
    man = []
    other = []
    try:
        for item in file:
            try :
                (person,dialog)= item.split(':',1)
                if person =='Man':
                    man.append(dialog)
                elif person == 'Other Man':
                    other.append(dialog)
            except ValueError :
                pass
    except IOError as arr:
        print("file doesnot exist "+ str(arr))

    try:
        with open('man_dialog.txt','wb')as man_file:
            pickle.dump(man,man_file)
        with open('other_dialog.txt','wb')as other_file:
            pickle.dump(other,other_file )
    except IOError as arr:
            print("Error "+str(arr))
    except pickle.PickleError as prr :
            print("Pickle Error"+str(prr)) 

    except :
        print("File Error")

    

    
        
