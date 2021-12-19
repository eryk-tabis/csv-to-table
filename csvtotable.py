import csv


# neccesary function
def get_row_count():
    with open(file_read_path, 'r') as file_read:
        count = sum(1 for row in file_read)
    return count


file_read_path = input("Enter path to csv file(default in this folder):")
# checking if path ends with csv
if file_read_path[-3:] == "csv":
    file_write_name = input("Enter name file to write table(table.txt as default)") or "table.txt"
    try:
        with open(file_read_path, 'r') as file_read, open(file_write_name, 'w') as file_write:
            delimiter = input("Enter delimiter(',' as default)") or ','
            csv_read = csv.reader(file_read, delimiter=delimiter)
            # function get_row_count() is necessary(it`s not working without it)
            row_count = get_row_count()
            amount_of_rows = int(input("Enter number of rows you want to get (max {})".format(row_count - 1)))
            if row_count < amount_of_rows:
                amount_of_rows = row_count
                print("Can only write {} rows".format(amount_of_rows))
            # flag incrementing as rows are increasing
            f = 0
            file_write.write("<table>")
            file_write.write("\n")
            # going thru rows
            for i in csv_read:
                if f == amount_of_rows + 1:
                    file_write.write("</table>")
                    break
                else:
                    file_write.write("<tr>")
                    # writing header row
                    if f == 0:

                        for j in i:  # going thru row
                            file_write.write("<th>{}</th>".format(j))
                        file_write.write("</tr>")
                        file_write.write("\n")
                    # writing normal row
                    else:
                        # going thru row
                        for j in i:
                            file_write.write("<td>{}</td>".format(j))
                        file_write.write("</tr>")
                        file_write.write("\n")

                f += 1
    except FileNotFoundError:
        print("File not found")
else:
    print("Something wrong with file path")
