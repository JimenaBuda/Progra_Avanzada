import pickle
import datetime

# Definir la clase para el manejo de la empresa WeWork LTI
class WeWorkLTI:
    def __init__(self):
        self.users = []
        self.rooms = []
        self.reservations = []

    def save_data(self):
        with open('wework_data.pkl', 'wb') as file:
            pickle.dump([self.users, self.rooms, self.reservations], file)

    def load_data(self):
        try:
            with open('wework_data.pkl', 'rb') as file:
                self.users, self.rooms, self.reservations = pickle.load(file)
        except FileNotFoundError:
            pass

    def register_user(self):
        name = input("Ingrese el nombre del usuario: ")
        email = input("Ingrese el correo electrónico del usuario: ")

        if self.check_user_exist(email):
            print("\nUSUARIO EXISTENTE")
        else:
            self.users.append({"name": name, "email": email})
            print("\nUsuario registrado exitosamente.")

    def modify_user(self):
        email = input("Ingrese el correo electrónico del usuario que desea modificar: ")
        if self.check_user_exist(email):
            new_name = input("Ingrese el nuevo nombre del usuario: ")
            index = self.get_user_index(email)
            self.users[index]["name"] = new_name
            print("\nUsuario modificado exitosamente.")
        else:
            print("\nEl usuario no está registrado.")

    def delete_user(self):
        email = input("Ingrese el correo electrónico del usuario que desea eliminar: ")
        if self.check_user_exist(email):
            index = self.get_user_index(email)
            del self.users[index]
            print("\nUsuario eliminado exitosamente.")
        else:
            print("\nEl usuario no está registrado.")

    def register_room(self):
        room_name = input("Ingrese el nombre de la sala: ")
        capacity = input("Ingrese la capacidad de la sala: ")
        self.rooms.append({"room_name": room_name, "capacity": capacity})
        print("\nSala registrada exitosamente.")

    def modify_room(self):
        room_name = input("Ingrese el nombre de la sala que desea modificar: ")
        if self.check_room_exist(room_name):
            new_name = input("Ingrese el nuevo nombre de la sala: ")
            index = self.get_room_index(room_name)
            self.rooms[index]["room_name"] = new_name
            print("\nSala modificada exitosamente.")
        else:
            print("\nLa sala no está registrada.")

    def delete_room(self):
        room_name = input("Ingrese el nombre de la sala que desea eliminar: ")
        if self.check_room_exist(room_name):
            index = self.get_room_index(room_name)
            del self.rooms[index]
            print("\nSala eliminada exitosamente.")
        else:
            print("\nLa sala no está registrada.")

    def register_reservation(self):
        print("Disponibles:")
        for i, room in enumerate(self.rooms):
            print(f"{i + 1}. {room['room_name']} - Capacidad: {room['capacity']}")

        room_choice = int(input("Seleccione el número de la sala a reservar: ")) - 1
        date = input("Ingrese la fecha de la reserva (YYYY-MM-DD): ")

        if self.validate_reservation_date(date):
            self.reservations.append({"room": self.rooms[room_choice]["room_name"], "date": date})
            print("\nReserva realizada exitosamente.")

    def delete_reservation(self):
        if not self.reservations:
            print("\nNo hay reservaciones registradas.")
        else:
            room = input("Ingrese el nombre de la sala de la reserva que desea eliminar: ")
            date = input("Ingrese la fecha de la reserva (YYYY-MM-DD): ")

            for reservation in self.reservations:
                if reservation["room"] == room and reservation["date"] == date:
                    self.reservations.remove(reservation)
                    print("\nReserva eliminada exitosamente.")
                    return

            print("\nNo se encontró la reserva.")

    def show_all_reservations(self):
        if not self.reservations:
            print("\nNo hay reservaciones registradas.")
        else:
            print("Todas las reservaciones:")
            for reservation in self.reservations:
                print(f"Sala: {reservation['room']} - Fecha: {reservation['date']}")

    def check_user_exist(self, email):
        for user in self.users:
            if user["email"] == email:
                return True
        return False
      
    def check_room_exist(self, room_name):
        for room in self.rooms:
            if room["room_name"] == room_name:
                return True
        return False

    def get_user_index(self, email):
        for i, user in enumerate(self.users):
            if user["email"] == email:
                return i
        return -1

    def get_room_index(self, room_name):
        for i, room in enumerate(self.rooms):
            if room["room_name"] == room_name:
                return i
        return -1

    # Función para validar si la reserva se hace con al menos 2 días de anticipación
    def validate_reservation_date(self, date):
        today = datetime.date.today()
        reservation_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        if (reservation_date - today).days < 2:
            print("\nAVISO: Por favor, haga la reserva con al menos 2 días de anticipación.")
            return False
        return True

# Función principal del menú
def main():
    wework = WeWorkLTI()
    wework.load_data()

    while True:
        print("\nBienvenido a WeWork LTI")
        print("******************************")
        print("1. Registro de Usuario")
        print("2. Modificar Usuario")
        print("3. Eliminar Usuario")
        print("4. Registro de Sala")
        print("5. Modificar Sala")
        print("6. Eliminar Sala")
        print("7. Registro de Reservación")
        print("8. Eliminar Reservación")
        print("9. Mostrar Todas las Reservaciones")
        print("10. Salir")
        print("******************************")

        choice = input("Ingrese el número de su elección: ")

        if choice == '1':
            wework.register_user()
            wework.save_data()
        elif choice == '2':
            wework.modify_user()
            wework.save_data()
        elif choice == '3':
            wework.delete_user()
            wework.save_data()
        elif choice == '4':
            wework.register_room()
            wework.save_data()
        elif choice == '5':
            wework.modify_room()
            wework.save_data()
        elif choice == '6':
            wework.delete_room()
            wework.save_data()
        elif choice == '7':
            wework.register_reservation()
            wework.save_data()
        elif choice == '8':
            wework.delete_reservation()
            wework.save_data()
        elif choice == '9':
            wework.show_all_reservations()
        elif choice == '10':
            print("¡GRACIAS POR PREFERIR WeWork LTI!")
            break
        else:
            print("Por favor, ingrese una opción válida.")

main()