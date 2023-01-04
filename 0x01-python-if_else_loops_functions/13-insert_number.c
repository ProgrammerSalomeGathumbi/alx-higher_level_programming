#include <stdlib.h>
#include "lists.h"

/**
*insert_node - inserts a number into a sorted singly linked list
*@head: pointer to a pointer to the head of the list
*@number: the number to be inserted
*Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	current = *head;

	if (number < current->n)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	while (current->next != NULL && number > current->next->n)
		current = current->next;
	new->next = current->next;
	current->next = new;
	return (new);
}
