import mysql.connector as ms
mycon=ms.connect(host='localhost', user='root', password='root')
a=mycon.cursor()
a.execute("create database if not exists PROJECT")
a.execute("use PROJECT")
a.execute("""CREATE TABLE IF NOT EXISTS PROJECT.items (
  `ItemId` char(6) NOT NULL,
  `ItemName` varchar(50) DEFAULT NULL,
  `Price` int(10) DEFAULT NULL,
  `Type` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`ItemId`)
)""")
a.execute("insert into project.items values('I001', 'Masala Dosa', 70, 'Food')")
a.execute("insert into project.items values('I002', 'Veg Chowmein', 80, 'Food')")
a.execute("insert into project.items values('I003', 'Tandoori Paneer', 100, 'Food')")
a.execute("insert into project.items values('I004', 'Veg Fried Rice', 100, 'Food')")
a.execute("insert into project.items values('I005', 'Spring Roll', 60, 'Food')")
a.execute("insert into project.items values('I006', 'Pasta', 80, 'Food')")
a.execute("insert into project.items values('I007', 'Paneer Chilly', 90, 'Food')")
a.execute("insert into project.items values('I008', 'Gobi Manchurian', 90, 'Food')")
a.execute("insert into project.items values('I009', 'Mushroom Chilly', 90, 'Food')")
a.execute("insert into project.items values('I010', 'Pasta', 80, 'Food')")
a.execute("insert into project.items values('I011', 'Water', 30, 'Drinks')")
a.execute("insert into project.items values('I012', 'Coffee Americano', 60, 'Drinks')")
a.execute("insert into project.items values('I013', 'Coffee Cappuccino', 75, 'Drinks')")
a.execute("insert into project.items values('I014', 'Coffee Espresso', 80, 'Drinks')")
a.execute("insert into project.items values('I015', 'Tea', 30, 'Drinks')")
a.execute("insert into project.items values('I016', 'Rasgulla', 35, 'Dessert')")
a.execute("insert into project.items values('I017', 'Laddoo', 30, 'Dessert')")
a.execute("insert into project.items values('I018', 'Donut', 30, 'Dessert')")
a.execute("insert into project.items values('I019', 'Almond Kulfi', 80, 'Dessert')")
a.execute("insert into project.items values('I020', 'Burfi', 30, 'Dessert')")
mycon.commit()
