#include "main.h"

/**
 * print_python_list - print basic info python lists
 * @p: pointer to object
 *
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t s, i;
	PyListObject *aloc;
	PyObject *list_item;

	aloc = (PyListObject *)p;
	s = ((PyVarObject *)(p))->ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", aloc->allocated);

	for (i = 0; i < s; i++)
	{
		list_item = aloc->ob_item[i];
		printf("Element %ld: %s\n", i, list_item->ob_type->tp_name);
		if (PyBytes_Check(list_item))
			print_python_bytes(list_item);
	}
}

/**
 * print_python_bytes - print basic info python bytes obj
 * @p: pointer to object
 *
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t s, i, limiter;
	char *data_str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	s = ((PyVarObject *)(p))->ob_size;
	data_str = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", s);
	printf("  trying string: %s\n", data_str);

	if (s >= 10)
		limiter = 10;
	else
		limiter = s + 1;
	printf("  first %ld bytes:", limiter);

	for (i = 0; i < limiter; i++)
	{
		if (data_str[i] >= 0)
			printf(" %02x", data_str[i]);
		else
			printf(" %02x", 256 + data_str[i]);
	}
	printf("\n");
}
