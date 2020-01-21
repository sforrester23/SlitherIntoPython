### When should we use the following?

#### _raise_
We should use _raise_ when we need to raise an exception or specific error in a certain case, perhaps if a condition is not met and this wouldn't make sense, might break our code, or might lead to a stream of logic we haven't accounted for (or don't want to account for).  
#### _finally_
We should use _finally_ at the end of a _try, except_ block of code. It should contain code that we want to execute regardless of what errors might be caught in the _try, except_ blocks of code. It is useful for keeping our code atomic (not repeating ourselves), because it may save us from writing the same thing out repeatedly, e.g. for staging the next iteration of a while loop.

#### _try_ and _except_
We use _try_ and _except_ when we are executing a block of code that we think is likely to throw errors. This code is *tried* in the _try_ block, and the _except_ block contains code that prepares for those potential errors. When the _try_ block is executed and gives out one of those foreseen errors, it will catch them and output a tailored message to the user, based on the type of error thrown. If no errors are thrown, the code executes as normal.

A good example of this is to have an assignment of a variable as an integer:
        
        integer = int(variable)
        
if this variable is a string, this cannot be done and a ```ValueError``` will be thrown. We can catch this like so:

        try:
            integer = int(variable)
        except ValueError:
            print("You can't cast variable as an integer!")
This way, when that casting tries to occur and cannot, the user will be given a helpful message to tell them what is going on. If it can be cast as an integer, it will do so as normal, without any errors.

#### What is a precondition?
The precondition is a condition that is required to be true before entering a block of code (or more specifically method/function) safely, without any errors or loss of functionality/logic.

#### What is a postcondition?
The postcondition is a condition that is required to be true upon exiting a block of code (or more specifically method/function) safely, without any errors or loss of functionality/logic.

Both the precondition and postcondition are extremely import things to consider when error handling. With error handling we can make sure out precondition holds true before executing a block of code that is going to require certain conditions to be able to run smoothly and as intended for the required result (e.g. for a function that calculates time elapsed, we must have the first value of time inputed smaller than the second value). And we can also within that block of code make sure we utilise error handling so we don't come out of it the other side with any unexpected or unintended outputs that don't make sense or aren't as designed.