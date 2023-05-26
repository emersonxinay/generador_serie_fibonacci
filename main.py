from generar import *
from seleccionar import *
from mostrar import *


opcion_serie = seleccionar_serie()
serie_generada = generar_serie(opcion_serie)
mostrar_serie(serie_generada)