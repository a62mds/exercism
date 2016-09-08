#ifndef SPACE_AGE_H
#define SPACE_AGE_H

namespace space_age {
  class space_age {
    private:
      const double earth_s_per_y{31557600.0};
      const double earth_y_per_s{1.0/earth_s_per_y};
      const double earth_y_per_mrc_y{0.2408467};
      const double earth_y_per_vns_y{0.61519726};
      const double earth_y_per_mrs_y{1.8808158};
      const double earth_y_per_jup_y{11.862615};
      const double earth_y_per_sat_y{29.447498};
      const double earth_y_per_urn_y{84.016846};
      const double earth_y_per_nep_y{164.79132};
      double m_age_in_seconds{0.0};
      double m_age_in_earth_y{0.0};
    public:
      space_age(double age_in_seconds) :
        m_age_in_seconds(age_in_seconds),
        m_age_in_earth_y(age_in_seconds * earth_y_per_s) {}
      double seconds() const    { return m_age_in_seconds; }
      double on_earth() const   { return m_age_in_earth_y; }
      double on_mercury() const { return m_age_in_earth_y / earth_y_per_mrc_y; }
      double on_venus() const   { return m_age_in_earth_y / earth_y_per_vns_y; }
      double on_mars() const    { return m_age_in_earth_y / earth_y_per_mrs_y; }
      double on_jupiter() const { return m_age_in_earth_y / earth_y_per_jup_y; }
      double on_saturn() const  { return m_age_in_earth_y / earth_y_per_sat_y; }
      double on_uranus() const  { return m_age_in_earth_y / earth_y_per_urn_y; }
      double on_neptune() const { return m_age_in_earth_y / earth_y_per_nep_y; }
  };
}

#endif
