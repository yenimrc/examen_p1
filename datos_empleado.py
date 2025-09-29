from abc import ABC 
from abc import abstractmethod


monto_vendido=5800
tasa_comision=3600
ingresos=monto_vendido*tasa_comision
sueldo_base=4500

class Empleado():
    @abstractmethod
    def __init__(self,rfc,apellidos,nombre,ingresos=4250):
        self._rfc=rfc
        self._apellidos=apellidos
        self.nombre=nombre
        self.ingresos=ingresos

class EmpleadoVendedor(Empleado):

    def __init__(self, rfc, apellidos, nombre,ingresos):
        super().__init__(rfc, apellidos, nombre,ingresos)

    def ingresos(self):
        ingresos=monto_vendido*tasa_comision
        monto_vendido=5800
        tasa_comision=3600
        print(f'Los ingresos de {self.nombre} son de {ingresos}')
    
    def bonificacion(self):
        if monto_vendido>1000:
            print('No obtienes bonificacion')
        elif 1000<monto_vendido<5000:
            print('Tu bonificacion es del 5% de tus ingresos')
        else:
            print('Tu bonoficacion es del 10% de tus ingresos')

    def descuento(self):
        if ingresos<1000:
            print('Tu descuento es del 11%')
        else:
            print('Tu descuento es del 15%')
    
    def sueldo_neto(self):
        print(f'Tu sueldo neto es de: {ingresos+ self.bonificacion()-self.descuento()}')


class EmpleadoPermanente(Empleado):
    def __init__(self, rfc, apellidos, nombre):
        super().__init__(rfc, apellidos, nombre)

    def sueldo_base(self):
        return sueldo_base
    
    def descuento(self):
        if ingresos<1000:
            print('Tu descuento es del 11%')
        else:
            print('Tu descuento es del 15%')
    
    def sueldo_neto(self):
        print(f'Tu sueldo neto es de: {ingresos - self.descuento()}')

empleado1=Empleado('VECJ880326XXX','Luciano','Anna')
#empleado1=EmpleadoVendedor()
empleado1.ingresos

#empleado2=Empleado('VECJ880326XHT','Perez','Juan')
#print(empleado1.sueldo_neto())




