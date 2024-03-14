class ImplanteMedico:
    def __init__(self, tipo, funcion, paciente):
        self.__tipo = tipo
        self.__funcion = funcion
        self.__paciente = paciente

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def get_funcion(self):
        return self.__funcion

    def set_funcion(self, funcion):
        self.__funcion = funcion

    def set_paciente(self, paciente):
        self.__paciente = paciente


class ImplanteCadera(ImplanteMedico):
    def __init__(self,tipo, funcion, material, tamaño, tipo_fijacion):
        super().__init__(tipo, funcion)
        self.__tipo_fijacion = tipo_fijacion
        self.__material = material
        self.__tamaño = tamaño
    def get_tipo_fijacion(self):
        return self.__tipo_fijacion
    def set_tipo_fijacion(self, tipo_fijacion):
        self.__tipo_fijacion = tipo_fijacion
    def get_material(self):
        return self.__material
    def set_material(self, material):
        self.__material = material
    def get_tamaño(self):
        return self.__tamaño
    def set_tamaño(self, tamaño):
        self.__tamaño = tamaño
        
class ImplanteRodilla(ImplanteMedico):
    def __init__(self,tipo, funcion, material, tamaño, tipo_fijacion):
        super().__init__(tipo, funcion)
        self.__tipo_fijacion = tipo_fijacion
        self.__material = material
        self.__tamaño = tamaño
    def get_tipo_fijacion(self):
        return self.__tipo_fijacion
    def set_tipo_fijacion(self, tipo_fijacion):
        self.__tipo_fijacion = tipo_fijacion
    def get_material(self):
        return self.__material
    def set_material(self, material):
        self.__material = material
    def get_tamaño(self):
        return self.__tamaño
    def set_tamaño(self, tamaño):
        self.__tamaño = tamaño


class Marcapasos(ImplanteMedico):
    def __init__(self, tipo, funcion, num_electrodos, conexion, frecuencia):
        super().__init__(tipo, funcion)
        self.__num_electrodos = num_electrodos
        self.__conexion = conexion
        self.__frecuencia= frecuencia
    
    def get_num_electrodos(self):
        return self.__num_electrodos
    def set_num_electrodos(self, num_electrodos):
        self.__num_electrodos = num_electrodos
    def get_conexion(self):
        return self.__conexion
    def set_conexion(self, conexion):
        self.__conexion = conexion
    def get_frecuencia(self):
        return self.__frecuencia
    def set_frecuencia(self, frecuencia):
        self.__frecuencia = frecuencia

class StentCoronario(ImplanteMedico):
    def __init__(self, funcion, tipo, longitud, diametro, material):
        super().__init__(tipo, funcion)
        self.__longitud = longitud
        self.__diametro = diametro
        self.__material= material

    def get_longitud(self):
        return self.__longitud
    def set_num_electrodos(self, longitud):
        self.__longitud = longitud
    def get_diametro(self):
        return self.__diametro
    def set_diametro(self, diametro):
        self.__diametro = diametro
    def get_material(self):
        return self.__material
    def set_frecuencia(self, material):
        self.__material = material

class ImplanteDental(ImplanteMedico):
    def __init__(self, funcion, tipo, forma, sis_fijacion, material):
        super().__init__(tipo, funcion)
        self.__material = material
        self.__sis_fijacion = sis_fijacion
        self.__forma = forma
    def get_sis_fijacion(self):
        return self.__sis_fijacion
    def set_tipo_fijacion(self, sis_fijacion):
        self.__sis_fijacion = sis_fijacion
    def get_material(self):
        return self.__material
    def set_frecuencia(self, material):
        self.__material = material
    def get_forma(self):
        return self.__forma
    def set_frecuencia(self, forma):
        self.__forma = forma


class Paciente:
    def __init__(self, nombre, cedual):
        self.__nombre = nombre
        self.__cedula = cedula
      
    def get_nombre(self):
        return self.__nombre
    def get_cedula(self):
        return self.__cedula
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_cedula(self, cedula):
        self.__cedual = cedula
    
class SistemaImplantes:
    def __init__(self, lista_implantes):
        self.lista_implantes = lista_implantes
        self.lista_pacientes = []

    def asignar_implante_paciente(self, implante, paciente, fecha_implantacion, medico_responsable, estado_implante):

        pass

    def registrar_fecha_implantacion(self, implante, fecha_implantacion):
        
        pass

    def registrar_medico_responsable(self, implante, medico_responsable):
        
        pass

    def registrar_estado_implante(self, implante, estado_implante):
        
        pass

    def realizar_seguimiento_vida_util_implante(self, implante, fechas_revision, mantenimiento):
        pass

lista_implantes = []