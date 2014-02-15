# Implementing Selection Sort to better understand it

def main():
    list = [ 'S', 'E', 'L', 'E', 'C', 'T', 'I', 'O', 'N', 'S', 'O', 'R', 'T']
    selection_sort(list)
    print list

def selection_sort(list):
    n = len(list)
    for i in xrange(len(list)):
        print list
        min = i;
        for j in xrange(i+1,n):
            if list[j] < list[min]:
                min = j
        list[min], list[i] = list[i], list[min]

if __name__ == "__main__":
    main()
