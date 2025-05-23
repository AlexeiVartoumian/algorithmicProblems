Introduction
General syntax
The for loop is one of the most commonly used statements to repeatedly execute some logic. In Go it consists of the for keyword, a header and a code block that contains the body of the loop wrapped in curly brackets. The header consists of 3 components separated by semicolons ;: init, condition and post.

for init; condition; post {
  // loop body - code that is executed repeatedly as long as the condition is true
}
The init component is some code that runs only once before the loop starts.
The condition component must be some expression that evaluates to a boolean and controls when the loop should stop. The code inside the loop will run as long as this condition evaluates to true. As soon as this expression evaluates to false, no more iterations of the loop will run.
The post component is some code that will run at the end of each iteration.
Note: Unlike other languages, there are no parentheses () surrounding the three components of the header. In fact, inserting such parenthesis is a compilation error. However, the braces { } surrounding the loop body are always required.

For Loops - An example
The init component usually sets up a counter variable, the condition checks whether the loop should be continued or stopped and the post component usually increments the counter at the end of each repetition.

for i := 1; i < 10; i++ {
  fmt.Println(i)
}
This loop will print the numbers from 1 to 9 (including 9). Defining the step is often done using an increment or decrement statement, as shown in the example above.

Instructions
You are an avid bird watcher that keeps track of how many birds have visited your garden. Usually you use a tally in a notebook to count the birds, but to better work with your data, you've digitalized the bird counts for the past weeks.

Now that you got a general feel for your bird count numbers, you want to make a more fine-grained analysis.

Implement a function BirdsInWeek that accepts a slice of bird counts per day and a week number.

It returns the total number of birds that you counted in that specific week. You can assume weeks are always tracked completely.

birdsPerDay := []int{2, 5, 0, 7, 4, 1, 3, 0, 2, 5, 0, 1, 3, 1}
BirdsInWeek(birdsPerDay, 2)
// => 12

Stuck? Reveal Hints
Opens in a modal
You realized that all the time you were trying to keep track of the birds, there was one bird that was hiding in a far corner of the garden.

You figured out that this bird always spent every second day in your garden.

You do not know exactly where it was in between those days but definitely not in your garden.

Your bird watcher intuition also tells you that the bird was in your garden on the first day that you tracked in your list.

Given this new information, write a function FixBirdCountLog that takes a slice of birds counted per day as an argument and returns the slice after correcting the counting mistake.

birdsPerDay := []int{2, 5, 0, 7, 4, 1}
FixBirdCountLog(birdsPerDay)
// => [3 5 1 7 5 1]

Stuck? Reveal Hints
Opens in a modal
How to debug
When a test fails, a message is displayed describing what went wrong and for which input. You can also use the fact that console output will be shown too. You can write to the console using:

import "fmt"
fmt.Println("Debug message")
Note: When debugging with the in-browser editor, using e.g. fmt.Print will not add a newline after the output which can provoke a bug in go test --json and result in messed up test output.