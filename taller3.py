class Nodo:
    """Representa un nodo de la lista doblemente enlazada."""
    def __init__(self, codigo, cliente, estado):
        self.codigo = codigo
        self.cliente = cliente
        self.estado = estado      # "En proceso", "Enviado", "Entregado"
        self.anterior = None
        self.siguiente = None

class ListaDobleEnlazada:
    """Lista doblemente enlazada para gestionar envíos."""
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def esta_vacia(self):
        return self.cabeza is None

    def agregar_envio(self, codigo, cliente, estado):
        """Agrega un nuevo envío al final de la lista."""
        if self.buscar_por_codigo(codigo) is not None:
            print(f"Error: Ya existe un envío con código {codigo}.")
            return False
        nuevo = Nodo(codigo, cliente, estado)
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.anterior = self.cola
            self.cola.siguiente = nuevo
            self.cola = nuevo
        self.tamanio += 1
        print(f"Envío {codigo} agregado correctamente.")
        return True

    def buscar_por_codigo(self, codigo):
        """Retorna el nodo que contiene el código, o None si no existe."""
        actual = self.cabeza
        while actual is not None:
            if actual.codigo == codigo:
                return actual
            actual = actual.siguiente
        return None

    def eliminar_por_codigo(self, codigo):
        """Elimina el envío con el código dado."""
        nodo = self.buscar_por_codigo(codigo)
        if nodo is None:
            print(f"No se encontró el envío con código {codigo}.")
            return False
        # si es el único nodo
        if nodo == self.cabeza and nodo == self.cola:
            self.cabeza = None
            self.cola = None
        # si es la cabeza
        elif nodo == self.cabeza:
            self.cabeza = nodo.siguiente
            self.cabeza.anterior = None
        # si es la cola
        elif nodo == self.cola:
            self.cola = nodo.anterior
            self.cola.siguiente = None
        # Nodo intermedio
        else:
            nodo.anterior.siguiente = nodo.siguiente
            nodo.siguiente.anterior = nodo.anterior
        self.tamanio -= 1
        print(f"Envío {codigo} eliminado correctamente.")
        return True

    def mostrar_adelante(self):
        """Recorre la lista desde la cabeza hacia la cola."""
        if self.esta_vacia():
            print("No hay envíos registrados.")
            return
        print("\n=== LISTA DE ENVÍOS (orden normal) ===")
        actual = self.cabeza
        while actual is not None:
            print(f"Código: {actual.codigo} | Cliente: {actual.cliente} | Estado: {actual.estado}")
            actual = actual.siguiente
        print("======================================\n")

    def mostrar_atras(self):
        """Recorre la lista desde la cola hacia la cabeza (bidireccional)."""
        if self.esta_vacia():
            print("No hay envíos registrados.")
            return
        print("\n=== LISTA DE ENVÍOS (orden inverso) ===")
        actual = self.cola
        while actual is not None:
            print(f"Código: {actual.codigo} | Cliente: {actual.cliente} | Estado: {actual.estado}")
            actual = actual.anterior
        print("========================================\n")

# ------------------- menú interactivo -------------------
def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN DE ENVÍOS ---")
    print("1. Agregar envío")
    print("2. Buscar envío por código")
    print("3. Eliminar envío")
    print("4. Mostrar envíos (adelante)")
    print("5. Mostrar envíos (atrás - recorrido bidireccional)")
    print("6. Salir")
    return input("Seleccione una opción: ")

def main():
    lista_envios = ListaDobleEnlazada()
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            codigo = input("Código del envío: ").strip()
            cliente = input("Nombre del cliente: ").strip()
            print("Estados: En proceso, Enviado, Entregado")
            estado = input("Estado: ").strip().capitalize()
            if estado not in ["En proceso", "Enviado", "Entregado"]:
                print("Estado no válido. Se asignará 'En proceso'.")
                estado = "En proceso"
            lista_envios.agregar_envio(codigo, cliente, estado)
        elif opcion == "2":
            codigo = input("Código del envío a buscar: ").strip()
            nodo = lista_envios.buscar_por_codigo(codigo)
            if nodo:
                print(f"Envío encontrado -> Código: {nodo.codigo} | Cliente: {nodo.cliente} | Estado: {nodo.estado}")
            else:
                print("Envío no encontrado.")
        elif opcion == "3":
            codigo = input("Código del envío a eliminar: ").strip()
            lista_envios.eliminar_por_codigo(codigo)
        elif opcion == "4":
            lista_envios.mostrar_adelante()
        elif opcion == "5":
            lista_envios.mostrar_atras()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()