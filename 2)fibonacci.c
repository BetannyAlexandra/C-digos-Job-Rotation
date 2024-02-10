#include <stdio.h>


int VerificarFibonacci(int num) {
    int a = 0, b = 1, c;

    while (b <= num) {
        if (b == num)
            return 1; 
        c = a + b;
        a = b;
        b = c;
    }

    return 0; 
}

int main() {
    int numero;

    printf("Digite o numero que deseja verificar se pertence a sequencia de Fibonacci: ");
    scanf("%d", &numero);
    if (VerificarFibonacci(numero)) {
        printf("%d pertence a sequencia de Fibonacci.\n", numero);
    } else {
        printf("%d nao pertence a sequencia de Fibonacci.\n", numero);
    }

    return 0;
}
