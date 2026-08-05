def get_records():
    records = []
    n=int(input("Enter the number of crops: "))
    for i in range(n):
        crop=input("Enter the crop name: ")
        try:
            y=float(input("Enter the yield : "))
            if y>0:
                data={
                    "crop": crop,
                    "yield": y
                }
                records.append(data)
            else:
                print("Yield must be a positive number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number for yield.")
    return records
print("Enter first set:")
list1=get_records()
print("Enter second set:")
list2=get_records()
print(list1)
print(list2)
def compare_crops(list1, list2):

    for item1 in list1:
        found = False

        for item2 in list2:

            if item1["crop"] == item2["crop"]:

                difference = item2["yield"] - item1["yield"]

                if difference > 0:
                    print(item1["crop"], "yield increased by", difference)

                elif difference < 0:
                    print(item1["crop"], "yield decreased by", abs(difference))

                else:
                    print(item1["crop"], "yield stayed the same")

                found = True
                break

        if found == False:
            print(item1["crop"], "is missing in second set")
compare_crops(list1, list2)