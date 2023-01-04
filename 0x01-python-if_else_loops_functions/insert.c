#include <stdlib.h>
#include "lists.h"
/**
*insert_node -entry point
*@head: pointer
*@number: integer
*Return:address of new node or NULL if  failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
		*head = new_node;
	else
	{
		listint_t *current = *head;

		while (current->next != NULL &&
			current->next->n < number)
			current = current->next;
		new_node->next = current->next;
		current->next = new_node;
	}
	return (new_node);
}
