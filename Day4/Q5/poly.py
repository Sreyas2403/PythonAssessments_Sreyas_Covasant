class Poly:
    def __init__(self, *args):
        self.args = args
        
    def __str__(self):
        return f"{self.args}"
        
        
    def __add__(self,other):
        if not isinstance(other, Poly):
            return NotImplemented

        c1, c2 = self.args, other.args
        if len(c1) < len(c2):
            c1 = (0,) * (len(c2) - len(c1)) + c1
        else:
            c2 = (0,) * (len(c1) - len(c2)) + c2
            
        result = tuple(a + b for a, b in zip(c1, c2))
        return Poly(*result)    

        
        

       