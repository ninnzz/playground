import csv


SELECTED = ["neilibo@gmail.com","vivre214@gmail.com","ardie@thinkingmachin.es","argeoalecha@petronas.com.my","phaophaoespina@gmail.com","tai271828@gmail.com","vaibhavs10@gmail.com","neequole@gmail.com","aniruddha@adhikary.net","tedmathewdelacruz@gmail.com","paul.depaula@pantheon.io","suzanne.lee@analytiksinc.com","tom.dyson@torchbox.com","jacob@jacobian.org","bengkeatliew@gmail.com","ronen.baram@oracle.com","aravind.putrevu@elastic.co","zhu.sun@shopee.com","jairus.g.jimenez@accenture.com","lai.man.sung@accenture.com"]


def read_file(csv_path: str) -> list:
	"""Read the main csv file of speakers"""

	short_list = []
	to_send = [("name", "email", "select")]

	with open(csv_path) as csvfile:
		reader = csv.reader(csvfile, delimiter=',')

		cols = next(reader)
		
		for row in reader:
			if row[2] in short_list:
				continue

			short_list.append(row[2])

			if row[2] in SELECTED:
				to_send.append((row[1], row[2], 1))
			else:
				to_send.append((row[1], row[2], 0))

	return to_send


filename = "cfp.csv"
names = read_file(filename)

for i in names:
	print(f"{i[0]}\t{i[1]}\t{i[2]}")