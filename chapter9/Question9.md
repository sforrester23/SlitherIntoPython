## Question 1
Both insertion sort and selection sort have a time complexity of O(n<sup>2</sup>)
### Question 2
Both insertion sort and selection sort have a space complexity of O(1)

## Question 3
Example of insertion sort: Ordering people by height, because you can more visibly see when someone is shorter than someone without measuring.
Example of selection sort: Ordering a deck of playing cards, because it is clear when you have searched the deck of cards when you have found the aces and to move them to the front. 

## Question 4
If the list is already sorted going into it without us knowing, we would prefer insertion sort because it will do fewer comparisons before arriving at the decision of being sorted compared to the selection sort. Fewer comparisons means a smaller amount of time to arrive at the sorted output, hence it is better and it requires less computing time.

Insertion sort starts at the far right of a list and compares it to the member of the list to the left of it, moving it down if it is less than it and then repeating the comparison until it finds a member on its left that is not greater than it. 

If the list is sorted, then for each list member, only one comparison will be made since it will deny the comparison that it's left member is greater than it. Hence the total number of comparisons is n: only one comparison per number in the list.

In this case of a pre-sorted list for selection sort, we have significantly more comparisons than n. The sort cycles from left to right through the list members (say, using index j), for each of these steps it searches for a minimum in the remaining (unsorted) right hand side of the list, then moves this located minimum to position j. 

Hence the list is always sorted up to index point j, and potentially unsorted after j until the end of the list (it could well be sorted, but we do not know because the computer has not checked it yet. And indeed in this example we will assume this list is in fact already sorted).

So, in the case where the list is actually sorted, what we have happening is the index j cycling through the list (this is the same as in insertion sort, so we cannot separate them based on this part of the way they work), but for each point in the list we have to find the minimum of all points to the right of j. This means comparing each and every one of those numbers to the right of the index j. 

Even when we know the next available minimum in the remaining unsorted list is just one step to the right, the computer doesn't know that and must check each and every other digit for a smaller one, such is how the minimum function would work on an unsorted list. 

So, there are therefore (n-j) comparisons to do at each point j in the list, where n is the total number of items in the list and j ranges from 0 to n-1. 

Hence the total number of comparisons is:

        S(n) =  n + (n-1) + (n-2) + ... + (n - (n - 3)) + (n - (n - 2)) + (n - (n - 1))
        S(n) =  n + (n-1) + (n-2) + ... + 3 + 2 + 1
        
but also, by associativity of addition: 
       
        S(n) = 1 + 2 + 3 + ... + (n - 2) + (n - 1) + n

So by adding both sides of these two expressions in these two different orders we get:
        
        2S(n) = (n + 1) + (n - 1 + 2) + (n - 2 + 3) + ... + (3 + n - 2) + (2 + n - 1) + (1 + n)
        
Hence,

        2S(n) = (n + 1) + (n + 1) + ... + (n + 1) + (n + 1)
        
Where there are n lots of (n+1)'s summed, so:

        2S(n) = n(n + 1)

Meaning:
        
        S(n) = n(n + 1)/2
             = (n^2)/2 + n/2
        
And hence there are n(n+1)/2 comparisons carried out on the selection sort, regardless of the fact that the list is sorted. This is always greater than the number n (for insertion sort comparisons), for values of n greater than or equal to 2. The n = 1 case is trivial, since that would not require a sort and they have the same number of comparisons, equal to 1.

Hence - as each sorting method has the same space complexity that doesn't vary with size of list - the insertion sort is more efficient for lists that happen to be already sorted because the selection sort always requires more time consuming comparisons than the insertion sort for already ordered lists.
        