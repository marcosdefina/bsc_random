The goal of this repo is to create a terminal visualization of ackermann's decision branching.

# The Ackermann Function

In **computability theory**, the **Ackermann function**, named after Wilhelm Ackermann, is one of the simplest and earliest-discovered examples of a **total computable function** that is not **primitive recursive**. All primitive recursive functions are total and computable, but the Ackermann function illustrates that not all total computable functions are primitive recursive.

After Ackermann's publication[^1] of his function (which had three non-negative integer arguments), many authors modified it to suit various purposes. Today, "the Ackermann function" may refer to any of numerous variants of the original function. One common version is the **two-argument Ackermann–Péter function**, developed by **Rózsa Péter** and **Raphael Robinson**. 

This function is defined using the following recurrence relation:

\[
A(m+1, n+1) = A(m, A(m+1, n))
\]

with appropriate base cases. Its value grows **very rapidly**; for example:

\[
A(4, 2) = 2^{65536} - 3
\]

This results in an integer with **19,729 decimal digits**[^2].

---

[^1]: Wilhelm Ackermann, *Zur Wertesetzung der n-stelligen Funktionen. Mathematische Annalen*, 1928.
[^2]: For more details, see the growth of the Ackermann function in computational mathematics.