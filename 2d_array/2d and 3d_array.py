


""" 
  0  1  2
0[1][2][3]
1[4][5][6]


for(i=0; i<2; i++) row
{
	for(j=0; j<3; j++) column
	{
		printf("%d", a[i][j])
	}
}



[1][2][3]		 [7] [8] [9]
[4][5][6]		[20][21][14]



for(i=0; i<2; i++) #i đại diện cho mỗi array
{
	for(j=0; j<2; j++) # j đại diện cho row
	{
		for(z=0; z<3; z++) # z đại diện cho column
		{
			print(a[i][j][z])
		}
	}
}


#				0       1
array = [	[[1,2, 3], [5,6,7],
			[8, 9, 10], [11, 12, 13]]
]			# 2 			#3


print(array[0][2][2]) 10
"""