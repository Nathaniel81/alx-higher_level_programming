#include <Python.h>

/**
 * print_python_list_info -  prints some basic info about Python lists.
 *
 * @p: A pyObject list
 */

void print_python_list_info(PyObject *p)
{
	int size = Py_SIZE(p);
	int idx = 0, a = ((PyListObject *)p)->allocated;
	PyObject *o;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", a);

	while (idx < size)
	{
		o = PyList_GetItem(p, idx);
		printf("Element %d: ", idx);
		printf("%s\n", Py_TYPE(o)->tp_name);
		idx++;
	}
}
