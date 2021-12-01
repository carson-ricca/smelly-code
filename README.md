# Smelly Code

## Code Smells

### Class Level Smells

- Cyclomatic Complexity:
    - Too many branches and loops.
- Large Class:
    - Trying to do too much and has too many instance variables (implementation completed).
- Middle Man:
    - Lots of methods are delegated to other classes (implemented).
- Data Class:
    - Classes have nothing but fields, and setters or getters for these fields (implemented).
- Lazy Class:
    - Class doing little (implementation completed).

### Method Level Smells

- Long Method:
    - Long procedures that are hard to understand (implemented).
    - [Rule of 30](https://dzone.com/articles/rule-30-–-when-method-class-or)
- Method Chains:
    - Method calling a different method which calls a different method which calls a different method… and on and on (
      implemented).
- Too Many Parameters:
    - A very long list of parameters (implemented).
    - Parameter Number from _"Clean Code: A Handbook of Agile Software Craftsmanship"_
- God Line:
    - An insanely long line of code (implemented).
- Identifier Size:
    - The identifier is excessively short or long (implemented).