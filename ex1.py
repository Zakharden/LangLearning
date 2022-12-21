# for i in range(8):
#     print(f"Русаков не съел {i} ёжиков!")

# records = []
# record = {}
# record["Name"]="Rusak"
# record["Age"]=17
# record["Lecture"]="Python way"
# records.append(record)
#
# record["Name"]="Sergei"
# record["Age"]=18
# record["Lecture"]="Python pay"
# records.append(record)
#
#
# print(records)
# for record in records:
#     for key,value in record.items():
#         print(f"{key} - {value} \t")
#     print("\n")

with open("test.txt", "a") as file:
    file.write("\nhello, Zakhar!3")

with open("test.txt", "r") as file:
    for line in file:
        print(line, end= "")
