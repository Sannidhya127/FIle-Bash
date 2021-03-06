// n is r0, we will pass it from python, ans is r1
mov r1, 1       	// ans = 1
loop:
cmp r0, 0       	// while n >= 0:
mulgt r1, r1, r0	//   ans *= n
subgt r0, r0, 1 	//   n = n - 1
bgt loop        	// 
                	// answer is in r1