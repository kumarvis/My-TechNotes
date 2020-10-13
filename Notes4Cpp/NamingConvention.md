# CPP Naming Conventions

This is set of 10 simple naming covention for cpp coding. Make code more structured and readable.

## 1. Class Names:


1. First character in a name must be UPPER CASE
2. No underscores (_) are permitted
3. Use upper case letters as word separators, lower case for the rest of a word.
4. NOUN followed by VERB.

```
Example: class OdeSolver
```

## 2. Method and Function Names

1. Classes are often Nouns. By making function names VERBS and following other naming conventions programs can be read more naturally. Function Name Should start with CAPITAL Letter.
2. Prefixes are sometimes useful. Example: is, has, get, set etc.
3. Suffixes are sometimes useful. Example: max, count

```
class OdeSolver{
public:
    int SolveEquation();
    void HandleError();
    bool isEmpty();
    int getCurrentValue();
};
```

## 3. Pointer Variables:
1. Pointers should be prepended by a ’p’ in most cases. Place the * close
to the variable name rather than the pointer type. 

```
String *pName= new String
```

## 4. Class Attribute Names:

1. Private attribute names should be prepended with the underscore
character ’m’.
2. ’m’ always precedes other name modifiers like ’p’ for pointer.

```
Class StudentRecord{
private:
    int mPercentMarks;
    String *mpName;
};
```

## 5. Reference Variables and Functions Returning References:

1. References should be prepended with ’r’. 

```
void TestConveyorStart(StatusInfo& rStatus) ;

StatusInfo& rGetStatus();
```

## 6. Method Argument Names: The first character or word should be

1. The first character or word should be lower case. All word beginnings after the first letter should be upper case.

```
int StartYourEngines( Engine& rSomeEngine, Engine anotherEngine);
```

## 7. GLOBAL Variables: 

1. Should be prepended with a 'g'. 

```
Logger* gpLog; //g=global, p=pointer
```

## 8. Static and Const Variables:
1. GLOBAL CONST: All caps with (_) separators. 

```
const double TWO_PI = 6.28318531;
```

2. CLASS CONST: Use k before the name. 

```
const int kDaysInAWeek = 7;
```

3. Static Variable: Static variables should be prepended with ’s’.

```
static StatusInfo sStatus;
```

## 9. Variable Names on Stack: 

1. Use all lower-case letters, separated with
(_) as word separator. 

```
Time time_of_error;
```

## 10. #define GUARDS: 
The format of the symbol name should be

`<PROJECT>_<PATH>_<FILE>_H_`

For example, the file
foo/src/bar/baz.h in project foo should have the following guard:

```
#ifndef FOO_BAR_BAZ_H_
#define FOO_BAR_BAZ_H_
...
...

#endif //FOO_BAR_BAZ_H_
```

### <ins>References:</ins>

1. [Chaste CS OX UK ](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=5&ved=2ahUKEwj_hPKzpfnoAhXWXisKHdaPDioQFjAEegQIBBAC&url=https%3A%2F%2Fchaste.cs.ox.ac.uk%2Ftrac%2Fraw-attachment%2Fwiki%2FCodingStandardsStrategy%2FcodingStandards.pdf&usg=AOvVaw0luvSMRxUSnHMf4StikNh-)

2. [Cpp Coding Standard CMU](https://users.ece.cmu.edu/~eno/coding/CppCodingStandard.html#classnames)