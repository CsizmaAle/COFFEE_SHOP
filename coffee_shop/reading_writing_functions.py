import csv
import meniu_functions as mf

def readingFile(in_file):
    reader=csv.reader(in_file)
    header=next(reader)
    List=[line for line in reader]
    return header, List

def readingIngr(in_file):
    reader=csv.reader(in_file)
    header=next(reader)
    List=[]
    for line in reader:
        dict={
            "name":line[0],
            "milk":line[1],
            "coffee":line[2],
            "water":line[3],
            "caramel":line[4],
            "vanilla": line[5] 
        }
        List.append(dict)
    return header, List

def writingFiles(out_file, header, List):
    writer=csv.writer(out_file)
    writer.writerow(header)
    writer.writerows(List)

def print_stock(header, List):
    for x in header:
        print(x, end="     ")
    print("")
    for line in List:
        space=0
        for item in line:
            space=space+len(item)
            if space<4:
                
                print(item.rjust(space), end="")
            else:
                print(item.rjust(14), end="")
        print("")

def read_meniu(meniuFile, ingredients):
    meniuHeader, meniuList= readingFile(meniuFile)
    for line in meniuList:
        if line[2]==" ":
            line[2]=str(mf.quantity_calculate(line[1],ingredients))
            line[2]+='ml'
       
    return meniuHeader, meniuList

def print_table(header, List):
    for x in header:
        print(x, end="     ")
    print("")
    for line in List:
        space=0
        for item in line:
            space=space+len(item)
            if space<4:
                
                print(item.rjust(space), end="")
            else:
                print(item.rjust(14), end="")
        print("")

