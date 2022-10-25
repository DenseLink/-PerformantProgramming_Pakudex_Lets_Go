#from pakuri import Pakuri
import pakuri
import sys


def main():

    q = 0
    pakumon_dict = dict()
    pakumon_object_list = []
    print("Welcome to Pakudex: Let's Go!")
    while q != 6:
        try:

            print("\nPakudex Main Menu")
            print("-----------------")
            print("1. List Pakuri")
            print("2. Show Pakuri")
            print("3. Add Pakuri")
            print("4. Remove Pakuri")
            print("5. Change Pakuri Level")
            print("6. Exit\n")
            #print("What would you like to do?")
            q = int(input("What would you like to do? "))
            if not 1 <= q < 7:
                q = 0
                raise ValueError
        except ValueError:
            q = 0
            print("\nUnrecognized menu selection!")
        if q == 6:
            print("\nThanks for using Pakudex: Let's Go! Bye!")
            break
        elif q == 1:
            if len(pakumon_object_list) > 0:
                print("\nPakuri in Pakudex:")
                i = 1
                for key, value in sorted(pakumon_dict.items()):

                    v = pakumon_dict[key][1]
                    #print(v)
                    print(str(i) + ". " + str(key) + " (" + str(pakumon_dict[key][0]) + ", level " + str(pakumon_dict[key][1]) + ")")
                    i = i + 1
            else:
                print("\nNo Pakuri in Pakudex yet!")
        elif q == 2:
            x = input("\nEnter the name of the Pakuri to display: ")
            if x in pakumon_dict.keys():
                print("\nName: " + str(x))
                print("Species: " + str(pakumon_dict[x][0]))
                print("Level: " + str(pakumon_dict[x][1]))
                print("CP: " + str(pakumon_dict[x][2]))
                print("HP: " + str(pakumon_dict[x][3]))
            else:
                print("Error: No such Pakuri!")
        elif q == 3:
            print("\nPakuri Information")
            print("------------------")
            x = input("Name: ")
            if x not in pakumon_dict.keys():
                y = input("Species: ")
                while True:
                    try:
                        z = -1
                        while z < 0 or z > 50:
                            z= int(input("Level: "))
                            if z < 0:
                                print("Level cannot be negative.")
                            elif z > 50:
                                print("Maximum level for Pakuri is 50.")
                        pakumon = pakuri.Pakuri(x, y, z)
                        getcp = pakumon.cp
                        gethp = pakumon.hp
                        pakumon_list = [y, z, getcp, gethp]
                        pakumon_dict[x] = pakumon_list
                        pakumon_object_list.append(pakumon)
                        print("\nPakuri " + str(x) + " (" + str(pakumon_dict[x][0]) + ", level " + str(pakumon_dict[x][1]) + ") added!")
                        break
                    except ValueError as error:
                        print("Invalid level!")
            else:
                print("Error: Pakudex already contains this Pakuri!")
        elif q == 4:
            x = input("\nEnter the name of the Pakuri to remove: ")
            if x in pakumon_dict.keys():
                pakumon_dict.pop(x)

                for place, values in enumerate(pakumon_object_list):
                    if pakumon_object_list[place].name == x:
                        del pakumon_object_list[place]
                print("Pakuri " + x + " removed.")
            else:
                print("Error: No such Pakuri!")
        elif q == 5:
            x = input("\nEnter the name of the Pakuri to change: ")
            if x in pakumon_dict.keys():
                try:
                    y = -1
                    while y < 0 or y > 50:
                        try:
                            try:
                                y = int(input("Enter the new level for the Pakuri: "))
                            except:
                                print("Invalid level!")
                                continue
                            if y < 0:
                                raise ValueError
                            elif y > 50:
                                raise Exception

                        except ValueError:
                            print("Level cannot be negative.")
                        except Exception as error:
                            print("Maximum level for Pakuri is 50.")

                    for place, values in enumerate(pakumon_object_list):
                        if pakumon_object_list[place].name == x:
                            test = pakumon_object_list[place]
                            test.level = y

                            pakumon_list = [pakumon_object_list[place].species, pakumon_object_list[place].level, pakumon_object_list[place].cp, pakumon_object_list[place].hp]
                            pakumon_dict[x] = pakumon_list

                except ValueError as error:
                    print("Invalid level!")
            else:
                print("Error: No such Pakuri!")




if __name__ == "__main__":
    main()