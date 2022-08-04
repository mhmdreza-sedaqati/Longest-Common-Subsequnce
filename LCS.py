first_sequence = input("Please enter first sequence : ")
second_sequence = input("Please enter second sequence : ")

m = len(first_sequence)
n = len(second_sequence)

number_matrix = [[0 for i in range(n+1)] for j in range(m+1)] 
arrow_matrix = [[0 for i in range(n+1)] for j in range(m+1)] 

for i in range(m):
    for j in range(n):
        if first_sequence[i] == second_sequence[j]:
            number_matrix[i+1][j+1] = number_matrix[i][j] + 1
            arrow_matrix[i+1][j+1] = "digonal"
        
        elif number_matrix[i][j+1] >= number_matrix[i+1][j]:
            number_matrix[i+1][j+1] = number_matrix[i][j+1]
            arrow_matrix[i+1][j+1] = "UP"

        else:   
            number_matrix[i+1][j+1] = number_matrix[i+1][j]
            arrow_matrix[i+1][j+1] = "LEFT"

print(number_matrix)

for i in range(n+1):
    arrow_matrix[0][i] = ' '

for i in range(m+1):
    arrow_matrix[i][0] = ' '

print(arrow_matrix)

ls1 = []


while True:
    if( arrow_matrix[m][n] == ' ' ):
        break
    elif ( arrow_matrix[m][n] == "UP" ):
        m = m-1
    elif ( arrow_matrix[m][n] == "LEFT" ):
        n = n-1
    elif ( arrow_matrix[m][n] == "digonal" ):
        ls1.append(first_sequence[m-1])
        m = m-1
        n = n-1

ls2 = []
i = len(ls1) - 1
for j in range(len(ls1)):
    ls2.append(ls1[i])
    i = i-1

lcs = "".join(ls2)
print("the longest common subsequence is : {0}".format(lcs))


