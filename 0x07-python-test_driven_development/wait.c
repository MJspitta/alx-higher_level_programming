#include "Python.h"
#include <stdio.h>

void print_python_string(PyObject *p)
{
	Py_ssize_t len, i;
	Py_UNICODE *val;

	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	len = PyUnicode_GET_LENGTH(p);
	val = PyUnicode_AS_UNICODE(p);

	printf("  type: compact unicode object\n");
	printf("  length: %ld\n", len);
	printf("  value: ");
	for (i = 0; i < len; i++)
		printf("%lc", val[i]);
	printf("\n");
}
