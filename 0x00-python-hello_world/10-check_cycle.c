#include <stdlib.h>
#include "lists.h"

/**
* check_cycle - Checks if a singly-linked list contains a cycle.
* @list: A singly-linked list.
*
* Return: If there is no cycle - 0.
*         If there is a cycle - 1.
*/
int check_cycle(listint_t *list)
{
	listint_t *c, *r;

	if (list == NULL || list->next == NULL)
		return (0);

	c = list->next;
	r = list->next->next;

	while (c && r && r->c)
	{
		if (c == r)
			return (1);

		c = slow->next;
		r = fast->next->next;
	}

	return (0);
}
