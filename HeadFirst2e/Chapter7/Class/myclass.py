
class MyClass:
    def __init__(self, v : int= 0, i :int =0 )->None:
        self.var =v
        self.inc=i
        
    def increment(self):
        self.var += self.inc

    def __repr__(self)->str:
        return str(self.var)
