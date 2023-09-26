k=0#счётчик пятёрок
ocenki=input().split()
for i in ocenki:
    if i=='5':
        k+=1
print(ocenki,(k/len(ocenki)*100))