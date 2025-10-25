#include <stdio.h>
#include "employee.h"

void inputEmployee(Employee *e)
{
    printf("Enter employee ID: ");
    scanf("%d", &e->id);

    printf("Enter name: ");
    scanf("%s", e->name);

    printf("Enter age: ");
    scanf("%d", &e->age);

    printf("Enter salary: ");
    scanf("%f", &e->salary);
}