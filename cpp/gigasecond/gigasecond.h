#ifndef GIGASECOND_H
#define GIGASECOND_H

#include<boost/date_time/gregorian/gregorian.hpp>

namespace gigasecond {
	boost::gregorian::date advance(boost::gregorian::date bday) {
		return bday + boost::gregorian::date_duration(1e9/86400);
	}
}

#endif
