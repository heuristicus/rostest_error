cmake_minimum_required(VERSION 3.0.2)
project(rostest_example)

find_package(catkin REQUIRED COMPONENTS rostest rosunit)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES rostest_example
#  CATKIN_DEPENDS other_catkin_pkg
#  DEPENDS system_lib
)
include_directories(
# include
# ${catkin_INCLUDE_DIRS}
)

if(CATKIN_ENABLE_TESTING)
  find_package(rostest REQUIRED)
  add_rostest(test/launch/test_error.launch)
endif()