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
	int s = Py_Size(p);
	PyObject *o;
	int aloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", aloc);
	while (i < s)
	{
		o = PyList_GetItem(p, i);
		printf("Element %i: %s\n", i, Py_TYPE(o)->tp_name);
	}
}
