class cinemaLoyaltyCard:


    def __init__(self,memberNumber):
        self._memberNumber=memberNumber
        self._numPoints=0

    def   addPoints(self,points):
          self._numPoints=self._numPoints+points



    def redeem(self,num):
        if(self._numPoints > num):
           self._numPoints=self._numPoints - num
           return True
        return False

    def getID(self):
        return self._memberNumber


    def getTotalPoints(self):
        return self._numPoints
        

class PlatinumcinemaLoyaltyCard(cinemaLoyaltyCard):

    
    def __init__(self,memberNumber):
        super().__init__(memberNumber)
        #self._numPoints=0
        #self._memberNumber=memberNumber


    def  addPoints(self,points):
         #self._numPoints=self._numPoints + points + self.PLATINUMREWARD
         super().addPoints(points+10)

    def getID(self):
        #return self._membernum
        super().getID()
  
    def getTotalPoints(self):
        #return self._numPoints
        super().getTotalPoints()

    def redeem(self,num):
        if(self._numPoints > num):
           self._numPoints=self._numPoints-num
           return True
        return False

b= cinemaLoyaltyCard(555)
print(b.getID())
#expected 555
b.addPoints(50)
print('expexted 50')
b.redeem(5)

print(b.getTotalPoints())
print('expected 45')



d= PlatinumcinemaLoyaltyCard(667)
print(d.getID())
print('expected 667')
d.addPoints(50)
d.redeem(20)
print(d.getTotalPoints())
print('expected 30')
