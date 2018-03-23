''' Add two matrix '''

a = [[1,2,3], [2,4,6], [3,6,9]]
b = [[1,2,3], [4,5,6], [7,8,9]]
c = [[0,0,0], [0,0,0], [0,0,0]]

#function for adding two 3x3 matricx
def add_mat(a,b,c):
    for i in range(len(a)):
        for j in range(len(a[0])):
            c[i][j] = a[i][j] + b[i][j]
            
def mat_disp(mat):
    for row in mat:
        for col in row:
            print(col , end=' ')
        print()
        
add_mat(a,b,c)

print('First Matrix : ',a)
mat_disp(a)
print('Second Matrix :',b)
mat_disp(b)
print('Sum of the matrix :',c)
mat_disp(c)
