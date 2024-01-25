class NECTO: #Великая задача Пчело-слона... или о Нечто в интерпритации Олега Юрьевича
    def __init__(self,bee:int,elephant:int):
        self.bee=bee
        self.elephant=elephant
    def fly(self):
        if self.bee >= self.elephant:
            return True
        else:
            return False
    def trumpet (self):
        if self.elephant >= self.bee:
            return "Tu-tu-doo-doo"
        else:
            return 'WZZZZZZZZZ'
    def eat(self, meal, value=0):#meal - траву или нектар, value - сколько едим
        if value == 'nectar':
            if self.elephant-value >= 0 and self.bee <=100:
                self.elephant -= value
                self.bee+=value
            elif self.elephant-value<0 and self.bee <=100:
                module= abs(self.elephant-value)
                self.elephant = 0
                self.bee += value - module
            elif self.elephant-value >0 and self.bee > 100:
                module = (self.bee + value) - 100
                self.bee=100
    def ger_parts (self):
        return [self.bee,self.elephant]
