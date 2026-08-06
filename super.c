#include <stdio.h>
int main () { 
char nombre [50];
float precio, subtotal, total=0, descuento=0;
int cantidad; 
char continuar;
do {
    printf("Nombre del producto: ");
    scanf("%[^\n]", nombre);

        printf("Precio: ");
        scanf("%f", &precio);

        printf("Cantidad: ");
        scanf("%d", &cantidad);

        subtotal = precio * cantidad;
        total += subtotal;

        printf("Subtotal de %s: %.2f\n", nombre, subtotal);

        printf("¿Quiere agregar algo mas? (s/n): ");
        scanf(" %c", &continuar);

    } while (continuar == 's' || continuar == 'S');

    if (total > 1000); {
        descuento = total * 0.10;
    }
    printf("\nTotal: %.2f\n", total);
    printf("Descuento: %.2f\n", descuento);
    printf("Total a pagar: %.2f\n", total - descuento);

    return 0;
}