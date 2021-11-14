# Smelly Code

## Code Smells

### Class Level Smells

- Cyclomatic Complexity:
    - Too many branches and loops.
- Large Class:
    - Trying to do too much and has too many instance variables.
- Middle Man:
    - Lots of methods are delegated to other classes
- Data Clump:
    - Bunches of data clump together in a lot of places.
- Freeloader:
    - Class doing little.

### Method Level Smells

- Long Method:
    - Long procedures that are hard to understand (implemented).
    - [Rule of 30](https://dzone.com/articles/rule-30-–-when-method-class-or)
- Message Chains:
    - Method calling a different method which calls a different method which calls a different method… and on and on.
- Too Many Parameters:
    - A very long list of parameters (implemented).
    - Parameter Number from _"Clean Code: A Handbook of Agile Software Craftsmanship"_
- God Line:
    - An insanely long line of code (implemented).
- Identifier Size:
    - The identifier is excessively short or long (implemented).