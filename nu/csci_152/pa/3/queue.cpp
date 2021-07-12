#include "queue.h"
#include <iostream>
#include <math.h>
#include <stdio.h>

using namespace std;

// Copy constructor
queue ::queue(const queue &q) {
  queue_size = 0;
  front = nullptr;
  back = nullptr;
  node *temp = q.front;
  while (temp != nullptr) {
    push(temp->value);
    temp = temp->next;
  }
}

// Initializer list constructor
queue ::queue(std::initializer_list<int> ilist) {
  queue_size = 0;
  front = nullptr;
  back = nullptr;
  for (auto a : ilist) {
    push(a);
  }
}

// Copy assignment
queue &queue ::operator=(const queue &q) {
  clear();
  queue_size = 0;
  node *temp = q.front;
  while (temp != nullptr) {
    push(temp->value);
    temp = temp->next;
  }
  return *this;
}

// Insert an item at the back of the queue
void queue ::push(int val) {
  node *temp = new node(val);
  if (back == nullptr) {
    front = temp;
    back = temp;
  } else {
    back->next = temp;
    back = back->next;
  }
  queue_size++;
}

// Returns the value of the front-most item of the queue;
// throws an exception if the queue is empty
int queue ::peek() const {
  if (empty()) {
    throw "empty";
  }
  return front->value;
}

// Remove the front-most item from the queue
// throws an exception if the queue is empty
void queue ::pop() {
  if (empty()) {
    throw "empty";
  }
  node *temp = front;
  front = front->next;
  delete temp;
  queue_size--;
}

// Remove everything from the queue
void queue ::clear() {
  while (!empty()) {
    node *temp = front;
    front = front->next;
    delete temp;
    queue_size--;
  }
  front = nullptr;
  back = nullptr;
}

// Returns the number of items on the queue
size_t queue ::size() const { return queue_size; }

// Returns whether or not the queue is currently empty
bool queue ::empty() const { return queue_size == 0; }

// Destructor
queue::~queue() { clear(); }
