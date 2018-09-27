# Workshop Reference

This repository contains example implementations for the UAB ACM workshop "How To Be an Effective Programmer: Linux, Command Lines, and Editors" in both Python 3 and Java 8. All commands listed, unless otherwise stated, work for both `bash` and Windows `cmd`.

This portion of the workshop showcases three simple programs and how they might be composed together with the command line to achieve behaviour greater than their sum.

## `stdin`, `stdout`, and `stderr`
Command-line programs interface via three streams of text: `stdin`, `stdout`, and `stderr`. A program gets its input via `stdin`, its typical results are printed to `stdout`, and its errors are directed to `stderr`. The command-line can redirect these streams between programs, and between programs and files.

Following are a couple *brief* introductions to some stream operators.

### Redirecting output to a file
The `>` operator can be used to route `stdout` or `stderr` to a file. This is a good time to introduce our first program, the generator. It lives either of `generator.py` and `Generator.java` Its job is to simply generate test data. This implementation prints the numbers of the range [0, 29] to `stdout`, occasionally printing an error to `stderr` instead.

### Generator
This file 