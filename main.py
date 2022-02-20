import turtle

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
        
  #      self.__createRunners()
    
  #  def createRunners(self):         
        for i in range(4): # lo hacemos en un bucle
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i]) 
            new_turtle.shape('turtle')
            new_turtle.penup()
            new_turtle.setpos(self.__startLine, self.__posStartY[i])
                                   
            self.corredores.append(new_turtle)
              
              

if __name__ == '__main__':
    circuito = Circuito(640, 480)