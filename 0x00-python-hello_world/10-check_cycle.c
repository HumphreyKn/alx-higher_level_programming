#include "lists.h"

/**
 * check_cycle - checks if there is a cycle
 * @list: head of the linked list to check
 *
 * Return: 1 if there is a cycle, 0 if no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	if (list == NULL)
		return (0);

	while (first && second && second->next)
	{
		first = first->next;
		second = second->next->next;

		if (first == second)
		{
			return (1);
		}
	}

	return (0);
}
