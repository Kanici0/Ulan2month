def bubble_sort(gema):
    n = len(gema)
    for i in range(n):
        for j in range(0, n-i-1):
            if gema[j] >gema[j+1]:
                gema[j],gema[j+1] = gema[j+1], gema[j]


if __name__ == "__main__":
    gema= [64, 34, 25, 12, 22, 11, 90]
    print("Исходный массив:", gema)
    bubble_sort(gema)
    print("Отсортированный массив:",gema)
