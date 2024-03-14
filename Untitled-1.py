import datetime
class ImplanteMedico:
    def __init__(self, tipo, funcion, paciente):
        self.__tipo = tipo
        self.__funcion = funcion
        self.__paciente = paciente
        self.__fecha_implantacion = None
        self.__medico_responsable = None
        self.__estado_implante = None

    def set_fecha_implantacion(self, fecha_implantacion):
        try:
            datetime.datetime.strptime(fecha_implantacion, "%Y-%m-%d")
        except ValueError:
            print("La fecha de implantación no es válida. debe ser de tipo 'YYYY-MM-DD'.")
            return
        self.__fecha_implantacion = fecha_implantacion

    def get_fecha_implantacion(self):
        return self.__fecha_implantacion

    def set_medico_responsable(self, medico_responsable):
        self.__medico_responsable = medico_responsable

    def get_medico_responsable(self):
        return self.__medico_responsable

    def set_estado_implante(self, estado_implante):
        self.__estado_implante = estado_implante

    def get_estado_implante(self):
        return self.__estado_implante
    
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
    def __init__(self, nombre, cedula):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__implante_asignado = None  

    def set_implante(self, implante):
        self.__implante_asignado = implante
    def get_implante(self):
        return self.__implante_asignado

    def obtener_implante_asignado(self):
        return self.implante_asignado
      
    def get_nombre(self):
        return self.__nombre
    def get_cedula(self):
        return self.__cedula
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_cedula(self, cedula):
        self.__cedula = cedula
    
class SistemaImplantes:
    def __init__(self):
        self.lista_implantes = []
        self.lista_pacientes = []

    def asignar_implante_paciente(self, implante, paciente, fecha_implantacion, medico_responsable, estado_implante):
        implante.set_paciente(paciente)
        paciente.set_implante(implante)
        self.set_fecha_implantacion(implante, fecha_implantacion)
        self.set_medico_responsable(implante, medico_responsable)
        self.set_estado_implante(implante, estado_implante)

    def realizar_seguimiento_vida_util_implante(self, implante, fechas_revision, mantenimiento):
        pass
    

def mostrar_menu():
        int(input(""""Menú:
                1. Agregar Implante
                2. Eliminar Implante
                3. Editar Información de Implante
                4. Visualizar Inventario
                5. Salir
                > """))
    

def agregar_implante(sistema):
    tipo = input("Tipo de implante: ")
    funcion = input("Función del implante: ")
    paciente = input("Nombre del paciente: ")
    implante = ImplanteMedico(tipo, funcion, paciente)
    sistema.lista_implantes.append(implante)
    print("Implante agregado exitosamente.")

def eliminar_implante(sistema):
    tipo = input("Ingrese el tipo de implante que desea eliminar: ")
    for implante in sistema.lista_implantes:
        if implante.tipo == tipo:
            sistema.lista_implantes.remove(implante)
            print("Implante eliminado exitosamente.")
            return
    print("No se encontró ningún implante con el tipo especificado.")

def editar_implante(sistema):
    tipo = input("Ingrese el tipo de implante que desea editar: ")
    for implante in sistema.lista_implantes:
        if implante.tipo == tipo:
            # falta proceso para ediatr implante
            print("Información del implante editada exitosamente.")
            return
    print("No se encontró ningún implante con el tipo especificado.")

def visualizar_inventario(sistema):
    print("\nInventario de Implantes:")
    for implante in sistema.lista_implantes:
        print(f"Tipo: {implante.tipo}, Función: {implante.funcion}, Paciente: {implante.paciente}")

def main():
    sistema = SistemaImplantes()
    while True:
        mostrar_menu()
        opcion = input("\nIngrese el número de la opción que desea: ")
        if opcion == 1:
            agregar_implante(sistema)
        elif opcion == 2:
            eliminar_implante(sistema)
        elif opcion == 3:
            editar_implante(sistema)
        elif opcion == 4:
            visualizar_inventario(sistema)
        elif opcion == 5:
            break
        else:
            print("Opción no válida.vuelva a intentarlo")

if __name__ == "__main__":
    main()