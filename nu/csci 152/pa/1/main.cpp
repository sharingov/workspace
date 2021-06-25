#include "csci152_student.h"
#include <iostream>

void print(const csci152_student &student) {
  std::cout << student.get_name() << ": " << student.calculate_course_perc()
            << std::endl;
}

// This is a minimal testing file.... we will use something more complete
// for grading!!!
int main() {

  csci152_student agood("Agood Stutante", {100, 100, 100, 100},
                        {20, 20, 20, 20, 20, 20}, 100);

  csci152_student abads("Abads Tudant", {50, 0, 10, 25, 3, 12},
                        {2, 3, 7, 11, 3}, 35);

  print(agood); // should print: Agood Stutante: 100
  print(abads); // should print: Abads Tudant: 26.8333

  std::cout << "-----" << std::endl;

  csci152_student abads_clone(abads); // same as abads

  print(abads_clone); // should print: Abads Tudant: 26.8333

  abads_clone.change_name("Abads' evil twin");

  print(abads_clone); // should print: Abads' evil twin: 26.8333
  print(abads);       // should still print: Abads Tudant: 26.8333

  std::cout << "-----" << std::endl;

  abads = agood; // agood's values should be copied into abads

  agood.change_name("Elwood Stutante");

  print(abads);       // should print: Agood Stutante: 100
  print(agood);       // should print: Elwood Stutante: 100
  print(abads_clone); // should print: Abads Tudant: 26.8333

  return 0;
}
