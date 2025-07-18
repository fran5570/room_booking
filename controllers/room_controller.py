from data.storage import Database

class RoomController:
    def __init__(self, db: Database):
        self.conn = db.get_connection()

    def create_room(self, name: str, capacity: int):
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO rooms (name, capacity) VALUES (?, ?)", (name, capacity))
            self.conn.commit()
            print("✅ Room created successfully.")
        except Exception as e:
            print("❌ Error creating room:", e)

    def list_rooms(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM rooms")
        rooms = cursor.fetchall()
        if rooms:
            print("\n📋 List of rooms:")
            for room in rooms:
                print(f"[{room[0]}] {room[1]} - Capacity: {room[2]}")
        else:
            print("⚠️ No rooms found.")

    def get_room_by_id(self, room_id: int):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM rooms WHERE room_id = ?", (room_id,))
        room = cursor.fetchone()
        if room:
            return room
        else:
            print("⚠️ Room not found.")
            return None
