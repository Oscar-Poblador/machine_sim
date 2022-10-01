def asm_pio(*args, **kwargs):
#Decorador de la función a realizar, lee sus parámetros de trabajo
    def decorador(programa):
    #Decora el programa
        def compilador():
            print("Parámetros", kwargs)
            #Imprimer parametros del programa a ejecutar
            programa() #Ejecuta el programa 
            return None #No retorna nada
        return compilador #Retorna compilador 
    return decorador #Retorna decorador

def decorador_instr(fun_inst):
#Decora las instruccione e ingresa la función a decorar
    def decoracion_instr(self,*args, **kwargs):
    #Ingresa la función en el que fue utilizado, sus argumentos y librerias
        fun_inst(self,*args, **kwargs)#inicializa la función que lo utilizó
        return None #No retorna nada
    return decoracion_instr#Retorna la decoración

pins='pins'

class PIO():
    #Crea la clase PIO para inicializar la rp2 en OUT_LOW
    OUT_LOW='PIO.OUT_LOW'
    

class StateMachine:
#Define el estado de la maquina de estados de la rp2
  def __init__(self, id_, program, freq=125000000, **kwargs):
    #Ingrea la maquina de estados a trabajar, el nombre del programa a relizar, la frecuencia de trabajo, guarda en la libreria el pin o pines de uso
        global sm_iniciandose,fsms
        #Define de forma globlal las distints funciones y crea la función para inicializar la rp2
        sm_iniciandose=self
        #Inicializa la función con ella misma
        self.lista_instr=[]
        #Ingresa una lista de instrucciones a la función
        program() #Ejecuta el programa que desea realizar 
        print('Fueron leidas',len(self.lista_instr), 'instrucciones')
        #Imprime la cantidad de instrucciones leídas
        sm_iniciandose=None #Reinicia la inicialización 
        fsms[id_]=self #Iguala la lista de maquinas de estados a la que ingresó al inicio de la función
        pass
      
        
  def active(self, x=None):
    #Permite determinar si la función está activa o no
    '''Esta rutina simula exclisivamnte esa FSM. Sería interesante crear simulación en parlelo con otras FSM'''
    if x==1:
        #Si está activa imprime el mensaje 
        print('Está pendiente de realizar la simulacón') #Esta función no se está realizando 

fsms=[None]*8 #Crea una lista de maquinas de estado para la rp2 e inicializa todas en NONE, hay un total 8 maquina en la lista

sm_iniciandose=None    #Define la inicialización del sistema en None 


class nop:
#Clase de la función Nop
    @decorador_instr
    def __init__(self,*args, **kwargs):
        #Ingresan los parámetros de la función y a sí misma
        global sm_iniciandose #Define su inicilización como global
        print(self.__class__.__name__)#,'nop.__init__',args,kwargs)
        #Imprime el nombre de la clase Nop
        sm_iniciandose.lista_instr.append(self) #Agrega la función nop a la lista de funciones

        pass
     
    def __getitem__(self,name):
        #Ingresa la función nop y la varibale nombre
        pass #No hace nada
        
class set(nop):
#Clase de la función set y hereda de NOP
    def __init__(self,*args, **kwargs):
    #Inicializa la función y lee el estado del pin como argumentos y guarda el número de pin en librerias    
        super().__init__(*args, **kwargs)
        #Toma los datos ingresados y hereda los metodos de inicio de la clase NOP
        pass
   
class wrap_target(nop):
#Clase de wrap target y hereda de NOP 
    def __init__(self,*args, **kwargs):
    #Inicializa la función wrap y lee si hay argumentos de inicio 
         super().__init__(*args, **kwargs)
         #Toma los datos ingresados y hereda los metodos de inicio de la clase NOP
         pass 
  
class wrap(nop):
#Clase de la función wrap y hereda de Nop
    def __init__(self,*args, **kwargs):
    #Inicializa la función wrap y lee si hay argumentos de inicio 
         super().__init__(*args, **kwargs)
         #Toma los datos ingresados y hereda los metodos de inicio de la clase NOP
         pass 
         
         
