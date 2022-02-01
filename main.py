"""Ödev1:Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden
([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir."""

mainList = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]

def flat(inputList):
    newList = []
    for i in inputList:
        if type(i) != list:
            newList.append(i)
        else:
            newList.extend(flat(i))
    return newList
print(flat(mainList))


"""Ödev2:Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki 
elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün"""

mainList2 = [[1, 2], [3, 4], [5, 6, 7]]
for z in range(len(mainList2)):
    mainList2[z].reverse()
    mainList2[z][::-1]

print(mainList2[::-1])

