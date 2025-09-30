from abc import ABC 
from abc import abstractmethod


sueldo_base=4500


class Empleado():
    @abstractmethod
    def __init__(self,rfc,apellidos,nombre):
        self._rfc=rfc 
        self._apellidos=apellidos
        self._nombre=nombre
    
    @abstractmethod
    def ingresos(self):
        pass
    
    @abstractmethod
    def descuento(self):
        pass

    @abstractmethod
    def salario_neto(self):
        pass

    def informacion(self):
        return f'Apellido {self._apellidos}, nombre {self._nombre}'
    
class EmpleadoVendedor(Empleado):

    def __init__(self, rfc, apellidos, nombre,monto_vendido,comision):
        super().__init__(rfc, apellidos, nombre)
        self.monto_vendido=monto_vendido
        self.comision=comision

    def ingresos(self):
        ingreso_c=self.monto_vendido*self.comision
        if ingreso_c<1000:
            print('Salario por debajo de lo esperado')
        return ingreso_c
    
    def bonificacion(self):
        ingresos=self.ingresos
        if self.monto_vendido<1000:
            return 0
        elif 1000<=self.monto_vendido<=5000:
            return ingresos * 0.05
        else:
            print('Tu bonificacion de del 10%')

    def descuento(self):
        ingresos=self.ingresos()
        if ingresos<1000:
            print('Tu descuento es del 11%')
        else:
            print('Tu descuento es del 15%')
    
    def sueldo_neto(self):
        return (f'Tu sueldo neto es de: {self.ingresos() + self.bonificacion()-self.descuento()}')


class EmpleadoPermanente(Empleado):
    def __init__(self, rfc, apellidos, nombre,salario,nss):
        super().__init__(rfc, apellidos, nombre)
        self.salario=salario
        self.nss=nss
        if salario<1000:
            raise ValueError('Salario menor al esperado')

    def ingresos(self):
        return self.salario

    def sueldo_base(self):
        return sueldo_base
    
    def descuento(self):
        if self.ingresos<1000:
            print(f'Tu descuento es del 11%, ${self.salario*0.11}')
        else:
            print(f'Tu descuento es del 15%, ${self.salario*0.15}')
    
    def sueldo_neto(self):
        print(f'Tu sueldo neto es de: {self.ingresos() - self.descuento()}')

vendedor1=EmpleadoVendedor('VECJ880326XXX', 'Lopez', 'Maria', 30000, 0.10)
print(f'Ingreso: {vendedor1.ingresos()}')
print(f'Descuento: {vendedor1.descuento()}')
print(f'Salario neto: {vendedor1.bonificacion()}')
print(' ')
e_permanente1=EmpleadoPermanente('VECJ880326YHT','Juarez','Benito',4700, 123456)
print(f'Ingreso: {e_permanente1.ingresos()}')
print(f'Descuento: {e_permanente1.sueldo_base()}')
print(f'Salario neto: {e_permanente1.sueldo_neto()}')





