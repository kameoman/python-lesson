void put_stars(int no)
{
    int i;
    for(i=no;i>=1;i--) 
        printf("*");
}  

void put_space(int no)
{
    int i;
    for(i=no-1;i>=1;i--) 
        printf(" ");

}

void put_triangle(int n)
{
   int i;
    for(i=n;i>=1;i--) {
        put_stars(i);
        printf("\n");
    }
    return;
}

int main(void)
{
    int ln;
    printf("何段ですか? ");
    scanf("%d",&ln);

    put_triangle(ln);

    return 0;
}