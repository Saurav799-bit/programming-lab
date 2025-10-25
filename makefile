employee_app: main.c employee.c print.c
	gcc main.c employee.c print.c -o employee_app

clean:
	rm -f employee_app