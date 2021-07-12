#include "stack.h"
#include <math.h>
#include <ostream>

using namespace std;

// Copy constructor
stack::stack(const stack &stk)
    : stack_size(stk.stack_size), array_capacity(stk.array_capacity) {
  values = new int[array_capacity];
  for (size_t i = 0; i < stack_size; i++) {
    values[i] = stk.values[i];
  }
}

// Initializer list constructor
stack::stack(initializer_list<int> ilist)
    : stack_size(ilist.size()),
      array_capacity((int)(5 * pow(2, ceil(log2(stack_size / 5 + 1))))) {
  size_t i = 0;
  values = new int[array_capacity];
  for (auto a : ilist) {
    values[i] = a;
    i++;
  }
}

// Copy assignment
stack &stack::operator=(const stack &stk) {
  if (array_capacity != stk.array_capacity) {
    array_capacity = stk.array_capacity;
    delete[] values;
    values = new int[array_capacity];
  }
  stack_size = stk.stack_size;
  for (size_t i = 0; i < stack_size; i++) {
    values[i] = stk.values[i];
  }
  return *this;
}

// Insert an item at the top of the stack
void stack::push(int val) {
  if (stack_size == array_capacity) {
    array_capacity *= 2;
    int *temp = new int[array_capacity];
    for (size_t i = 0; i < stack_size; i++) {
      temp[i] = values[i];
    }
    delete[] values;
    values = new int[array_capacity];
    for (size_t i = 0; i < stack_size; i++) {
      values[i] = temp[i];
    }
    delete[] temp;
  }
  values[stack_size] = val;
  stack_size++;
}

// Returns the value of the topmost item of the stack;
// throws an exception if the stack is empty
int stack::peek() const {
  if (empty()) {
    throw "empty";
  }
  return values[stack_size - 1];
}

// Remove the topmost item from the stack
// throws an exception if the stack is empty
void stack::pop() {
  if (empty()) {
    throw "empty";
  }
  stack_size--;
}
// Remove everything from the stack
void stack::clear() { stack_size = 0; }

// Returns the number of items on the stack
size_t stack::size() const { return stack_size; }

// Returns whether or not the stack is currently empty
bool stack::empty() const { return stack_size == 0; }

// Destructor
stack::~stack() { delete[] values; }
