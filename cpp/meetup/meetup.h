#ifndef MEETUP_H
#define MEETUP_H

#include "boost/date_time/gregorian/gregorian.hpp"

namespace meetup {

  using Tmonth = boost::date_time::months_of_year;
  using Tyear = int;
  using Tdate = boost::gregorian::date;

  class scheduler {
  public:
    scheduler(Tmonth month, Tyear year) : _month(month), _year(year) {}
    Tdate monteenth() const;
    /*
    Tdate tuesteenth() const;
    Tdate wednesteenth() const;
    Tdate thursteenth() const;
    Tdate friteenth() const;
    Tdate saturteenth() const;
    Tdate sunteenth() const;
    */
  private:
    Tmonth _month;
    Tyear _year;
  };
}

#endif
