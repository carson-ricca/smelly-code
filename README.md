# Smelly Code

## Running the Project

Everything required to run the project including all necessary data is already in the project. In order to run the
project ensure that `Python 3` is installed on your machine, then continue with the following steps:

> 1. Run `pip install -r requirements.txt`
> 2. Run `python3 main.py` to run the code detection on the _Canvas Gamification_ repository.
> 3. The plot of all code smells for the repository will be displayed upon completion of the program.
> 4. The code smells will be exported to `output/code_smells.csv`.
> 5. To run the unit tests, use the command `python3 -m unittest discover -s tests`.

## Project Status

- The project is currently at a place where I am confident that everything is completed properly.
- There could be small room for improvements in the detection methods that might improve the accuracy. I do not believe
  this would increase the amount detected by much.
- The accuracy can also be fine-tuned by changing the values used for detection in `constants.py`, I determined these
  initial values based on research, and my own personal development experience. A better selection for these values
  could be possibly be proposed by an expert and would help increase the accuracy of the detection.
- Testing Strategy:
    - In order to test that my code smell detection is working as expected I implemented unit-testing that tests the
      detection of the ten code smells I selected for this project.

## File Structure

```
.
+-- .github/workflows (contains workflow for automated testing on GitHub)
|   +-- ci.yml
+-- data
|   +-- canvas-gamification-master.zip (raw repo downloaded from GitHub)
|   +-- canvas-gamification-master (unzipped data folder)
+-- output (contains exported csv with all code smells)
|   +-- code_smells.csv
+-- scripts (contains all code smell detection)
|   +-- __init__.py
|   +-- detect_cyclomatic_complexity.py
|   +-- detect_data_class.py
|   +-- detect_function_chains.py
|   +-- detect_function_length.py
|   +-- detect_god_line.py
|   +-- detect_identifier_size.py
|   +-- detect_large_class.py
|   +-- detect_lazy_class.py
|   +-- detect_many_parameters.py
|   +-- detect_middle_man.py
+-- test_files (ensure code smell detection works as expected)
|   +-- __init__.py
|   +-- test.py
|   +-- test_cyclomatic_complexity.py
|   +-- test_data_class.py
|   +-- test_large_class.py
|   +-- test_method_class.py
|   +-- test_middle_man.py
+-- tests (test used to ensure code works as expected)
|   +-- __init__.py
|   +-- test_code_smell_detection.py
+-- util (util functions used across scripts)
|   +-- __init__.py
|   +-- compute_length.py
|   +-- file.py
+-- constants.py
+-- detect_code_smells.py
+-- export_dataframe.py
+-- main.py
+-- plot_dataframe.py
+-- README.md
+-- requirements.txt
```

## Project Plan

- Week 8:
    - Working on the project plan.
    - Exploring different code smells that exist, and researching the most common ones.
    - Might need to use GitHub API will need investigating.
- Week 9:
    - Set up the repository.
    - Basic python setup, structure, etc…
    - Define class level and method level code smells.
    - Define them in English.
- Week 10:
    - Pick 5 smells from each category that I would like to identify.
    - Set up models for each smell, and its attributes, description, etc...
- Week 11:
    - Begin writing code to determine smells.
    - Begin writing test files to test the above code.
- Week 12:
    - Finish functions for determining smells.
    - Finish test files.
    - Test on the provided repository.
    - Start on presentation/findings.
- Week 13:
    - Finish presentation/report/findings.
- Week 14:
    - Finalize and submit required deliverables.

## Code Smells

### Total Code Smells in Repository

- [https://docs.google.com/spreadsheets/d/1tJXRMzRGm2gtFQvw7nRJ_2UiIBiHPKie0t_1i0GLrAg/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1tJXRMzRGm2gtFQvw7nRJ_2UiIBiHPKie0t_1i0GLrAg/edit?usp=sharing)
    - Total counts for all code smells in the repository are at the bottom of the above file.

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
    - ~~To detect this code smell I iterate over every node in the AST for each file, if the node is of the
      type `ast.Call` then if the node has a `value` attribute. Having this attribute means it makes another function
      call. If this happened on the same line then it is a method chain.~~
    - The above was my initial implementation of detection, but it turned out to be very inaccurate. I have improved it,
      and it now makes much more sense. I iterate over every line in each file, I then compare the count of `').'` for
      each line against a constant value that is the number of allowed function chains.
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