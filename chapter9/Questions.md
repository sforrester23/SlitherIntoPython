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

If the list is sorted, then for each list member, only one comparison will be made since it will deny the comparison that it's left member is greater than it. Hence the total number of comparisons is ```n```: only one comparison per number in the list.

In this case of a pre-sorted list for selection sort, we have significantly more comparisons than ```n```. The sorting algorithm cycles from left to right through the list members (say, using index i). It essentially splits the list into two parts, the sorted and unsorted part of the list. For each of these steps it searches through the list from that point i to the end of the list (in the unsorted section), for the lowest value in the list that is lower than the value at position i.

By relocating this minimum value to the point i and sending the value that was at point i to the place where the minimum was positioned, step by step we see this builds the list so that it is always sorted in order up to point i. If no value lower than the one at point i is found on a given cycle, then no relocation occurs because this would make the list up to point i unsorted. E.g. if position i has value 3, and the minimum found in the list from point i onwards is 5, it makes no sense to move 5 in front of 3, so we move to the next position in the list to cycle through.  

For each iteration, the list is always sorted up to index point i, and unsorted after i until the end of the list (it could well be sorted, but we do not know because the computer has not checked it yet. And indeed in this example we will assume this list is in fact already sorted).

So, in the case where the list is actually sorted, what we have happening is the index i cycling through the list (this is the same as in insertion sort, so we cannot separate them based on this part of the way they work), but for each point in the list we have to compare each and every one of those numbers to the right of the index i, to check if any of them are less than the value at position i.

In the case of this sorting technique, there is in fact never any number in the remaining list to the right of point i that is less than the one at point i, since we know the list is ordered so. This means each iteration a comparison is done for each of the remaining items in the list, without achieving any swapping.

So, there are therefore (n-i) comparisons to do at each point i in the list, where n is the total number of items in the list and j ranges from 0 to n-1.

Hence the total number of comparisons is:

        S(n) =  n + (n-1) + (n-2) + ... + (n - (n - 3)) + (n - (n - 2)) + (n - (n - 1))
        S(n) =  n + (n-1) + (n-2) + ... + 3 + 2 + 1

But also, by associativity of addition (meaning you can write additions in any order and it will still be the same):

        S(n) = n + (n-1) + (n-2) + ... +    3    +    2    + 1
        S(n) = 1  +  2   +   3   + ... + (n - 2) + (n - 1) + n

So by adding both sides of these two expressions in these two different orders we get:

        2S(n) = (n + 1) + (n - 1 + 2) + (n - 2 + 3) + ... + (3 + n - 2) + (2 + n - 1) + (1 + n)

Hence,

        2S(n) = (n + 1) + (n + 1) + ... + (n + 1) + (n + 1)

Where there are n lots of (n+1)'s summed, so:

        2S(n) = n(n + 1)

Meaning:

        S(n) = n(n + 1)/2
             = (n^2)/2 + n/2

And hence there are n(n+1)/2 comparisons carried out on the selection sort, regardless of the fact that the list is sorted. This is always greater than the number n (for insertion sort comparisons), for values of n greater than or equal to 2. The n = 1 case is trivial, since that would not require a sort and they have the same number of comparisons, equal to 1. In fact, in each case the sorting algorithm wouldn't work for lists of length 1 because the indexing required would cause it to error.

Hence - as each sorting method has the same space complexity that doesn't vary with size of list - the insertion sort is more efficient for lists that happen to be already sorted because the selection sort always requires more comparisons (which are time consuming) than the insertion sort.

Which sorting technique is better will change depending on how "unsorted" a list is, which is not something easy to define. Typically insertion sort will use fewer comparisons but it does require more swaps to be done by defining a "dummy" variable for the compared value and moving adjacent values in lists that are not sorted. These swaps do cause a time delay on large scale list sorting (where n is very large).

Selection sort does not require swapping each time you see two unsorted adjacent values, it just finds what needs to be placed and moves it to the position in the list. So in a case where the sorting algorithm finds a lot of out of order adjacent values, it was swap a lot using insertion sort and hence selection sort might be better. It all depends on the degree of "sortedness".
