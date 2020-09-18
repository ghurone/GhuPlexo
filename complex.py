from math import sqrt, atan, sin, cos, e, log

class Complexo:
    def __init__(self, re=0, im=0):
        self._re = re
        self._im = im
        
    def __repr__(self):
        if self._re == 0 and self._im == 0:
            s = '0'
        elif self._re == 0:
            s = f'{self._im}𝒊'
        elif self._im == 0:
            s = f'{self._re}'
        else:
            if self._im > 0:
                s = f'({self._re} + {self._im}j)'
            else:
                s = f'({self._re} - {-1*self._im}j)'
        return s
    
    def __str__(self):
        return self.__repr__()
    
    def __int__(self):
        if self._im != 0:
            raise TypeError('Não consigo converter um complexo para um int')
        else:
            return int(self._re)
    
    def __float__(self):
        if self._im != 0:
            raise TypeError('Não consigo converter um complexo para um float')
        else:
            return float(self._re)
    
    def __eq__(self, other):
        if isinstance(other, (int, float)):
            if self._im == 0:
                return self._re == other
            else:
                return False
        elif isinstance(other, complex):
            return self._re == other.real and self._im == other.imag
        elif isinstance(other, Complexo):
            return self._re == other.__re and self._im == other.__im
        else:
            self.__ErroOperation()
    
    def __pos__(self):
        return self
    
    def __neg__(self):
        return Complexo(-self._re, -self._im)
    
    def __abs__(self):
        return Complexo(abs(self._re), abs(self._im))
    
    def __bool__(self):
        return self._re != 0 and self._im !=0
    
    def __add__(self, other):
        """Método para somar Complexoos"""
        if isinstance(other, (int, float)):
            re = self._re + other
            im = self._im
        elif isinstance(other, complex):
            re = self._re + other.real
            im = self._im + other.imag
        elif isinstance(other, Complexo):
            re = self._re + other._re
            im = self._im + other._im
        else:
            self.__ErroOperation()
            
        return Complexo(re, im)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        """Método para subtrair Complexoos"""
        if isinstance(other, (int, float)):
            re = self._re - other
            im = self._im
        elif isinstance(other, complex):
            re = self._re - other.real
            im = self._im - other.imag
        elif isinstance(other, Complexo):
            re = self._re - other._re
            im = self._im - other._im
        else:
            self.__ErrorOperation()
            
        return Complexo(re, im)
    
    def __rsub__(self, other):
        return -self.__sub__(other)
    
    def __mul__(self, other):
        """Método para multiplicar Complexoos"""
        if isinstance(other, (int, float)):
            re = self._re * other
            im = self._im * other
        elif isinstance(other, complex):
            re = self._re * other.real - self._im * other.imag
            im = self._re * other.imag + self._im * other.real
        elif isinstance(other, Complexo):
            re = self._re * other._re - self._im * other._im
            im = self._re * other._im + self._im * other._re
        else:
            self.__ErroOperation()
        
        return Complexo(re, im)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        """Método para dividir complexos"""
        if isinstance(other, (int, float)):
            re = self._re / other
            im = self._im / other
        elif isinstance(other, complex):
            den = other.real**2 + other.imag **2
            re = (self._re * other.real + self._im * other.imag) / den
            im = (self._im * other.real - self._re * other.imag) / den
        elif isinstance(other, Complexo):
            den = other._re**2 + other._im **2
            re = (self._re * other._re + self._im * other._im) / den
            im = (self._im * other._re - self._re * other._im) / den
        else:
            self.__ErroOperation()
        
        return Complexo(re, im)
        
    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            den = self._re**2 + self._im**2
            re = (other * self._re) / den
            im = (-other * self._im) / den
        elif isinstance(other, complex):
            den = self._re**2 + self._im**2
            re = (other.real * self._re + other.imag * self._im) / den
            im = (other.imag * self._re - other.real * self._im) / den
        else:
            return self.__truediv__(other)
        
        return Complexo(re, im)
    
    def __pow__(self, other):
        """Método para exponenciação de complexos"""
        mod_z, theta = self.modulo, self.angulo
        
        if isinstance(other, (float, int)):
            re = round((mod_z**other) * cos(other * theta),3)
            im = round((mod_z**other) * sin(other * theta),3)
        elif isinstance(other, Complexo):
            const = e ** (other._re * log(mod_z) - other._im*theta)
            arg = other._re*theta + other._im*log(mod_z)
            re = const * cos(arg)
            im = const * sin(arg)
        elif isinstance(other, complex):
            const = e ** (other.real * log(mod_z) - other.imag*theta)
            arg = other.real*theta + other.imag*log(mod_z)
            re = const * cos(arg)
            im = const * sin(arg)        
        else:
            self.__ErroOperation()
            
        return Complexo(re, im)
        
    def __rpow__(self, other):
        if isinstance(other, (int, float)):
            const = other**self._re
            re = const * cos(self._im * log(other))
            im = const * sin(self._im * log(other))
        elif isinstance(other, complex):    
            mod_z = sqrt((other.real)**2 + (other.imag)**2)
            theta = atan(other.imag/other.real)
            
            const = e ** (self._re * log(mod_z) - self._im*theta)
            arg = self._re*theta + self._im*log(mod_z)
            re = const * cos(arg)
            im = const * sin(arg)
        else:
            return self.__pow__(other)
            
        return Complexo(re, im)
    
    @property
    def conjugado(self):
        """Retorna o conjugado do número complexo"""
        return Complexo(self._re, -self._im)
    
    @property
    def modulo(self):
        """Retorna o módulo do número complexo"""
        return sqrt((self._re)**2 + (self._im)**2)
    
    @property
    def angulo(self):
        """Retorna o ângulo - em radianos - com a reta real."""
        return atan(self._im/self._re)
    
    @property
    def real(self):
        """Retorna a parte real do número complexo."""
        return self._re
    
    @property
    def imag(self):
        """Retorna a parte imaginária do número complexo."""
        return self._im
    
    @staticmethod    
    def __ErroOperation():
        """Errozinho"""
        raise TypeError('Esse objeto não consegue fazer esse tipo de operação')
        