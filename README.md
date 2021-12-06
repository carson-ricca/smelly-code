# Smelly Code

## Code Smells

### Class Level Smells

- Cyclomatic Complexity:
    - Too many branches and loops.
    - To detect this I use the idea that the cyclomatic complexity involves counting entry points into branches or
      loops. For every `ast.ClassDef` I iterate over every line within the class, I then check if this line contains any
      of the key values in a constant list. This list contains key values that indicate an entry point to a loop or
      branch. After all these have been counted for the class, I compare the total cyclomatic complexity with another
      constant to determine if it is too much, in that case the code smell is detected.
- Large Class:
    - Trying to do too much and has too many instance variables.
    - This is detected in the same way as lazy class but uses a different constant to determine if the class is too
      large.
- Middle Man:
    - Lots of methods are delegated to other classes.
    - For this I walk through the AST, and dig deeper into each `ast.ClassDef` node. I then look within each of these
      nodes for all the `ast.FunctionDef` nodes. I then determine if each function only contains calls to other
      functions, and doesn't contain any code itself. I then compare the percentage of functions that delegate their
      responsibilities vs. the total number of functions in the class. If the percentage is greater than a set constant
      it is a middle-man.
- Data Class:
    - Classes have nothing but fields, and setters or getters for these fields.
    - To detect this class smell, I iterate over the AST and check each `ast.ClassDef`. Within each of these nodes I
      then use helper functions to detect if the class only contains fields and/or getters/setters.
- Lazy Class:
    - Class doing little.
    - In order to detect this code smell, I iterate over every node in the AST looking for the `ast.ClassDef` type. I
      then check the line length of the class against a predetermined constant to determine if it is a lazy class.

### Method Level Smells

- Long Method:
    - Long procedures that are hard to understand.
    - [Rule of 30](https://dzone.com/articles/rule-30-–-when-method-class-or).
    - In order to determine if a function is too long, I iterate over every node in the AST, when I find
      a `ast.FunctionDef` node, I then determine the total lines that make up this function. I then compare this value
      to a set constant and if it exceeds this constant then the function length is too long.
- Method Chains:
    - Method calling a different method which calls a different method which calls a different method… and on and on (
      implemented).
    - To detect this code smell I iterate over every node in the AST for each file, if the node is of the
      type `ast.Call` then if the node has a `value` attribute. Having this attribute means it makes another function
      call. If this happened on the same line then it is a method chain.
- Too Many Parameters:
    - A very long list of parameters.
    - Parameter Number from _"Clean Code: A Handbook of Agile Software Craftsmanship"_.
    - To detect this code smell I iterate through the nodes in the AST, if it is a `ast.FunctionDef` I then look at the
      arguments and compare the amount of arguments against a constant to determine if it contains too many.
- God Line:
    - An insanely long line of code.
    - Number of characters per line comes from PyCharm's warning.
    - To determine if a line is too long, I iterate through every line in every file and check the length of the line
      against a pre-determined constant.
- Identifier Size:
    - The identifier is excessively short or long.
    - To detect this code smell I iterate over every node in the AST, I then check if it is of the following
      types: `ast.ClassDef`, `ast.FunctionDef`, or `ast.name`. If it is any of these types then it is an identifier. I
      then compare the name for the identifier to a constant to determine if it is either too short or too long.