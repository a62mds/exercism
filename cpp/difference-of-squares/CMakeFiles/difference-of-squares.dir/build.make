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
CMAKE_SOURCE_DIR = /home/mitch/exercism/cpp/difference-of-squares

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/mitch/exercism/cpp/difference-of-squares

# Include any dependencies generated for this target.
include CMakeFiles/difference-of-squares.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/difference-of-squares.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/difference-of-squares.dir/flags.make

CMakeFiles/difference-of-squares.dir/difference_of_squares_test.cpp.o: CMakeFiles/difference-of-squares.dir/flags.make
CMakeFiles/difference-of-squares.dir/difference_of_squares_test.cpp.o: difference_of_squares_test.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/mitch/exercism/cpp/difference-of-squares/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/difference-of-squares.dir/difference_of_squares_test.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/difference-of-squares.dir/difference_of_squares_test.cpp.o -c /home/mitch/exercism/cpp/difference-of-squares/difference_of_squares_test.cpp

CMakeFiles/difference-of-squares.dir/difference_of_squares_test.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/difference-of-squares.dir/difference_of_squares_test.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/mitch/exercism/cpp/difference-of-squares/difference_of_squares_test.cpp > CMakeFiles/difference-of-squares.dir/difference_of_squares_test.cpp.i

CMakeFiles/difference-of-squares.dir/difference_of_squares_test.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/difference-of-squares.dir/difference_of_squares_test.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/mitch/exercism/cpp/difference-of-squares/difference_of_squares_test.cpp -o CMakeFiles/difference-of-squares.dir/difference_of_squares_test.cpp.s

CMakeFiles/difference-of-squares.dir/difference_of_squares_test.cpp.o.requires:
.PHONY : CMakeFiles/difference-of-squares.dir/difference_of_squares_test.cpp.o.requires

CMakeFiles/difference-of-squares.dir/difference_of_squares_test.cpp.o.provides: CMakeFiles/difference-of-squares.dir/difference_of_squares_test.cpp.o.requires
	$(MAKE) -f CMakeFiles/difference-of-squares.dir/build.make CMakeFiles/difference-of-squares.dir/difference_of_squares_test.cpp.o.provides.build
.PHONY : CMakeFiles/difference-of-squares.dir/difference_of_squares_test.cpp.o.provides

CMakeFiles/difference-of-squares.dir/difference_of_squares_test.cpp.o.provides.build: CMakeFiles/difference-of-squares.dir/difference_of_squares_test.cpp.o

# Object files for target difference-of-squares
difference__of__squares_OBJECTS = \
"CMakeFiles/difference-of-squares.dir/difference_of_squares_test.cpp.o"

# External object files for target difference-of-squares
difference__of__squares_EXTERNAL_OBJECTS =

difference-of-squares: CMakeFiles/difference-of-squares.dir/difference_of_squares_test.cpp.o
difference-of-squares: CMakeFiles/difference-of-squares.dir/build.make
difference-of-squares: /usr/lib/i386-linux-gnu/libboost_unit_test_framework.a
difference-of-squares: /usr/lib/i386-linux-gnu/libboost_date_time.a
difference-of-squares: /usr/lib/i386-linux-gnu/libboost_regex.a
difference-of-squares: CMakeFiles/difference-of-squares.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable difference-of-squares"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/difference-of-squares.dir/link.txt --verbose=$(VERBOSE)
	./difference-of-squares

# Rule to build all files generated by this target.
CMakeFiles/difference-of-squares.dir/build: difference-of-squares
.PHONY : CMakeFiles/difference-of-squares.dir/build

CMakeFiles/difference-of-squares.dir/requires: CMakeFiles/difference-of-squares.dir/difference_of_squares_test.cpp.o.requires
.PHONY : CMakeFiles/difference-of-squares.dir/requires

CMakeFiles/difference-of-squares.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/difference-of-squares.dir/cmake_clean.cmake
.PHONY : CMakeFiles/difference-of-squares.dir/clean

CMakeFiles/difference-of-squares.dir/depend:
	cd /home/mitch/exercism/cpp/difference-of-squares && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/mitch/exercism/cpp/difference-of-squares /home/mitch/exercism/cpp/difference-of-squares /home/mitch/exercism/cpp/difference-of-squares /home/mitch/exercism/cpp/difference-of-squares /home/mitch/exercism/cpp/difference-of-squares/CMakeFiles/difference-of-squares.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/difference-of-squares.dir/depend
