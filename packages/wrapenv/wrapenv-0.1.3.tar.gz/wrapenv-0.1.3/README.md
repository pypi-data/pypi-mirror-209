# WrapEnv

An environment that can hold several callable functions along with pre- and post-processing
functions and auxilary environment. It is intended to be used as a wrapper for a function that
is to be called in a different environment than the one it was defined in.

## Installation

As usual, you can install the package using pip:

```bash
pip install wrapenv
```

## Usage

The package provides an instance of the class `ENVIRONMENT` that can be used as a decorator for functions that
are to be wrapped. As the instance is a global variable, it can be used from anywhere in the code (even in other modules).

The example in the [EXAMPLES](examples/README.md) folder demonstrates how to use the `ENVIRONMENT` instance to wrap a 
function that is to be called in a different environment than the one it was defined in.

