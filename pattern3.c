#include<stdio.h>
int main()
{
	int i,j,rows;
	printf("Enter the number of rows you want: \n");
	scanf("%d", &rows);
	for(i=0;i<rows;i++)
	{
		for(j=0;j<(rows-i);j++)
		{
			printf("* ");
		}
		printf("\n");
		
	}
	return 0;
}
