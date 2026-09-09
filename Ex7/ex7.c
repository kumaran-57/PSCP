#include<stdio.h>
struct student {	// Structure Declaration
int rollno;
char name[20];
float sub[6];
float total,internal_mark[6];
};
void display(struct student stu[],int n);
int main()
{
struct student stu[20];	// Structure  variable Declaration
int i,j,k,n;
printf("\n Student Internal Mark Details");
printf("\n Enter the Number of Students : ");
scanf("%d",&n);
printf("\nRollNo\tName\n");	// Get student details
for(i=0;i<n;i++)
    {
scanf("%d%s",&stu[i].rollno,stu[i].name);
for(k=1;k<=5;k++)
        {
stu[i].total = 0.0;
for(j=1;j<=3;j++)
            {
printf("\n Enter the IA %d mark for sub %d:",j,k);
scanf("%f",&stu[i].sub[k]);
stu[i].total=stu[i].total+stu[i].sub[k];
            }
stu[i].internal_mark[k]=(stu[i].total/300)*20;
        }
    }
display(stu,n);
}
void display(struct student stu[],int n)
{
int i,j;
printf("\nThe Student Details are\n");
for(i=0;i<n;i++)
    {
printf("\nRollNo:%d\nName:%s\n", stu[i].rollno, stu[i].name);
for(j=1;j<=5;j++)
        {
printf("Subject%d - Internal Mark: %0.2f\n",j,stu[i].internal_mark[j]);
        }
    }
}
