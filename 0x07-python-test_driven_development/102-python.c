#include "Python.h"

void print_python_string(PyObject *p)
{
	Py_ssize_t len, i;
	Py_UNICODE *pstr;

	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	len = PyUnicode_GET_LENGTH(p);
	pstr = PyUnicode_AS_UNICODE(p);

	printf("  type: compact unicode object\n");
	printf("  length: %ld\n", len);
	printf("  value: ");
	for (i = 0; i < length; i++)
		printf("%lc", val[i]);
	printf("\n");
}
