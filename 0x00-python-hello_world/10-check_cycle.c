#include "lists.h"

/**
 * check_cycle - check if singly-linked list contains cycle
 * @list: singly linked list
 *
 * Return: 0 (no cycle) or 1 (there is cycle)
 */
int check_cycle(listint_t *list)
{
	listint_t *slowturtle = list;
	listint_t *fasthare = list;

	if (!list)
		return (0);

	while (slowturtle && fasthare && fasthare->next)
	{
		slowturtle = slowturtle->next;
		fasthare = fasthare->next->next;
		if (slowturtle == fasthare)
			return (1);
	}

	return (0);
}
