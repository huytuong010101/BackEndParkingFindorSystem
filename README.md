# Parking Findor System [BackEnd]
```
PBL5 - Parking Findor System
- Member: TuongNH, VyHV, HanLHN, PhuongTT
- Full version:
  - Raspberry: https://github.com/huytuong010101/PBL5-ParkingFinder-Raspberry
  - FrontEnd: https://github.com/pphuongdut/parkingfindor
- Demo: https://youtu.be/aqc-QID5GfQ
```
## Install
- Clone this repository
- `pip install -r requirements.txt`
## Init database
- `cd src`
- `export PYTHONPATH=$(pwd)`
- `python database/connection.py` (Just tun first time to init database and fake data)
## How to run?
```
make run [PORT=8080] [HOST=127.0.0.1]
```
- Go to `host:port/docs` to testing API

