try:
    fw = open(r"D:\python_file\test.txt", "a")
    # to write the content into file we use write() function.
    fw.write("Java is easy and good programming language.")
    fw.close()
    fp = open(r"D:\python_file\test.txt", "r")
    # to read the file we use read() function, readLine() and readLines()
    print(fp.read())
    fp.close()
except FileNotFoundError:
    print("File not found please check the file name")