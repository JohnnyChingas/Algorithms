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
            print "j = %d, min = %d"%(j,min)
            print "is %s < %s?"%(list[j],list[min])
            if list[j] < list[min]:
                print "%s is smaller than %s"%(list[j],list[min])
                min = j
            else:
                print "No"

        list[min], list[i] = list[i], list[min]
        print "let's swap ind %d for ind %d"%(i,min)
        print list
        print "\n"

if __name__ == "__main__":
    main()
