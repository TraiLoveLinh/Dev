C = ["A", "B", "C"]
def Hanoi(n,i,j,k):
    if n == 1:
        print("Chuyen dia ",n," tu coc ",C[i]," sang coc ",C[j])
    else:
        Hanoi(n-1,i,k,j)
        print("Chuyen dua ",n," tu coc",C[i]," sang coc",C[j])  
        Hanoi(n-1,k,j,i)


Hanoi(3,0,2,1)