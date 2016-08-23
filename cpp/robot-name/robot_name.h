#ifndef ROBOT_NAME_H
#define ROBOT_NAME_H

namespace robot_name {
	class robot {
		private:
			std::string m_name;
			std::string gen_name();
		public:
			robot() : m_name(gen_name()) {}
			std::string name() const { return m_name; }
			void reset() { m_name = gen_name(); }
	}
}

std::string robot_name::robot::gen_name() {
	return "RX837";
}

#endif
