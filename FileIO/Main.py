import FileIO.StockDriver as stockDriver


def menu():
    loop = False
    driver = None

    while not loop:
        print("==========================================================================")
        print("Welcome to the Stock Exchange!")
        print("==========================================================================")
        print("\nWhat would you like to do?")
        print(
            "1. Add STOCK file\n2. Display STOCK information\n3. Serialize a file\n4. Read a serialised file\n5. Exit")
        choice = str(input("Enter one of the choice > "))
        loop = (choice == "5")
        if choice == "1":
            if driver is None:
                driver = pass_file(driver)
            else:
                overwrite = str(input("File has been written, overwrite?\n[Y/N]\n"))
                if overwrite == "Y" or overwrite == "y":
                    pass_file(driver)
                elif overwrite == "N" or overwrite == "n":
                    print("...Returning to interface...")
                else:
                    print("Y or N, things you see when you have eyes")
        elif choice == "2":
            if driver is not None:
                driver.display()
        elif choice == "3":
            if driver is not None:
                driver.pickling(str(input("Enter the name for the pickled file > ")))
        elif choice == "4":
            driver = stockDriver.unpickling(str(input("Enter the name of the file for unpickling > ")))
        elif choice == "5":
            print("//..Exiting..//")
        else:
            print("Error: Incorrect user input, try again.")
            menu()


def pass_file(driver):
    file = str(input("Enter a valid stock file > "))
    save = str(input("Enter the name of the save file > "))
    if file is None or file == "":
        print("Invalid file import!")
        pass_file(driver)
    else:
        driver = stockDriver.StockDriver(file, save)
        print("File added!")
    return driver

menu()