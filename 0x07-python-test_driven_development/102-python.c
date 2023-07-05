#include <Python.h>

void print_python_string(PyObject *p)
{
	Py_ssize_t len;
	Py_UNICODE *pstr;
	int i;

	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	pstr = PyUnicode_AsUnicode(p);
	len = PyUnicode_GetLength(p);
	i = PyUnicode_KIND(p);

	printf("  type: compact unicode object\n");
	printf("  length: %ld\n", len);
	printf("  value: ");
}
