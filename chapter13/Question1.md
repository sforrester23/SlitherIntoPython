## Question 1
### Answer the following questions:

##### Why must we add 1 to low when updating it's value?
We must add ```1``` to ```low``` when updating its value because we need to end up having ```low = high``` by the end of the search, so that we can say we have found the correct value. If there is no adding of a 1, then in some cases we never settle on a final value as we are reduced to a list of two values by the end of the loop without any way to distinguish between the two.
 
We know our value is one of the two in this list, but due to the way that the mid point is calculated, by rounding down the division of two (this is problematic when the sum of ```low + high``` is odd, as is always true for two adjacent numbers), we can end up setting the low point to the same value as it was before (in the case where ```arr[mid] < elem```). In this instance, the high value is not altered either and we just do another cycle with the same values of ```low```, ```high``` and hence ```mid``` as before, so nothing changes and we end up doing the same process with the same result having come so close. 

This causes us to either loop infinitely if the algorithm is defined that way, or to continue to the end of our prescribed 20 guesses, as is laid out in the chapter notes, without definitively finding our desired element and knowing that it is just one of two elements left in our search list. 

The reason it also makes sense to add 1 to our mid value when assigning to ```low``` is because of the strict inequality imposed on the condition ```arr[mid] < elem```. The ```low = mid + 1``` procedure only executes if the value at the mid point is _*definitely*_ lower than the element we're searching for, we know that the ```mid``` value is not our element because of the strictness of the inequality, whereas the ```mid + 1``` point may well contain the value we are looking for. It is therefore safe to reset our ```low``` point to ```mid + 1``` since the searching mechanic will still include that value in the process for the search, that is because for each iteration it can only search between points ```low``` and ```high```. In the case where the ```mid``` value _is_ our element, the condition ```arr[mid] < elem``` will register as false and we will not exclude it from our search span, because ```high``` is set to ```mid``` thus it is still included. 

It also makes sense to reduce the scope of our list each time. Without the +1 we are usually just halving the size of our list. In the cases where we execute the ```low = mid + 1``` reassignment, we are also reducing the length of out list to search in by one, speeding up the process more than you might think in the long run. 

Also for example, if we had our inequality the other way around, say using the comparison ```arr[mid] > elem```, we would be want to enact the reassignment of ```high = mid - 1``` in the case where it is true. This works in the same way. We know if the condition is true, that the ```mid``` value does not contain our element, so we can remove it and only extend our list of search points (that is, the ones between low to high) to include values we _know_ are contenders to be the element we are searching for, speeding up the process along the way.

In summary, we need to at the ```low = mid + 1``` term to make sure we converge on a single value, without it we might, depending on the list, continue looping to the end with the same two values of ```low``` and ```high```, not knowing which is our element and exceeding our number of tries. 

Although in certain order list structures or for certain given ```elem```'s the process might work without this ```+1```, we need to be sure we can get it right every time. This adjustment makes sure of that. It also speeds up the process more than you think, reducing the scope of the search by potentially more than half when the condition is true. 

##### What is the runtime complexity of Binary Search?

The runtime complexity of Binary Search is ```O(log(n))```, where log is the logarithm to the base 2.

##### What is the space complexity of Binary Search?
The space complexity of Binary Search is ```O(1)```, that is it uses constant memory because no copies are made of the list throughout. 

