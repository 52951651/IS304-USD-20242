'''
Tarea para antes de la  próxima clase:
Crear un programa en Python que cree una clase denominada CuentaBancaria. Agregar encapsulamiento y sobrecarga del constructor de clase, asi como los métodos get y set requeridos para gestionar los atributos de dicha clase.
Los atributos de la clase debern ser: __numeroCta, __nombreCliente, __fechaApertura, __saldo.
Agregar metodos para aperturar cuentas, realizar consignaciones y retiros controlados (es decir, no permitir consignaciones negativas, ni retiros superiores al saldo, las aperturas deben exigir un valor inicial mínimo de 100 mil pesos).
Crear un menú para crear objetos y realizar las diversas operaciones referidas.

'''
class CuentaBancaria:
  class CuentaBancaria:
    def __init__(self, numeroCta, nombreCliente, fechaApertura, saldo=100000):
        # Atributos privados
        self.__numeroCta = numeroCta
        self.__nombreCliente = nombreCliente
        self.__fechaApertura = fechaApertura
        if saldo >= 100000:
            self.__saldo = saldo
        else:
            raise ValueError("El saldo inicial debe ser al menos 100,000 pesos.")

    # Métodos GET
    def get_numeroCta(self):
        return self.__numeroCta

    def get_nombreCliente(self):
        return self.__nombreCliente

    def get_fechaApertura(self):
        return self.__fechaApertura

    def get_saldo(self):
        return self.__saldo

    # Métodos SET
    def set_nombreCliente(self, nombreCliente):
        self.__nombreCliente = nombreCliente

    def set_fechaApertura(self, fechaApertura):
        self.__fechaApertura = fechaApertura

    def set_saldo(self, saldo):
        if saldo >= 0:
            self.__saldo = saldo
        else:
            raise ValueError("El saldo no puede ser negativo.")

    # Método para consignar dinero
    def consignar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Consignación exitosa. Nuevo saldo: {self.__saldo} pesos.")
        else:
            print("No se puede consignar una cantidad negativa o cero.")

    # Método para retirar dinero
    def retirar(self, cantidad):
        if cantidad > self.__saldo:
            print("Fondos insuficientes para realizar el retiro.")
        elif cantidad <= 0:
            print("No se puede retirar una cantidad negativa o cero.")
        else:
            self.__saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldo} pesos.")

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- MENÚ DE OPERACIONES BANCARIAS ---")
    print("1. Aperturar cuenta")
    print("2. Consultar saldo")
    print("3. Consignar dinero")
    print("4. Retirar dinero")
    print("5. Salir")

# Programa principal
def main():
    cuenta = None

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            numeroCta = input("Ingrese el número de cuenta: ")
            nombreCliente = input("Ingrese el nombre del cliente: ")
            fechaApertura = input("Ingrese la fecha de apertura (dd/mm/yyyy): ")
            saldo = int(input("Ingrese el saldo inicial (mínimo 100,000 pesos): "))
            try:
                cuenta = CuentaBancaria(numeroCta, nombreCliente, fechaApertura, saldo)
                print("Cuenta aperturada exitosamente.")
            except ValueError as ve:
                print(ve)

        elif opcion == '2':
            if cuenta:
                print(f"Saldo actual: {cuenta.get_saldo()} pesos.")
            else:
                print("Debe aperturar una cuenta primero.")

        elif opcion == '3':
            if cuenta:
                cantidad = int(input("Ingrese la cantidad a consignar: "))
                cuenta.consignar(cantidad)
            else:
                print("Debe aperturar una cuenta primero.")

        elif opcion == '4':
            if cuenta:
                cantidad = int(input("Ingrese la cantidad a retirar: "))
                cuenta.retirar(cantidad)
            else:
                print("Debe aperturar una cuenta primero.")

        elif opcion == '5':
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

