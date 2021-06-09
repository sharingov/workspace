#include "car.cpp"
#include <iostream>
#include <stdexcept>

#define rep(b) for (int i = 0; i < b; i++)

using namespace std;

int main() {
  car my_car(180.0, "FHT455");
  my_car.turn_on();

  rep(5) {
    cout << "pressing gas..." << endl;
    my_car.press_gas_pedal(40);
  }

  my_car.press_brake();

  try {
    my_car.turn_off();
  } catch (invalid_argument &ex) {
    cout << ex.what() << " bruh" << endl;
  }

  return 0;
}
