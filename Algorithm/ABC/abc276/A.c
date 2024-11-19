#include <stdio.h>
#include <string.h>

int main(void)
{
    char s[100];
    int size = sizeof(s);
    int idx = -1;
    scanf("%s", s);
    for (int i = 0; i < size; i++) {
        if (s[i] == 'a') {
            idx = i+1;
        }
    }
    printf("%d\n", idx);
    return 0;
}