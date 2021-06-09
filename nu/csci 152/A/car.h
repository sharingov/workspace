#ifndef CAR_H_
#define CAR_H_

#include <stdexcept>

using namespace std;

class car {
  bool engine_on;
  double speed;

  const double max_speed;
  const string vin;

public:
  car(double max_spd, string veh_in);

  bool turn_on();
  bool turn_off();

  void press_brake();
  void press_gas_pedal(double pressure);

  bool is_engine_on() const;
  double get_max_speed() const;
  double get_speed() const;
  string get_vin() const;

  ~car();
};

#endif
