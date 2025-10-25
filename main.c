#include <stdio.h>
#include "employee.h"
#include "print.h"

int main()
{
    Employee e;
    inputEmployee(&e);
    printEmployee(&e);
    return 0;
}