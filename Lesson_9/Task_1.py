from time import sleep
from itertools import cycle

class TrafficLight():
    colors=['red','yellow','green']
    color_duration = {'red': 7, 'yellow': 2, 'green': 10}
    def state(self,color='red'):
        i=0
        color_idx=self.colors.index(color)
        if color_idx==2:
            prev=color_idx
            print(color)
            sleep(self.color_duration[color])
            color_idx-=1




        # i=0
        # while i!=iter:
        #     for color in self.colors:
        #         print(color)
        #         sleep(self.color_duration[color])
        #     i+=1





    def running(self,iter):
        for i in range(iter):
            a=cycle(TrafficLight.color)
            next(a)
            print(a)