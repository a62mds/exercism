# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/mitch/exercism/cpp/bob

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/mitch/exercism/cpp/bob

# Include any dependencies generated for this target.
include CMakeFiles/bob.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/bob.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/bob.dir/flags.make

CMakeFiles/bob.dir/bob_test.cpp.o: CMakeFiles/bob.dir/flags.make
CMakeFiles/bob.dir/bob_test.cpp.o: bob_test.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/mitch/exercism/cpp/bob/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/bob.dir/bob_test.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/bob.dir/bob_test.cpp.o -c /home/mitch/exercism/cpp/bob/bob_test.cpp

CMakeFiles/bob.dir/bob_test.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/bob.dir/bob_test.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/mitch/exercism/cpp/bob/bob_test.cpp > CMakeFiles/bob.dir/bob_test.cpp.i

CMakeFiles/bob.dir/bob_test.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/bob.dir/bob_test.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/mitch/exercism/cpp/bob/bob_test.cpp -o CMakeFiles/bob.dir/bob_test.cpp.s

CMakeFiles/bob.dir/bob_test.cpp.o.requires:
.PHONY : CMakeFiles/bob.dir/bob_test.cpp.o.requires

CMakeFiles/bob.dir/bob_test.cpp.o.provides: CMakeFiles/bob.dir/bob_test.cpp.o.requires
	$(MAKE) -f CMakeFiles/bob.dir/build.make CMakeFiles/bob.dir/bob_test.cpp.o.provides.build
.PHONY : CMakeFiles/bob.dir/bob_test.cpp.o.provides

CMakeFiles/bob.dir/bob_test.cpp.o.provides.build: CMakeFiles/bob.dir/bob_test.cpp.o

# Object files for target bob
bob_OBJECTS = \
"CMakeFiles/bob.dir/bob_test.cpp.o"

# External object files for target bob
bob_EXTERNAL_OBJECTS =

bob: CMakeFiles/bob.dir/bob_test.cpp.o
bob: CMakeFiles/bob.dir/build.make
bob: /usr/lib/i386-linux-gnu/libboost_unit_test_framework.a
bob: /usr/lib/i386-linux-gnu/libboost_date_time.a
bob: /usr/lib/i386-linux-gnu/libboost_regex.a
bob: CMakeFiles/bob.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable bob"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/bob.dir/link.txt --verbose=$(VERBOSE)
	./bob

# Rule to build all files generated by this target.
CMakeFiles/bob.dir/build: bob
.PHONY : CMakeFiles/bob.dir/build

CMakeFiles/bob.dir/requires: CMakeFiles/bob.dir/bob_test.cpp.o.requires
.PHONY : CMakeFiles/bob.dir/requires

CMakeFiles/bob.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/bob.dir/cmake_clean.cmake
.PHONY : CMakeFiles/bob.dir/clean

CMakeFiles/bob.dir/depend:
	cd /home/mitch/exercism/cpp/bob && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/mitch/exercism/cpp/bob /home/mitch/exercism/cpp/bob /home/mitch/exercism/cpp/bob /home/mitch/exercism/cpp/bob /home/mitch/exercism/cpp/bob/CMakeFiles/bob.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/bob.dir/depend

