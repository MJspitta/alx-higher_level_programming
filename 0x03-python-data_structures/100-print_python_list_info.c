#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - print basic info about python list
 * @p: pointer to python object
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	int i = 0;
	long int s = PyList_Size(p);
	PyListObject *o = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", s);
	printf("[*] Allocated = %li\n", o->allocated);
	while (i < s)
	{
		printf("Element %i: %s\n", i, Py_TYPE(o->ob_item[i])->tp_name);
	}
}
