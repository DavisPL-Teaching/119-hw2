# Hints

This file is optional.
Feel free to take a look at these hints if you get stuck!

## Part 1

1. Use .flatMap:

https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.flatMap.html

2. Use .reduceByKey:

https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.RDD.reduceByKey.html

4. Remember that a Python range(a, b)
includes a but does not include b.

5. To compute an average, you need the sum and the count.
It will be helpful to keep track of both at once
after the map stage and when reducing.
You won't need the key k2, so you can set all keys to 1 (for example).

If you get stuck on Q5, try going back to Q4 and doing it using `general_map` and `general_reduce`. Also, try reviewing the examples
in the unit tests in Q1 and Q2.

6. The `general_reduce` is partitioned by the key k2.
You can use this to easily add up values for each digit.
(There should be 10 keys, one for each digit)

7. This may be the hardest question, mainly because of the
helper function!

For the helper function, to get the digits of an integer, one way to do it is just convert the integer to a string.
You may find it helpful to have a dictinoary like
DIGIT_NAMES = { "0": zero, "1": one, "2": two, ... } etc.

Once you have the helper function, the logic for q7() should
be similar to q6().

8. load_input_bigger() should have similar logic to load_input()

11. Use set(l) to get a set from a list l.

The question is a bit of a trick question! The answer should
be very simple, if you have implemented `general_reduce` correctly.

13.
In the description of the `general_reduce` function, the key
part is "will be combined (in some order) until there
are no values of that key left".

14.
Hint 1:
Reduce is a function that basically takes two integers and returns an integer, for example
    x, y ==> x + y
If the function is like addition or multiplication, then it will
be commutative/associative, so it doesn't matter what order things are reduced in.

To get a different example, you need something that is either not commutative or not associative.

Hint 2:
There is an example of a noncommutative reducer somewhere else in the file already!

16.
You can set the parallelism to whatever you want, say,
1, 2, and 10.
reminder: the syntax is
sc.parallelize(data, parallelism)

20.
This one is hard! It should be possible to implement all the examples.
The simplest one to try is probably Fig. 7, Type 1.

For the example in Fig. 7: the way this example works is for each value v2, it gets the value `x = v2["x"]`. You can assume it returns this value x at the end. But our `general_reduce` is a bit different! How do we simulate this with our version? One way is to have, for two x values, use a reduce function that returns one of them... for example `merge(x1, x2) = x1`. The problem here is that depending on the order of the input, you might get different results once everything is merged together.

## Part 2

You can draw the graph from left-to-write or top-to-bottom.
What we're looking for here is there should be some load_input functions
at the very left (or very top),
then arrows into the various `general_map` and `general_reduce` computations that you did.
These should be shared if there were multiple questions where you used the same `general_map` function, but only if these shared the same data as input!
For example Q5/6 and Q8 should be separate nodes - although they are the same computation, they don't use the same intermediate data.
Also, your pipelines for Q8a and Q8b should be drawn as separate nodes because they use different input than Q7.

On the other hand, nodes should be drawn the same if they use exactly the same input dataset or are the exact same computation on that dataset. For example, because q1 and q2 use the same input dataset with the same level of parallelism, draw the two inputs nodes the same.

Remember that your Q16a, Q16b, and Q16c pipelines should use different
nodes, as they differ on the level of parallelism. It's OK to draw these
as all starting from one (unparallelized) dataset and then splitting into three
parallelized versions, if that's how your code is structured.

Don't worry about the specific labels on your nodes, as long as they are clearly indicate with what question they are (e.g., `q8_input`, `q8_map`, `q8_reduce`). You may choose to annotate the exact lambda function used below the node if you choose, but this is not required.

## Part 3

It will help to re-use much of the code you had working in HW1.
You should be able to use the `generate_plot` method that you created.

For the reflection, remember to ignore task and pipeline parallelism!
A simple assumption for data parallelism that we use is to imagine that your datasets
will be split in half and each worker will process them in parallel, without any
communication between them.
That means you shouldn't have to worry about any overhead of communicating between
the workers, for the purposes of the "theoretical" expectation.
Technically speaking, this assumption
is valid as long as we are only working with narrow operators, not wide ones.
