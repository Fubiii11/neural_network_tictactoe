import csv
#This code is just important if you dont use MinMax to filter the boards
def filter_winner(file, output_file):
    filtered_data = []

    with open(file, "r") as f:
        reader = csv.reader(f)
        data = list(reader)

    temp_game = []
    for row in data:
        if len(row) == 1:
            # check winner
            result = int(row[0])
            if result == -1:  # just save games where player -1 wins
                filtered_data.extend(temp_game)
            # empty list if the winner is not player -1
            temp_game = []
        else:
            temp_game.append(row)

    # save filtered data in a new csv file
    with open(output_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(filtered_data)

filter_winner("csv_datei", "filtered_csv_datei.csv")
