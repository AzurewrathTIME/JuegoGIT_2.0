#include <stdio.h> 

int main() {
int matriz1[3][3]={
    {4, 2, 4},
    {2, 7, 8},
    {6, 5, 3}
 };

int matriz2[3][3]={
    {5, 3, 9},
    {4, 1, 7},
    {2, 8, 3}
  };

int matrizF[3][3]={
    {0, 0, 0},
    {0, 0, 0},
    {0, 0, 0}
  };
    int matriz[2][2] = {{1, 2}, {3, 4}};
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            for (int k = 0; k < 3; k++) {
                matrizF[i][j] += matriz1[i][k] * matriz2[k][j];
            }
        }
            
    }
        for (int i = 0; i < 3; i++) {
         for (int j = 0; j < 3; j++) {
            printf("%d ", matrizF[i][j]);
        }
        printf("\n");
    }
    return 0; 
} 

