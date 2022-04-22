from peewee import SqliteDatabase
from datetime import datetime

db = SqliteDatabase("database.db")

if __name__ == "__main__":
    # Create table
    from models import Node, Park, ParkRecord

    db.connect()
    db.create_tables([Node, Park, ParkRecord])
    # Fake data
    node1 = Node.create(
        node_name="Công viên 26/3",
        address="Đường Nguyễn Tri Phương, ĐN",
        token="123123123",
        long=108.2036781,
        lat=16.064814,
    )
    park1 = Park.create(
        park_name="Trước công viên 26/3",
        address="Nguyễn Tri Phương",
        long=108.2023015,
        lat=16.0655712,
        node=node1,
    )

    park2 = Park.create(
        park_name="Sau công viên 26/3",
        address="Nguyễn Tri Phương",
        long=108.2036781,
        lat=16.064814,
        node=node1,
    )

    node2 = Node.create(
        node_name="Trường đại học Bách Khoa ĐN",
        address="54 Nguyễn Lương Bằng, Đà Nẵng",
        token="123123123",
        long=108.1477034,
        lat=16.0739283,
    )
    park3 = Park.create(
        park_name="Nhà xe Giảng viên - Trường đại học Bách Khoa ĐN",
        address="54 Nguyễn Lương Bằng, Đà Nẵng",
        long=108.1477034,
        lat=16.0739283,
        node=node2,
    )
    
    node3 = Node.create(
        node_name="Siêu thị BigC",
        address="Đường Hùng Vương",
        token="123123123",
        long=108.2112561,
        lat=16.0668683,
    )
    park4 = Park.create(
        park_name="Siêu thị BigC",
        address="Đường Hùng Vương",
        long=108.2112561,
        lat=16.0668683,
        node=node3,
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
        park=park3,
        time=datetime.now(),
        image="https://i.ibb.co/VJQ2RM0/1.png",
        num_of_empty_space=1,
    )

    record4 = ParkRecord.create(
        park=park4,
        time=datetime.now(),
        image="https://i.ibb.co/19dHy6z/2.png",
        num_of_empty_space=4,
    )


    # Close db
    db.close()
