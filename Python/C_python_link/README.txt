
*********************************************
*                                           *
*  Python to C_Program Interface examples   *
*                                           *
*********************************************

1. First compile C program, generate .so file

   linux> gcc -fPIC my_test.c -shared -o my_test.so

2. To run python script:

   linux> python my_test.py
