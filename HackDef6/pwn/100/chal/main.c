#include <stdio.h>
#include <stdlib.h>

#define MAX_INSTRUCCIONES 50
#define TAM_ARR 10

int arr[TAM_ARR];

void init(){
    setvbuf(stdin , NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void muestra_instrucciones(){
    printf("Bienvenido a mini shellcoding.\n");
    printf("Las instrucciones aceptadas son:\n");
    printf("0 idx1 idx2:\n");
    printf("    arr[idx1] = arr[idx2]\n");
    printf("\n");
    printf("1 idx1 idx2:\n");
    printf("    arr[idx1] += arr[idx2]\n");
    printf("\n");
    printf("2 idx1 idx2:\n");
    printf("    arr[idx1] -= arr[idx2]\n");
    printf("\n");
    printf("3 idx1 idx2:\n");
    printf("    arr[idx1] *= arr[idx2]\n");
    printf("\n");
    printf("4 idx1 idx2:\n");
    printf("    arr[idx1] /= arr[idx2]\n");
    printf("\n");
    printf("5 idx1 idx2:\n");
    printf("    arr[idx1] |= arr[idx2]\n");
    printf("\n");
    printf("6 idx1 idx2:\n");
    printf("    arr[idx1] &= arr[idx2]\n");
    printf("\n");
    printf("7 idx1 idx2:\n");
    printf("    arr[idx1] ^= arr[idx2]\n");
    printf("\n");
    printf("8 idx1:\n");
    printf("    arr[idx1] = 1\n");
    printf("\n");
    printf("9:\n");
    printf("    llamada");
    printf("    si arr[0] == 0, entonces imprimir arr[1]\n");
    printf("    si arr[0] == 1, entonces sumar 1 a todo arr\n");
    printf("    si arr[0] == 2, entonces imprimir flag si arr[1] == 65535\n");
    printf("    si arr[0] == 4, entonces salir\n");
    printf("\n");
}

void check_idx(int idx){
    if(idx < 0 || idx >= TAM_ARR){
        printf("idx=%d invalido\n", idx);
        exit(1);
    }
}

void llamada(){
    switch(arr[0]){
        case 0:
            printf("arr[1]=%d\n", arr[1]);
            break;
        case 1:
            for(int i = 0; i < TAM_ARR; i++){
                arr[i]++;
            }
            break;
        case 2:
            if(arr[1] == 65535){
                printf("Felicidades! Aqui tienes tu flag\n");
                system("cat flag.txt");
            }else{
                printf(":(");
            }
            break;
        case 4:
            printf("Bye!\n");
            exit(0);
        default:
            printf("op desconocida : %d\n", arr[0]);
            break;
    }
}

int main(){
    init();
    muestra_instrucciones();
    int N = 0;
    printf("cantidad de instrucciones : ");
    scanf("%d", &N);
    if(N < 0 || N > MAX_INSTRUCCIONES){
        printf("N=%d no esta permitido\n", N);
        return -1;
    }

    for(int i = 1; i <= N; i++){
        int tipo = -1;
        scanf("%d", &tipo);
        int idx1 = -1, idx2 = -1;
        switch(tipo){
            case 0:
                scanf("%d%d", &idx1, &idx2);
                check_idx(idx1);
                check_idx(idx2);
                arr[idx1] = arr[idx2];
                break;
            case 1:
                scanf("%d%d", &idx1, &idx2);
                check_idx(idx1);
                check_idx(idx2);
                arr[idx1] += arr[idx2];
                break;
            case 2:
                scanf("%d%d", &idx1, &idx2);
                check_idx(idx1);
                check_idx(idx2);
                arr[idx1] -= arr[idx2];
                break;
            case 3:
                scanf("%d%d", &idx1, &idx2);
                check_idx(idx1);
                check_idx(idx2);
                arr[idx1] *= arr[idx2];
                break;
            case 4:
                scanf("%d%d", &idx1, &idx2);
                check_idx(idx1);
                check_idx(idx2);
                arr[idx1] /= arr[idx2];
                break;
            case 5:
                scanf("%d%d", &idx1, &idx2);
                check_idx(idx1);
                check_idx(idx2);
                arr[idx1] |= arr[idx2];
                break;
            case 6:
                scanf("%d%d", &idx1, &idx2);
                check_idx(idx1);
                check_idx(idx2);
                arr[idx1] &= arr[idx2];
                break;
            case 7:
                scanf("%d%d", &idx1, &idx2);
                check_idx(idx1);
                check_idx(idx2);
                arr[idx1] ^= arr[idx2];
                break;
            case 8:
                scanf("%d", &idx1);
                check_idx(idx1);
                arr[idx1] = 1;
                break;
            case 9:
                llamada();
                break;
        }
    }
    printf("Suerte para la proxima\n");
    return 0;
}

