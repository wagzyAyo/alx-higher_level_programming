#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Return: 0 If the function fails or pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new_address;

	new_address = malloc(sizeof(listint_t));
	if (new_address == NULL)
		return (NULL);
	new_address->n = number;

	if (node == NULL || node->n >= number)
	{
		new_address->next = node;
		*head = new_address;
		return (new_address);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new_address->next = node->next;
	node->next = new_address;

	return (new_address);
}
