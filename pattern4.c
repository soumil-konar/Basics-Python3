#include<stdio.h>
int main()
{
	int i,j,m=1;
	int rows;
	printf("Please enter the number of rows you want: \n");
	scanf("%d", &rows);
	for(i=rows;i>=1;i--)
	{
		for(j=1;j<=i-1;j++)
		{
			printf(" ");
		}
		for(int k=1;k<=m;k++)
		{
			printf("*");
		}
		printf("\n");
		m++;	
	}	
	return 0;
}
