def convert(s, numRows):
        if numRows == 1 or numRows >=len(s):
                return s
        res = [[] for i in range(numRows)]
        row = 0
        delta = -1
        for i in s:
                res[row].append(i)
                print("Outside IF --- ",res,i,row,delta)
                if row == 0 or row == numRows -1:
                        delta *= -1
                        print("Inside IF ----- ",res,delta)
                row += delta
                print("After DELTA ---- ",res,row)

        for i in range(len(res)):
                res[i] = ''.join(res[i])

        return ''.join(str(v) for v in res)    
		
		

print(convert("PAHNAPLSIIGYIR",3))
