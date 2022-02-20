import turtle
import random

class Circuito():
    corredores = []
    __posStartY = (-60, -20, 20, 60)
    __colorTurtle = ('red', 'blue', 'green', 'orange')
        
    def __init__(self, width, height):     
        self.__screen =  turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgrey')
        self.__startLine = (-width / 2) + 20 # en lugar de 20, un 5% de ancho total?
        self.__finishLine = (width / 2) - 20
        
        self.__createRunners()
    
    def __createRunners(self):         
        for i in range(4): # lo hacemos en un bucle
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i]) 
            new_turtle.shape('turtle')
            new_turtle.penup()
            new_turtle.setpos(self.__startLine, self.__posStartY[i])
                                   
            self.corredores.append(new_turtle)
    
   # avanzando por turno, como tirando dados, en cada turno, cada instancia hace una accion.
    def competir(self):
          
        hayGanador = False
          
        while not hayGanador:
            for tortuga in self.corredores:
                avance = random.randint(1, 10)
                tortuga.forward(avance)
                  
                if tortuga.position()[0] >= self.__finishLine:
                    hayGanador = True
                    print('La tortuga de color {} ha ganado'.format(tortuga.color()[0]))
                    break 
                
if __name__ == '__main__':
    circuito = Circuito(640, 480)
    circuito.competir()