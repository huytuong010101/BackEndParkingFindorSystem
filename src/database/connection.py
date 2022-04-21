from peewee import SqliteDatabase
from datetime import datetime

db = SqliteDatabase("database.db")

if __name__ == "__main__":
    # Create table
    from models import Node, Park, ParkRecord

    db.connect()
    db.create_tables([Node, Park, ParkRecord])
    # Fake data
    node = Node.create(
        node_name="Công viên 26/3",
        address="Đường Nguyễn Tri Phương, ĐN",
        token="123123123",
        long=0,
        lat=0,
    )
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

    record1 = ParkRecord.create(
        park=park1,
        time=datetime.now(),
        image="https://i.imgur.com/qZImWfa.png",
        num_of_empty_space=2,
    )

    record2 = ParkRecord.create(
        park=park2,
        time=datetime.now(),
        image="https://i.imgur.com/5xwsO1w.png",
        num_of_empty_space=5,
    )

    record3 = ParkRecord.create(
        park=park2,
        time=datetime.now(),
        image="https://i.imgur.com/5xwsO1w.png",
        num_of_empty_space=6,
    )
    # Close db
    db.close()
