try:
    fw = open("D:\python_file\sample.txt", "a")
    fw.writelines(["\nabc","\nxyz"])
    fw.close()


    fp = open("D:\python_file\sample.txt","r")
    #to read the file we have inbuilt function called read() function, readLine() and readLines()
    print(fp.read())
    fp.close()
except FileNotFoundError:
    print("File not found please check file name again")