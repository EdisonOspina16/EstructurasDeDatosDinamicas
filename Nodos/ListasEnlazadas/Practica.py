class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insertar(self, elemento):
        nuevo_nodo = Node(elemento)
        if not self.head or self.head.value.prioridad < elemento.prioridad:
            nuevo_nodo.next = self.head
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.next and actual.next.value.prioridad >= elemento.prioridad:
                actual = actual.next
            nuevo_nodo.next = actual.next
            actual.next = nuevo_nodo
        self.size += 1

    def atender(self):
        if not self.head:
            raise Exception("No hay pacientes en la cola.")
        paciente_atendido = self.head.value
        self.head = self.head.next
        self.size -= 1
        return paciente_atendido

    def mostrar(self):
        if not self.head:
            raise Exception("No hay pacientes en la cola.")
        actual = self.head
        while actual:
            print(actual.value)
            actual = actual.next

    def buscar_pacientes_pares(self):

        """la funcion trata de que si los pacientes tienen la misma prioridad pares,
          devuelve el primer y el ultimo paciente
        """

        # Llevar un conteo de las prioridades.
        actual = self.head
        diccionario = {}

        while actual:
            prioridad = actual.value.prioridad
            if prioridad in diccionario:
                diccionario[prioridad].append(actual.value)
            else:
                diccionario[prioridad] = [actual.value]
            actual = actual.next
        print(diccionario)

        """while actual:
            nuevo_valor = 1
            prioridad = actual.value.prioridad
            diccionario[prioridad] = nuevo_valor
            if diccionario[prioridad] == nuevo_valor:
                diccionario[prioridad] += 1
            actual = actual.next
            print(diccionario)"""

        # Hacer la comparacion si el numero de pacientes son pares o no
        pacientes_pares = []
        for prioridad, pacientes in diccionario.items():
            if len(pacientes) % 2 == 0:
                # Sacar el primer y el ultimo paciente si se cumple lo anterior
                pacientes_pares.append((pacientes[0], pacientes[-1]))
            return pacientes_pares

class ColaPrioridad:
    def __init__(self):
        self.lista_pacientes = LinkedList()

    def enqueue(self, paciente):
        self.lista_pacientes.insertar(paciente)

    def dequeue(self):
        return self.lista_pacientes.atender()

    def fisrt(self):
        self.lista_pacientes.mostrar()

    def buscar_pacientes_pares(self):
      return self.lista_pacientes.buscar_pacientes_pares()


class Paciente:
    def __init__(self, nombre: str, descripcion_consulta: str):
        self.nombre: str = nombre
        self.descripcion_consulta: str = descripcion_consulta
        self.prioridad: int = self.calcular_prioridad()

    def calcular_prioridad(self) -> int:
        descripcion = self.descripcion_consulta.lower()
        if any(palabra in descripcion for palabra in ["dolor agudo", "fractura", "ataque"]):
            return 5
        elif any(palabra in descripcion for palabra in ["fiebre", "tos"]):
            return 3
        elif any(palabra in descripcion for palabra in ["revisión", "control"]):
            return 1
        raise Exception("Los sintomas no son validos....Ingrese uno correcto.")

    def __str__(self) -> str:
        return f"Paciente: {self.nombre}, Prioridad: {self.prioridad}, Motivo: {self.descripcion_consulta}"

    def __repr__(self) -> str:
        return f"Paciente({self.nombre}, Prioridad: {self.prioridad})"

cola = ColaPrioridad()

paciente1 = Paciente("juan", "fiebre alta y tos")
paciente2 = Paciente("maria", "dolor agudo en el pecho")
paciente3 = Paciente("carlos", "revisión de rutina")
paciente4 = Paciente("ana", "control")
paciente5 = Paciente("ximena", "corazon roto en busca de control")
paciente6 = Paciente("sofia", "control")
paciente7 = Paciente("natalia", "control")


cola.enqueue(paciente1)
cola.enqueue(paciente2)
cola.enqueue(paciente3)
cola.enqueue(paciente4)
cola.enqueue(paciente5)
cola.enqueue(paciente6)
cola.enqueue(paciente7)


print("Cola de pacientes:")
cola.fisrt()

print(cola.buscar_pacientes_pares())