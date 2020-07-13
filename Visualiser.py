import pygame
import random
pygame.font.init()

global num
num=100
white=(255,255,255)
light_blue=(0,76,153)
blue=(0,51,102)
red = (200,0,0)
green = (0,200,0)
light_red = (255,0,0)
light_green = (0,255,0)
fnt = pygame.font.SysFont("comicsans", 20)
width = 900
length = 600
array =[0]*num            
arr_clr =[(0,204,204)]*num  
clr_ind = 0
clr =[(0,204,204) ,(153,0,153) ,blue,(51,0,51)] 


pygame.init()
icon=pygame.image.load('sort.png')
back1=pygame.image.load('back2.jpg')
pygame.display.set_icon(icon)       
screen = pygame.display.set_mode((900,650))    
pygame.display.set_caption('Sorting Visualiser')            

def top():
    fnt1 = pygame.font.SysFont("comicsans", 40)
    txt = fnt1.render(" SORTING VISUALISER ", 1, blue) 
    screen.blit(txt, (290, 30)) 
    pygame.draw.line(screen, blue,(0, 95), (900, 95), 6)


def button(msg,x,y,w,h,ic,ac,fc,action=None):    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        
        if click[0] == 1 and action != None:
            generate_arr()
            action() 
        
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    textSurf = fnt.render(msg, 1, fc)
    textRect=textSurf.get_rect()
    textRect.center = ( round(x+(w/2)), round(y+(h/2)) )
    screen.blit(textSurf, textRect)

def draw(s): 
    global num
    txt = fnt.render("PRESS 'ENTER' TO START ", 1, blue)  
    screen.blit(txt, (50, 10)) 
    
    txt1 = fnt.render("PRESS 'R' TO GENERATE NEW ARRAY ",1, blue) 
    screen.blit(txt1, (550, 10))

    fnt1 = pygame.font.SysFont("comicsans", 40)
    txx = fnt1.render("VISUALISATION OF "+s+" SORT", 1, blue)  
    screen.blit(txx, (220,50))

    element_width =(width-150)//num
    boundry_arr = 900 // num
    boundry_grp = 550 // 100
    pygame.draw.line(screen, blue,(0, 95), (900, 95), 6) 
    #for i in range(1, 100): 
        #pygame.draw.line(screen,(224, 224, 224),(0, boundry_grp * i + 100),(900, boundry_grp * i + 100), 1) 
      
   
    for  i in range(1, num): 
        pygame.draw.line(screen, arr_clr[i],(boundry_arr * i, 650-array[i]*(boundry_grp)),(boundry_arr * i,  650),element_width)  


def clrchange(array,n):
    for i in range(0,n):
        arr_clr[i]=clr[2]

def generate_arr():
    global num 
    for i in range(1, num): 
        arr_clr[i]= clr[0]                  
        array[i]= random.randrange(1, 100) 
generate_arr()

def refill(s): 
    screen.fill((255, 255, 255)) 
    draw(s) 
    pygame.display.update() 
    pygame.time.delay(10) 
    
def MergeSort(array, l, r): 
    mid =(l + r)//2
    if l<r: 
        MergeSort(array, l, mid) 
        MergeSort(array, mid + 1, r) 
        merge(array, l, mid,mid + 1, r) 
    
def merge(array, x1, y1, x2, y2): 
    i = x1 
    j = x2 
    temp =[] 
    pygame.event.pump()  
    while i<= y1 and j<= y2: 
        arr_clr[i]= clr[1] 
        arr_clr[j]= clr[1] 
        refill("MERGE") 
        arr_clr[i]= clr[0] 
        arr_clr[j]= clr[0] 
        if array[i]<array[j]: 
                temp.append(array[i]) 
                i+= 1
        else: 
                temp.append(array[j]) 
                j+= 1
    while i<= y1: 
        arr_clr[i]= clr[1] 
        refill("MERGE") 
        arr_clr[i]= clr[0] 
        temp.append(array[i]) 
        i+= 1
    while j<= y2: 
        arr_clr[j]= clr[1] 
        refill("MERGE") 
        arr_clr[j]= clr[0] 
        temp.append(array[j]) 
        j+= 1
    j = 0       
    for i in range(x1, y2 + 1):   
        pygame.event.pump()   
        array[i]= temp[j] 
        j+= 1
        arr_clr[i]= clr[2] 
        refill("MERGE") 
        if y2-x1 == len(array)-2: 
            arr_clr[i]= clr[2] 
        else:     
            arr_clr[i]= clr[0]     
            
def partition(array,low,high): 
    i = ( low-1 )         
    pivot = array[high]  
    pygame.event.pump()   
    for j in range(low , high):
        if   array[j] < pivot: 
            i = i+1 
            array[i],array[j] = array[j],array[i] 
    array[i+1],array[high] = array[high],array[i+1]
    refill("QUICK")
    return  i+1 
            
def QuickSort(array,low,high): 
    if low < high: 
        pi = partition(array,low,high) 
        QuickSort(array, low, pi-1) 
        QuickSort(array, pi+1, high)  
        
def SelectionSort(array,l,n):
    n=n+1
    for i in range(n):
        min_idx = i 
        for j in range(i+1, n): 
            if array[min_idx] > array[j]: 
                min_idx = j
            pygame.event.pump() 
        array[i], array[min_idx] = array[min_idx], array[i]
        arr_clr[min_idx]=clr[3]
        arr_clr[i]=clr[1]
        refill("SELECTION")
        arr_clr[min_idx]=clr[1]
        arr_clr[i]=clr[2]

def heapify(array, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1    # left = 2*i + 1 
    r = 2 * i + 2    # right = 2*i + 2 

    # See if left child of root exists and is greater than root 
    if l < n and array[i] < array[l]: 
        largest = l 

    # See if right child of root exists and is greater than root 
    if r < n and array[largest] < array[r]: 
        largest = r 

    # Change root, if needed 
    if largest != i: 
        array[i],array[largest] = array[largest],array[i] # swap 

        # Heapify the root. 
        heapify(array, n, largest) 

def HeapSort(array,l,n): 
    n=n+1

    # Build a maxheap. 
    for i in range(n//2 - 1, -1, -1): 
        pygame.event.pump()
        heapify(array, n, i) 

    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        array[i], array[0] = array[0], array[i] # swap
        arr_clr[i]=clr[3]
        arr_clr[0]=clr[1]
        refill("HEAP")
        arr_clr[i]=clr[2]
        arr_clr[0]=clr[0]
        heapify(array, i, 0) 

def InsertionSort(array,l,n): 
    for i in range(1, n+1):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            pygame.event.pump()

            array[j + 1] = array[j] 
            j -= 1
            arr_clr[j+1]=clr[1] 
            refill("INSERTION")
            arr_clr[j+1]=clr[0]
        array[j + 1] = key
        arr_clr[i]=clr[2]
        #refill()
        #arr_clr[i]=clr[0]
             

def BubbleSort(array,l,n):
    n=n+1;
    count=0
    for i in range(0,n): 
        for j in range(0,n - i - 1):
            if array[j] > array[j + 1]:
                count+=1
                array[j],array[j+1]=array[j+1],array[j]
                pygame.event.pump()
            arr_clr[j]=clr[1]              
            arr_clr[j+1]=clr[3]
            refill("BUBBLE")
            arr_clr[j]=clr[0]
            arr_clr[j+1]=clr[2]                           



def ex():
    pygame.quit()
    quit()
    sys.exit()

def bub():
    global pause
    crashed = False
    while not crashed:
        for event in pygame.event.get():   
            if event.type == pygame.QUIT:           
                crashed=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: 
                    generate_arr() 
                if event.key == pygame.K_RETURN:
                    BubbleSort(array,0,len(array)-1)  
            
        screen.fill((250,250,250))     
        draw("BUBBLE")
        pygame.display.update()



def mer():
    global pause
    crashed = False
    while not crashed:
        for event in pygame.event.get():   
            if event.type == pygame.QUIT:           
                crashed=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: 
                    generate_arr() 
                if event.key == pygame.K_RETURN:
                    MergeSort(array,0,len(array)-1)
                    clrchange(array,len(array))

        screen.fill((250,250,250))      
        draw("MERGE")
        pygame.display.update()


def qui():
    global pause
    crashed = False
    while not crashed:
        for event in pygame.event.get():   
            if event.type == pygame.QUIT:           
                crashed=True
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_r: 
                    generate_arr() 
                if event.key == pygame.K_RETURN:
                    QuickSort(array,0,len(array)-1)
                    clrchange(array,len(array))

        screen.fill((250,250,250))        
        draw("QUICK")
        pygame.display.update()



def sel():
    global pause
    crashed = False
    while not crashed:
        for event in pygame.event.get():   
            if event.type == pygame.QUIT:           
                crashed=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: 
                    generate_arr() 
                if event.key == pygame.K_RETURN:
                    SelectionSort(array,0,len(array)-1)
                                    
        screen.fill((250,250,250))    
        draw("SELECTION")
        pygame.display.update()


def ins():
    global pause
    crashed = False
    while not crashed:
        for event in pygame.event.get():   
            if event.type == pygame.QUIT:           
                crashed=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: 
                    generate_arr() 
                if event.key == pygame.K_RETURN:
                    InsertionSort(array,0,len(array)-1)
                    clrchange(array,len(array))
                
        screen.fill((250,250,250))        
        draw("INSERTION")
        pygame.display.update()


def hea():
    global pause
    crashed = False
    while not crashed:
        for event in pygame.event.get():   
            if event.type == pygame.QUIT:           
                crashed=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: 
                    generate_arr() 
                if event.key == pygame.K_RETURN:
                    HeapSort(array,0,len(array)-1)
                
        screen.fill((250,250,250))        
        draw("HEAP")
        pygame.display.update()


crashed = False
while not crashed:

    for event in pygame.event.get():   
        if event.type == pygame.QUIT:          
            ex()
    screen.blit(back1,(0,0))
    
    
    top()
    button("MERGE SORT!!",150,200,150,50,blue,light_blue,white,mer)
    button("QUICK SORT!!",600,200,150,50,blue,light_blue,white,qui)
    button("BUBBLE SORT!!",150,350,150,50,blue,light_blue,white,bub)
    button("SELECTION SORT!!",600,350,150,50,blue,light_blue,white,sel)   
    button("INSERTION SORT!!",150,500,150,50,blue,light_blue,white,ins)
    button("HEAP SORT!!",600,500,150,50,blue,light_blue,white,hea)

    pygame.display.update()
    
pygame.quit()
quit()

