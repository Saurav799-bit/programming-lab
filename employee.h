#ifndef EMPLOYEE_H
#define EMPLOYEE_H

typedef struct {
    int id;
    char name[50];
    int age;
    float salary;
} Employee;

void inputEmployee(Employee *e);

#endif
