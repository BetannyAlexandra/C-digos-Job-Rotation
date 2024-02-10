#include <stdio.h>
#include <string.h>

int main() {
    // exemplo de string a ser invertida
    char str[] = "programacao";
    
    int length = strlen(str);
    
    for (int i = 0; i < length / 2; i++) {
        char temp = str[i];
        str[i] = str[length - i - 1];
        str[length - i - 1] = temp;
    }
  
    printf("String invertida: %s\n", str);
    
    return 0;
}
