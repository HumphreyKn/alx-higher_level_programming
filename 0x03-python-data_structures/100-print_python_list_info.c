#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to the PyListObject (list)
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *ll;
	int i;

	ll = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", ll->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", ll->allocated);

	for (i = 0; i < ll->ob_base.ob_size; i++)
	{
		printf("Element %d: %s\n", i, ll->ob_item[i]->ob_type->tp_name);
	}
}
