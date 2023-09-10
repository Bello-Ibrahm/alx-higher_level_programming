#include "lists.h"
/**
 * is_palindrome - checks if singly linked list is a palindrome
 * @head: head of linked list
 * Return:  0 if it's not a palindrome, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	int len = 0, i = 0;
	listint_t *tmp;
	int NodeContainer[10000];

	tmp = *head;
	if ((*head) == NULL)
		return (1);
	while (tmp != NULL)
	{
		len++;
		tmp = tmp->next;
	}
	if (len == 1)
		return (1);
	tmp = *head;
	while (tmp != NULL)
	{
		NodeContainer[i] = tmp->n;
		tmp = tmp->next;
		i++;
	}
	for (i = 0; i <= len / 2; i++)
	{
		if (NodeContainer[i] != NodeContainer[len - i - 1])
		{
			return (0);
		}
	}
	return (1);
}
