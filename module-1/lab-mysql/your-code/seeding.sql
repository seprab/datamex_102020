use car_dealership;
DELETE FROM cars;
DELETE FROM customer;
DELETE FROM invoices;
DELETE FROM salesperson;
INSERT INTO cars VALUES
	("9651618", "Volkswagen","Tiguan", "2019", "Blue"),
	("2993448", "Peugeot","Rifter", "2019", "Red"),
	("5925945", "Ford","Fusion", "2018", "White"),
    ("1512356", "Toyota","RAV4", "2018", "Silver"),
    ("9859629", "Volvo","V60", "2019", "Gray"),
    ("5159293", "Volvo","V60 Cross Country", "2019", "Gray");

INSERT INTO customer VALUES
	("10001", "Pablo","346361", "", "Paseo de la Chopera, 14", "Madrid", "Madrid", "Spain", "28045"),
	("20001", "Abraham","130590", "", "120 SW 8th St", "Miami", "Florida", "United States", "28045"),
	("30001", "Napoléon","331797", "", "40 Rue du Colisée", "Paris", "Île-de-France", "France", "28045");

INSERT INTO salesperson VALUES
	("00001", "Petey Cruiser", "Madrid"),
    ("00002", "Anna Sthesia", "Barcelona"),
    ("00003", "Paul Molive", "Berlin"),
    ("00004", "Gail Forcewind", "Paris"),
    ("00005", "Paige Turner", "Mimia"),
    ("00006", "Bob Frapples", "Mexico City"),
    ("00007", "Walter Melon", "Amsterdam"),
    ("00008", "Shonda Leer", "São Paulo");

INSERT INTO invoices VALUES
	("852399038", "2018-08-22", "9651618", "10001", "00001"),
    ("731166526", "2018-08-22", "9651618", "20001", "00002"),
    ("271135104", "2018-08-22", "9651618", "30001", "00003");