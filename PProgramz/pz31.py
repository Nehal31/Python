''' transpose of matrix '''

a_mat = [[1,2,5], [4,1,6], [3,6,9], [4,8,3]]


#function for adding two mXn matricx
def trans_mat(mat):
    t_mat = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
    return t_mat

def mat_disp(mat):
    for row in mat:
        for col in row:
            print(col , end=' ')
        print()
        
b_mat = trans_mat(a_mat)

print('Test Matrix : ')
mat_disp(a_mat)
print('Result Matrix : Transpose of Test Matrix')
mat_disp(b_mat)
