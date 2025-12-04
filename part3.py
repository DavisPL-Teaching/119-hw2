"""
Part 3: Measuring Performance

Now that you have drawn the dataflow graph in part 2,
this part will explore how performance of real pipelines
can differ from the theoretical model of dataflow graphs.

We will measure the performance of your pipeline
using your ThroughputHelper and LatencyHelper from HW1.

=== Coding part 1: making the input size and partitioning configurable ===

We would like to measure the throughput and latency of your PART1_PIPELINE,
but first, we need to make it configurable in:
(i) the input size
(ii) the level of parallelism.

Currently, your pipeline should have at least two inputs, load_input() and load_input_bigger().

You will need to change part1 by making the following additions:

- Make load_input and load_input_bigger take arguments that can be None, like this:

    def load_input(N=None, P=None)

    def load_input_bigger(N=None, P=None)

You will also need to do the same thing to q8_a, q8_b, and q16_a, q16_b, q16_c:

    def q8_a(N=None, P=None)

    def q8_b(N=None, P=None)

    def q16_a(N=None, P=None):

    def q16_b(N=None, P=None):

    def q16_c(N=None, P=None):

Finally, your Q20 pipeline also uses a similar dataset as the above, please also make that one parametric:

    def q20(N=None, P=None):

Don't make any other changes to the function signatures.

Here, the argument N = None is an optional parameter that, if specified, gives the size of the input
to be considered, and P = None is an optional parameter that, if specifed, gives the level of parallelism
(number of partitions) in the RDD.

You will need to make both functions work with the new signatures.
Be careful to check that the above changes should preserve the existing functionality of part1
(so python3 part1.py should still give the same output as before!)

Once this is done, define a *new* version of the PART_1_PIPELINE, below,
that takes as input the parameters N and P.
(This time, you don't have to consider the None case.)
You should not modify the existing PART_1_PIPELINE.

You may either delete the parts of the code that save the output file, or change these to a different output file like part1-answers-temp.txt.

- Please note: Spark will have issues if you load the `sc.SparkContext` more than once! This is why in Part 1
  we have it so that sc.SparkContext is only loaded if part1.py is run directly.
"""

# Imports and spark context
import part1
import pyspark
from pyspark.sql import SparkSession
if __name__ == "__main__":
    spark = SparkSession.builder.appName("DataflowGraphExample").getOrCreate()
    sc = spark.sparkContext

def PART_1_PIPELINE_PARAMETRIC(N, P):
    """
    TODO: Follow the same logic as PART_1_PIPELINE
    N = number of inputs
    P = parallelism (number of partitions)
    (You can copy the code here), but make the following changes:
    - load_input should use an input of size N.
    - load_input_bigger (including q8_a and q8_b) should use an input of size N.
    - both of these should return an RDD with level of parallelism P (number of partitions = P).
    """
    raise NotImplementedError

"""
=== Coding part 2: measuring the throughput and latency ===

Now we are ready to measure the throughput and latency.

To start, copy the code for ThroughputHelper and LatencyHelper from HW1 into this file.

Then, please measure the performance of PART1_PIPELINE as a whole
using five levels of parallelism:
- parallelism 1
- parallelism 2
- parallelism 4
- parallelism 8
- parallelism 16

For each level of parallelism, you should measure the throughput and latency as the number of input
items increases, using the following input sizes:
- N = 1, 10, 100, 1000, 10_000, 100_000, 1_000_000

- Note that the larger sizes may take a while to run (for example, up to 10 minutes). You can try with smaller sizes to test your code first.

- **Time limit:** The entire part1.py plus part3.py should run in at most 30 minutes total!
  Here is a reference point from our testing of the official solution:
  - `time python3 part1.py`: about 30 seconds
  - `time python3 part3.py`: about 5 minutes

You can generate any plots you like (for example, a bar chart or an x-y plot on a log scale,)
but store them in the following 10 files,
where the file name corresponds to the level of parallelism:

output/part3-throughput-1.png
output/part3-throughput-2.png
output/part3-throughput-4.png
output/part3-throughput-8.png
output/part3-throughput-16.png
output/part3-latency-1.png
output/part3-latency-2.png
output/part3-latency-4.png
output/part3-latency-8.png
output/part3-latency-16.png

Clarifying notes:

- To control the level of parallelism, use the N, P parameters in your PART_1_PIPELINE_PARAMETRIC above.

- Make sure you sanity check the output to see if it matches what you would expect! The pipeline should run slower
  for larger input sizes N (in general) and for fewer number of partitions P (in general).

- For throughput, the "number of input items" should be 2 * N -- that is, N input items for load_input, and N for load_input_bigger.

- For latency, please measure the performance of the code on the entire input dataset
(rather than a single input row as we did on HW1).
MapReduce is batch processing, so all input rows are processed as a batch
and the latency of any individual input row is the same as the latency of the entire dataset.
That is why we are assuming the latency will just be the running time of the entire dataset.

- Please set `NUM_RUNS` to `1` if you haven't already. Note that this will make the values for low numbers (like `N=1`, `N=10`, and `N=100`) vary quite unpredictably.

===== Warning! =====

If your code is taking way too long to run, or if the latency seems the same for all runs, read here!

Python lambdas are weird! If using a Python lambda to call into your PART_1_PIPELINE_PARAMETRIC, you need
to do it like so:

  lambda N=N, P=P: PART_1_PIPELINE_PARAMETRIC(N, P)

The reason for the N=N, P=P is so that the PART_1_PIPELINE_PARAMETRIC captures N and P by value, rather
than by reference.
If you debug the code by having it print N and P on iteration, you will see that they all default to the
latest value of N, even when you vary N using a for loop - because N is one variable, all references to
N will remain the same.

To check if this is occuring, check your latency plot! Latency should not be constant, it should increase for
the larger runs.

This is a well-known issue in Python when working with lambdas.
For further reading, see for example:
https://stackoverflow.com/questions/69326838/how-to-capture-a-value-in-a-python-closure
https://www.reddit.com/r/ProgrammingLanguages/comments/bxxx7x/python_closures_are_capturing_by_reference_should/
"""

# Copy in ThroughputHelper and LatencyHelper

# Insert code to generate plots here as needed

"""
=== Reflection part ===

Once this is done, write a reflection and save it in
a text file, output/part3-reflection.txt.

I would like you to think about and answer the following questions:

1. What would we expect from the throughput and latency
of the pipeline, given only the dataflow graph?

Use the information we have seen in class. In particular,
how should throughput and latency change when we double the amount of parallelism?

Please ignore pipeline and task parallelism for this question.
The parallelism we care about here is data parallelism.

2. In practice, does the expectation from question 1
match the performance you see on the actual measurements? Why or why not?

State specific numbers! What was the expected throughput and what was the observed?
What was the expected latency and what was the observed?

3. Finally, use your answers to Q1-Q2 to form a conjecture
as to what differences there are (large or small) between
the theoretical model and the actual runtime.
Name some overheads that might be present in the pipeline
that are not accounted for by our theoretical model of
dataflow graphs that could affect performance.

You should list an explicit conjecture in your reflection, like this:

    Conjecture: I conjecture that ....

You may have different conjectures for different parallelism cases.
For example, for the parallelism=4 case vs the parallelism=16 case,
if you believe that different overheads are relevant for these different scenarios.

=== Grading notes ===

- Don't forget to fill out the entrypoint below before submitting your code!
Running python3 part3.py should work and should re-generate all of your plots in output/.

- You should modify the code for `part1.py` directly. Make sure that your `python3 part1.py` still runs and gets the same output as before!

- Your larger cases may take a while to run, but the entirety of your code
  (part1.py + part3.py) must terminate within the 30 minute time limit as specified above.

- In the reflection, please write at least a paragraph for each question. (5 sentences each)

- Please include specific numbers in your reflection (particularly for Q2).

=== Entrypoint ===
"""

if __name__ == '__main__':
    print("Complete part 3. Please use the main function below to generate your plots so that they are regenerated whenever the code is run:")

    print("[add code here]")
    # TODO: add code here
