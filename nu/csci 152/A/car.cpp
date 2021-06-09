#include "car.h"
#include <iostream>
#include <math.h>
#include <stdio.h>

using namespace std;

car::car(double max_spd, string veh_in)
    : engine_on(false), speed(0.0), max_speed(max_spd), vin(veh_in) {}

bool car ::turn_on() {
  if (engine_on) {
    return false;
  }
  engine_on = true;
  return true;
}

bool car ::turn_off() {
  if (!engine_on) {
    return false;
  }
  if (speed > 0) {
    throw invalid_argument("not allowed");
  }
  engine_on = false;
  return true;
}

void car::press_gas_pedal(double pressure) {
  if (pressure < 0.0) {
    throw invalid_argument("negative pressure");
  }
  if (engine_on) {
    speed = min(max_speed, speed + pressure);
  }
}

void car::press_brake() { speed = 0; }

bool car::is_engine_on() const { return engine_on; }
double car::get_max_speed() const { return max_speed; }
double car::get_speed() const { return speed; }
string car::get_vin() const { return vin; }

car::~car() {}
