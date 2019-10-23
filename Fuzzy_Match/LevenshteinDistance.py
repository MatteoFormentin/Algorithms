# Levenshtein Distance Algorithm
# Calculate how much two string differ each other in terms of insert a new letter, delete one or substitute it (no swap)
# Works by building a matrix with one string as row and one as column, on the row 0 and column 0 is placed an empty character that means empty string.
# Each submatrix [0,m][0,n] is the substring distance, building the full matrix on [len(a)][len(b)] there is the Levenshtein distance.
# Building equation:
# # lev[i,j] = min{lev[i-1,j-1] + c , lev[i,j-1] + 1 , lev[i-1,j] + 1 }
# lev[i - 1, j] + 1,     // insert - go left
# lev[i, j - 1] + 1,      // delete - go up
# lev[i - 1, j - 1] + c   // substitute
# On each step ìt is searched the minum operation to align the substring


def levenshteinDistance(a, b):
    matrix = [[0 for x in range(len(b)+1)] for y in range(len(a)+1)]

    for i in range(0, len(a)+1):
        for j in range(0, len(b)+1):
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            else:
                if a[i-1] == b[j-1]: #next is i,j since we have the empty string line/column
                    c = 0
                else:
                    c = 1

                # M[i][j] = min{M[i-1][j-1] + c , M[i][j-1] + 1 , M[i-1][j] + 1 }
                # d[i - 1, j] + 1,     // insert - go right
                # d[i, j - 1] + 1,      // delete - go down
                # d[i - 1, j - 1] + c   // substitute (c==1)/do nothing (c==0) - go down-right
                matrix[i][j] = min(matrix[i-1][j-1] + c,
                                   min(matrix[i][j-1] + 1, matrix[i-1][j]+1))

    return matrix[len(a)][len(b)]


print(levenshteinDistance("google", "facebook"))
