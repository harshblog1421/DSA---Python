Given an array of integers A with N elements and a target integer B, the task is to find all the indices at which B occurs in the array.

Note: The problem encourages recursive logic for learning purposes. Although the online judge doesn't enforce recursion, it's recommended to use recursive solutions to align with the question's spirit.

def search(A,B,index,result):

    if index >=len(A):
        return 
        
    if A[index] ==B:
        result.append(index)
    
    search(A,B,index+1,result)

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def allIndices(self, A, B):
        result = []
        search(A,B,0,result)
        return result
