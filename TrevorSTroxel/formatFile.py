"""
This file was used to help format the data dumb found here: https://apocalyptech.com/games/bl3-refs/
Again massive credit goes to apocalyptech, as he did all the heavy lifting, and all I did was format the .sql file.
Though I did have to translate it all of it into MSSQL from MariaDB, so massive credit to this site: https://www.jooq.org/translate/ as it help me translate from one language to another
This has no affect on the program itself, so feel free to delete/use it if you like.
"""


# i = 0
# queue = open(r"SQLQuery2.txt", "a+")

# read = queue.readline()

# for comma in read:
#     if comma == ',':
#          i+=1
#     if i == 2000:
#         print("done")
#         i = 0
#         queue.append(") AS v(id, names)" + "\n" + "SELECT v.id, v.namesFROM (VALUES" + "\n")

# Using readlines()
# file1 = open('SQLQuery2.txt', 'a+')
# Lines = file1.readlines()

# count = 0
# # Strips the newline character
# for line in Lines:
#     count += 1
#     if count == 1000:
#         count = 0
#         print("Writing line")
#         print("Line{}: {}".format(count, line.strip()))
#         file1.writelines(") AS v(id, names)" + "\n" + "SELECT v.id, v.namesFROM (VALUES" + "\n")

# with open("SQLQuery2.txt", "a+") as file_object:

# b_file = open("SQLQuery2 copy.txt", "r")
# place_line = b_file.readlines()

a_file = open((""), "r")
list_of_lines = a_file.readlines()
i = 0
k = 0
for line in list_of_lines:    
    i += 1
    k += 1
    testing = str(line)
    # if k == 1000 and testing.find("dbo.bl3refs"):
    #     copystring = list_of_lines[i-1]
    #     size = len(copystring)
    #     new_line = copystring[:size-2]
    #     list_of_lines[i - 1] = new_line
    #     list_of_lines.insert(i, ") AS v(from_obj, to_obj)" + "\n" + "SELECT v.from_obj, v.to_obj FROM (VALUES" + "\n")
    #     k = 0
    if k == 1000:
        copystring = list_of_lines[i-1]
        size = len(copystring)
        new_line = copystring[:size-2]
        list_of_lines[i - 1] = new_line
        list_of_lines.insert(i, ") AS v(id, names)" + "\n" + "SELECT v.id, v.names FROM (VALUES" + "\n")
        k = 0

a_file = open("", "w+")
a_file.writelines(list_of_lines)
a_file.close()