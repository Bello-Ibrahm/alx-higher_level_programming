#include "lists.h"
/**
 * print_dlistint - Print all the  elements of a linked list
 * @h: Head of a node
 *
 * Return: Number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	int count = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		count++;
	}
	return (count);
}
