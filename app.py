from Helper import Helper
from Settings import CSV_END_POINT

def main():
    table = Helper.GenerateListOfBytes()
    if(len(table) > 1):
        Helper.SaveToCSV(table, destination = CSV_END_POINT)
        print("Done")

if(__name__ == '__main__'):
    main()





