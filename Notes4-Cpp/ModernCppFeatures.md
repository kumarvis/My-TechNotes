# Lambda

## What is Lambda?
C++ 11 introduced **lambda** expression is a convenient way of defining an anonymous function object, to allow us write an inline function which can be used for short snippets of code that are not going to be reuse and not worth naming.

```cpp
auto isOdd = [](int candidate) {return candidate %2 !=0; } ;
```
