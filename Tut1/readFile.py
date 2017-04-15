# 'r' = read ; 'w' = write; a = "append"
# 'r+' = reads+write
# 'w+' = overwrites existing +reads and writes
# 'a+' = appends and reads
fle = open("text.txt",'r')
content = fle.read()
print(content)

# content.seek(0) resets the pointer to the beginning
fle.seek(0)
content2 = fle.readline()
print("content2 "+content2)

fle.seek(0)
content3 = fle.readlines()
content3 = [i.rstrip("\n") for i in content3]
print(content3)
fle.close()

writer = open("writenFile.txt", 'w')
writer.write("this is the fisrt line"+"\n")
writer.close()

# to append more lines to the text file
writer = open("writenFile.txt", 'a')
writer.write('line x')
writer.close()

# open things "with"
with open("writenFile.txt","a+") as files:
    files.seek(0)
    stuff = files.read()
    files.write("\nHello")
