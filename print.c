#include <stdio.h>
#include "print.h"

void printEmployee(const Employee *e) {
    printf("\n--- Employee Details ---\n");
    printf("ID: %d\n", e->id);
    printf("Name: %s\n", e->name);
    printf("Age: %d\n", e->age);
    printf("Salary: %.2f\n", e->salary);
}
