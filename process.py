import wmi
import subprocess
import os

class Process:

    def getAllProc(self):
        try:
            output = os.popen('wmic process get description, processid').read()

            return output
        except:
            return "There's been an error!"

    def printAllProc(self):
        print()
        print(self.getAllProc())

    def searchProc(self, procName):
        allProc = self.getAllProc().lower()
        contains = allProc.find(procName)

        if contains > 0:
            return True
        else:
            return False

class Main:

    if __name__ == "__main__":
        process = Process()
        
        choice = int(input("Please choose one from below:\n1- Display all process\n2- Search a process\n--> "))
        
        if choice == 1:
            process.printAllProc()
        elif choice == 2:
            procToSearch = input("\nPlease enter the name of the process: ")
            procToSearch = procToSearch.replace(" ", "").lower()

            found = process.searchProc(procToSearch)

            if found:
                print(f"Process '{procToSearch}' is running!\n")
            else:
                print(f"Process '{procToSearch}' is not running!\n")
        else:
            print("\nPlease enter a valid choice!")
