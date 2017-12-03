import pickle
def pickle_print_dialog():
    try:
        with open('man_dialog.txt','wb')as man_file:
            pickle.dump(man,file = man_file)
        with open('other_dialog.txt','wb')as other_file:
            pickel.dump(other,file = other_file )
        except IOError as arr:
            print("Error "+str(arr))
        except pickle.PickleError as prr :
            print("Pickle Error"+str(prr))
        
