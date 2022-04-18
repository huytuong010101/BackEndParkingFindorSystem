from peewee import SqliteDatabase

db = SqliteDatabase('database.db')

if __name__ == "__main__":
    # Create table
    from models import Node, Park, ParkRecord
    db.connect()
    db.create_tables([Node, Park, ParkRecord])
    # Fake data
    node = Node.create(node_name="Công viên 26/3", address="Đường Nguyễn Tri Phương, ĐN", token="123123123", long=0, lat=0)
    park1 = Park.create(
        park_name="Trước công viên 26/3",
        address="Nguyễn Tri Phương",
        long=0,
        lat=0,
        node=node,
    )
    
    park2 = Park.create(
        park_name="Sau công viên 26/3",
        address="Nguyễn Tri Phương",
        long=0,
        lat=0,
        node=node,
    )
    # Close db
    db.close()