#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 *is_palindrome -checks if a singly linked list is a palindrome
 * @head: A pointer
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int length = 0;
	int i;
	int *values;

	/* Get the length of the list and store the values in an array */
	while (current != NULL)
	{
		length++;
		current = current->next;
	}
	values = malloc(sizeof(int) * length);
	if (values == NULL)
		return (0);
	current = *head;
	for (i = 0; i < length; i++)
	{
		values[i] = current->n;
		current = current->next;
	}
	/* Compare the values in the array to the values in the list */
	current = *head;
	for (i = 0; i < length; i++)
	{
		if (values[i] != current->n)
		{
			free(values);
			return (0);
		}
		current = current->next;
	}
	free(values);
	return (1);
}
