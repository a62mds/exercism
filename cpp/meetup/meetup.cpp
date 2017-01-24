#include "meetup.h"
using namespace meetup;
using namespace boost::gregorian;


Tdate scheduler::monteenth() const {
  Tdate answer{2013, boost::gregorian::May, 13};
  return answer;
}
