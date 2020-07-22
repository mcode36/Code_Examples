#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include "my_test.h"

// Return greetings (string) 
const char *hello(char* name) {
   char hello[] = "Hello ";
   char excla[] = "!\n";
   char *greeting = malloc ( sizeof(char) * ( strlen(name) + strlen(hello) + strlen(excla) + 1 ) );
   strcpy(greeting, hello);
   strcat(greeting, name);
   strcat(greeting, excla);
   return greeting;
}

// Add two number and return integer
int addNum(int a, int b) {
   int nAdd = a + b;
   return nAdd;
}

// Add two float number and return float
float add_float(float a, float b){
   return a + b;
}

// Array addition (int)
int add_int_array(int *a, int *b, int *c, int n){
   int i;
   for (i=0; i<n; i++) {
      c[i] = a[i] + b[i];
   }
   return 0;
}

// Array division (float)
float array_div(float *a, float *b, int n){
   int i;
   for (i=0; i<n; i++) {
      b[i] = a[i] / 2.0;
   }
   return 0;
}
 