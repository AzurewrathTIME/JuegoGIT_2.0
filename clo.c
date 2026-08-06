#include <stdio.h>
#include <time.h>

int main() 
{
   clock_t inicio, fin;
   double tiempo;

   inicio = clock();
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

   // Código a medir
   for(int mat = 0; mat < 100000000; mat++);
     for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            for (int k = 0; k < 3; k++) {
                matrizF[i][j] += matriz1[i][k] * matriz2[k][j];
                for (int i = 0; i < 3; i++) {
         for (int j = 0; j < 3; j++) {
            printf("%d ", matrizF[i][j]);
        }
        printf("\n");
    }
            }
         }
     }
         
    
     
    }

   fin = clock();

   tiempo = (double)(fin - inicio) / CLOCKS_PER_SEC;

   printf("Tiempo de ejecucion: %f segundos\n", tiempo);

   return 0;
}  