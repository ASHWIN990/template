#include <stdio.h>

int main(){
    char name[20];

    printf("\nEnter Your Name : ");
    scanf("%[^\n]%c", name);
    printf("\nYour Name is : %s", name);

    return 0;
}