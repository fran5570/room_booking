from data.storage import Database
import datetime

class ReservationController:
    def __init__(self, db: Database):
        self.conn = db.get_connection()

    def create_reservation(self, user_id: int, room_id: int, date: str, start_time: str, end_time: str):
        cursor = self.conn.cursor()

        # Validación de formato de hora
        try:
            start = datetime.datetime.strptime(f"{date} {start_time}", "%Y-%m-%d %H:%M")
            end = datetime.datetime.strptime(f"{date} {end_time}", "%Y-%m-%d %H:%M")
            if start >= end:
                print("❌ End time must be after start time.")
                return
        except ValueError:
            print("❌ Invalid date or time format.")
            return

        # Verificamos solapamiento
        cursor.execute("""
            SELECT * FROM reservations
            WHERE room_id = ? AND date = ?
              AND (
                    (start_time < ? AND end_time > ?) OR
                    (start_time < ? AND end_time > ?) OR
                    (start_time >= ? AND end_time <= ?)
                  )
        """, (room_id, date, end_time, end_time, start_time, start_time, start_time, end_time))

        conflict = cursor.fetchone()
        if conflict:
            print("❌ This room is already reserved at that time.")
            return

        # Insertamos la reserva
        cursor.execute("""
            INSERT INTO reservations (user_id, room_id, date, start_time, end_time)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, room_id, date, start_time, end_time))
        self.conn.commit()
        print("✅ Reservation created successfully.")

    def list_reservations(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT r.reservation_id, u.name, ro.name, r.date, r.start_time, r.end_time
            FROM reservations r
            JOIN users u ON r.user_id = u.user_id
            JOIN rooms ro ON r.room_id = ro.room_id
            ORDER BY r.date, r.start_time
        """)
        results = cursor.fetchall()
        if results:
            print("\n📋 Reservations:")
            for row in results:
                print(f"[{row[0]}] {row[1]} booked '{row[2]}' on {row[3]} from {row[4]} to {row[5]}")
        else:
            print("⚠️ No reservations found.")

    def list_reservations_by_user(self, user_id: int):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT r.reservation_id, ro.name, r.date, r.start_time, r.end_time
            FROM reservations r
            JOIN rooms ro ON r.room_id = ro.room_id
            WHERE r.user_id = ?
            ORDER BY r.date, r.start_time
        """, (user_id,))
        results = cursor.fetchall()
        if results:
            print("\n📋 Reservations for user:")
            for row in results:
                print(f"[{row[0]}] Room: {row[1]}, Date: {row[2]}, {row[3]} to {row[4]}")
        else:
            print("⚠️ No reservations for this user.")

    def list_reservations_by_room(self, room_id: int):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT r.reservation_id, u.name, r.date, r.start_time, r.end_time
            FROM reservations r
            JOIN users u ON r.user_id = u.user_id
            WHERE r.room_id = ?
            ORDER BY r.date, r.start_time
        """, (room_id,))
        results = cursor.fetchall()
        if results:
            print("\n📋 Reservations for room:")
            for row in results:
                print(f"[{row[0]}] User: {row[1]}, Date: {row[2]}, {row[3]} to {row[4]}")
        else:
            print("⚠️ No reservations for this room.")
