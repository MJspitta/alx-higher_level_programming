#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - check if it is palindrome
 * @head: head pointer
 *
 * Return: 0 (not palindrome), 1 (is palindrome)
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	slow = rev_list(&slow);
	fast = *head;
	while (slow != NULL)
	{
		if (fast->n != slow->n)
			return (0);
		fast = fast->next;
		slow = slow->next;
	}
	return (1);
}

/**
 * rev_list - reverse linked list
 * @head: head pointer
 *
 * Return: pointer to new head
 */
listint_t *rev_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return prev;
}
