# =============================================================================
              #PATTERN--A
def a():
    for row in range(7):
        for col in range(5):
            if ((col==0 or col==4) and (row!=0)) or row==3 or ((row==0) and (col!=0 and col!=4)):
                print('*',end=' ')
            else:
                print(end='  ')
        print()        
    print('\n')
                   #PATTERN--B

    for row in range(7):
        for col in range(5):
            if ((row==0 or row==3 or row==6) and (col!=4)) or ((row==1 or row==2 or row==4 or row==5) and (col!=1 and col!=2 and col!=3)):
                print('*',end=' ')
            else:
                print(end='  ')
        print()        
    print('\n')
              #PATTERN--C

    for row in range(7):
        for col in range(5):
            if ((row==0 or row==6) and col!=0) or ((row==1 or row==2 or row==3 or row==4 or row==5) and (col!=1 and col!=2 and col!=3 and col!=4)) :
                print('*',end=' ')
            else:
                print(end=' ')
        print()        
    print('\n')
                #PATTERN-D
    for row in range(7):
      for col in range(5):
         if ((row==0 or row==6) and col!=4) or ((col==0 or col==4) and (row!=0 and row!=6)):
             print('*',end=' ')
         else:
             print(end='  ')
      print()
    print('\n')         
# =============================================================================
                  #PATTERN-E
# =============================================================================
    for row in range(7):
        for col in range(5):
            if (row==0 or row==3 or row==6) or col==0:
                print('*',end=' ')
            else:
                print(end='  ')
        print()
    print()                  
# =============================================================================
                     #PATTERN--F
    for row in range(7):
        for col in range(5):
            if  (row==0 or row==3) or col==0:             
                print('*',end=' ')
            else:
                print(end='  ')
        print() 
    print('\n') 
# =============================================================================
                   #PATTERN--G
# =============================================================================
    for row in range(7):
     for col in range(6):
         if (row==0 or row==6) or col==0 or ((col==4 or col==5) and (row!=1 and row!=2)) :
             print('*',end=' ')
         else:
             print(end='  ')
     print()                   
    print()
# =============================================================================
                        #PATTERN--H
# =============================================================================
    for row in range(7):
     for col in range(5):
         if col==0 or col==4 or row==3:
             print('*',end=' ')
         else:
             print(end='  ')
     print()        
    print()
# =============================================================================
                       #PATTERN--I
# =============================================================================
    for row in range(7):
     for col in range(5):
         if row==0 or row==6 or col==2:
             print('*',end=' ')
         else:
             print(end='  ')
     print()                       
    print()
# =============================================================================
                        #PATTERN--J
# =============================================================================
    for row in range(7):
     for col in range(5):
         if row==0 or (col==2) or (row==6 and (col!=2 and col!=3 and col!=4)):
             print('*',end=' ')
         else:
             print(end='  ')
     print()                         
    print()
# =============================================================================
                         #PATTERN-K
    for row in range(7):
     for col in range(5):
         if col==0 or ((row==0 and (col!=1 and col!=2 and col!=3))) or ((row==1 and (col!=1 and col!=2 and col!=4))) or ((row==2 and (col!=1 and col!=3 and col!=4))) or ((row==3 and (col!=3 and col!=2 and col!=4))) or ((row==4 and (col!=1 and col!=3 and col!=4))) or ((row==5 and (col!=1 and col!=2 and col!=4))) or ((row==6 and (col!=1 and col!=2 and col!=3))):
             print('*',end=' ')
         else:
             print(end='  ')
     print()        
    print()
# =============================================================================
                         #PATTERN-L
    for row in range(7):
        for col in range(5):
            if (row==6) or col==0:
                print('*',end=' ')
            else:
                print(end='  ')
        print()
    print()                     




                         #PATTERN-M
# =============================================================================
    for row in range(7):
     for col in range(7):
         if col==0 or col==6 or (row==1 and (col!=2 and col!=3 and col!=4 )) or (row==2 and (col!=1 and col!=3 and col!=6 and col!=5)) or (row==3 and (col!=1 and col!=2 and col!=4 and col!=5)):
             print('*',end=' ')
         else:
             print(end='  ')
     print()    
    print()
 #=============================================================================
                          #PATTERN-N
# =============================================================================
    for row in range(7):
     for col in range(7):
         if col==0 or col==6 or (row==1 and (col!=2 and col!=3 and col!=4 and col!=5)) or (row==2 and (col!=1 and col!=3 and col!=4 and col!=5)) or (row==3 and (col!=2 and col!=1 and col!=4 and col!=5)) or (row==4 and (col!=2 and col!=3 and col!=1 and col!=5)) or (row==5 and (col!=2 and col!=3 and col!=4 and col!=1)):
             print('*', end=' ')
         else:
             print(end='  ')
     print()                          
    print()
# =============================================================================
                          #PATTERN-O
    for row in range(7):
     for col in range(5):
         if ((row==0 or row==6) and (col!=0 and col!=4)) or ((col==0 or col==4) and (row!=0 and row!=6)):
             print('*',end=' ')
         else:
             print(end='  ')
     print()                                  
    print()
# #=============================================================================
# =============================================================================
                      #PATTERN-P
# =============================================================================
    for row in range(7):
     for col in range(5):
         if col==0 or col==4 and (row!=0 and row!=3 and row!=4 and row!=5 and row!=6) or ((row==0 or row==3) and col!=4):
             print('*',end=' ')
         else:
             print(end='  ')
     print()        
    print()
# =============================================================================
                         #PATTERN-Q
# =============================================================================
    for row in range(8):
     for col in range(5):
         if ((row==0 or row==6) and (col!=0 and col!=4)) or ((col==0 or col==4) and (row!=0 and row!=6 and row!=7)) or col==4 and row==7:
             print('*',end=' ')
         else:
             print(end='  ')
     print()                         
    print()

                         #PATTERN--R
# =============================================================================
    for row in range(7):
     for col in range(5):
         if col==0 or col==4 and (row!=0 and row!=3 ) or ((row==0 or row==3) and col!=4):
             print('*',end=' ')
         else:
             print(end='  ')
     print()        
    print()
                          #PATTERN-S 
# =============================================================================
    for row in range(7):
     for col in range(5):
         if ((row==0 or row==3 or row==6 ) and (col!=0 and col!=4)) or (col==0 and (row!=0 and row!=4 and row!=5 and row!=6 and row!=3)) or (col==4 and (row!=0 and row!=1 and row!=2 and row!=3 and row!=6)):
             print('*',end=' ')
         else:
             print(end='  ')
     print()        
    print()
# =============================================================================
                        #PATTERN-T
# =============================================================================
    for row in range(7):
     for col in range(5):
         if (row==0 or col==2):
             print('*',end=' ')
         else:
             print(end='  ')
     print()        
    print()
# =============================================================================
                         #PATTERN-U
# =============================================================================
    for row in range(7):
     for col in range(5):
         if ((row==6) and (col!=0 and col!=4)) or ((col==0 or col==4) and (row!=6))  :
             print('*',end=' ')
         else:
             print(end='  ')
     print()        
    print()
# =============================================================================
                         #PATTERN-V
# =============================================================================
    for row in range(4):
     for col in range(7):
         if (row==0 and (col!=5 and col!=1 and col!=2 and col!=3 and col!=4)) or (row==1 and (col!=6 and col!=0 and col!=2 and col!=3 and col!=4)) or (row==2 and (col!=1 and col!=0 and col!=5 and col!=3 and col!=6)) or (row==3 and (col!=0 and col!=1 and col!=2 and col!=5 and col!=6 and col!=4)):
             print('*',end=' ')
         else:
             print(end='  ')
     print()        
    print()
# =============================================================================
                      #PATTERN-W
# =============================================================================
    for row in range(4):
     for col in range(5):
         if (col==0 or col==4) or (row==1 and (col!=1 and col!=3)) or (row==2 and (col!=2)):
             print('*',end=' ')
         else:
             print(end='  ')
     print()                      
    print()
# =============================================================================
                    #PATTERN-X
# =============================================================================
    for row in range(5):
     for col in range(5):
         if ((row==0 or row==4) and (col!=1 and col!=2 and col!=3)) or (row==1 and (col!=0 and col!=2 and col!=4)) or (row==2 and (col!=0 and col!=1 and col!=3 and col!=4)) or (row==3 and (col!=0 and col!=2 and col!=4)):                  
             print('*',end=' ')
         else:
             print(end='  ')
     print()                         
    print()
    print()
# =============================================================================
                        #PATTERN-Y
# =============================================================================
    for row in range(5):
     for col in range(5):
         if (row==0 and (col!=1 and col!=2 and col!=3)) or (row==1 and (col!=0 and col!=2 and col!=4)) or (col==2 and (row!=0 and row!=1)):
             print('*',end=' ')
         else:
             print(end='  ')
     print()                        
    print()
    print()
# =============================================================================
                       #PATTERN-Z

    for row in range(5):
        for col in range(5):
            if (row==0 or row==4) or (row==3 and (col!=0 and col!=3 and col!=2 and col!=4)) or (row==1 and (col!=0 and col!=1 and col!=2 and col!=4)) or (col==2 and (row!=0 and row!=1 and row!=3 and row!=4)):
                print('*',end=' ')
            else:
                print(end='  ')
        print()                       




a();print('\n')

                  