class LivePercentage:
    def __init__(self,minimum,maximum):
        self.min = minimum # minimum number of range
        self.max = maximum # maximum number of range
        self.val = None
    def _percOf(self,number): return(((number - self.min) * 100) / (self.max - self.min))
    def _numOf(self,percentage): return(((percentage * (self.max - self.min) / 100) + self.min))
    def getPerc(self,*args): return(self._percOf(self.val))
    def getNum(self,*args): return(self.val)
    def setPerc(self,percentage): self.val = self._numOf(percentage)
    def setNum(self,number): self.val = number
    def set(self,user_in):
        in_type = type(user_in)
        if in_type == str and '%' in user_in: print("percentage is WIP!"); raise Exception()
        elif in_type == (int or float): self.setNum(user_in)
        else: raise TypeError("accepted formats: integer, float or string as 'x%'")
def clamp(val,minimum,maximum):
    if val < minimum: return(minimum)
    elif val > maximum: return(maximum)
    elif val >= minimum and val <= maximum: return(val)
    else: raise Exception("an error occured while clamping values")
#def percentOf(val,scaleBy): return((val/100)*scaleBy)
