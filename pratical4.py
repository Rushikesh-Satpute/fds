import array as a 
def Selection_Sort(m,n):
    for i in range(len(m)):
        min_idx = i
        for j in range(i + 1, len(m)):
            if m[min_idx] > m[j]:
                min_idx = j
                m[i], m[min_idx] = m[min_idx], m[i]
    print("Marks of students after performing Selection Sort on the list : ")
    for i in range(len(m)):
        print("%.2f"%m[i])
def bubble_sort(a,n):

    for p in range (1,n):
        for q in range (0,n-p):
            if(a[q]>a[q+1]):
                temp =a[q]
                a[q]=a[q+1]
                a[q+1]=temp
    print("marks after bubble sort :")
    for n in range (0,n):
        print("%.2f"%a[n])
def main():
    arr=a.array('f',[])
    l=int(input("enter number of student :"))
    print ("enetr marks of student")
    for i in range(0,l):
        print("student ",i+1)
        e=float(input())
        arr.append(e)
    print("----------students------------")
    
    for n in range (0,l):
        print("%.2f"%arr[n])
    flag=1;
    while True:
        print("Menu:")
        print("1. Selection Sort of the marks")
        print("2. Bubble Sort of the marks")
        print("3. top 5 student")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            Selection_Sort(arr,l)

        elif choice == 2:
            bubble_sort(arr,l)

        elif choice == 3:
            print("top 5 students :")
            for k in range (l-1,l-6,-1):
                print("%.2f" %arr[k])

        elif choice == 4:
        
            break

        else:
            print("Invalid choice. Please enter a valid option.")
            
    
    
   
    
    
main()

