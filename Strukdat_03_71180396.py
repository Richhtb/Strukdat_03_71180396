input1= input("masukkan input kalimat pertama: ")
input2= input("masukkan input kalimat yang kedua: ")

input1= input1.lower()
input1= input1.split(" ")
n = 0
for i in input1:
    # print(i)
    if i == input2:
        n += 1 
# print(input1)
print(n)
# print(input2)