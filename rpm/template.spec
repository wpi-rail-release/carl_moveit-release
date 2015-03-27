Name:           ros-indigo-carl-moveit
Version:        0.0.9
Release:        0%{?dist}
Summary:        ROS carl_moveit package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/carl_moveit
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-carl-description
Requires:       ros-indigo-control-msgs
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-joint-state-publisher
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-moveit-planners-ompl
Requires:       ros-indigo-moveit-ros-move-group
Requires:       ros-indigo-moveit-ros-planning-interface
Requires:       ros-indigo-rail-manipulation-msgs
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-wpi-jaco-msgs
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-carl-description
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-control-msgs
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-moveit-ros-planning-interface
BuildRequires:  ros-indigo-rail-manipulation-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-wpi-jaco-msgs

%description
MoveIt! Configuration and ROS Interface for CARL

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Mar 27 2015 David Kent <davidkent@wpi.edu> - 0.0.9-0
- Autogenerated by Bloom

* Tue Mar 24 2015 David Kent <davidkent@wpi.edu> - 0.0.8-0
- Autogenerated by Bloom

* Tue Feb 17 2015 David Kent <davidkent@wpi.edu> - 0.0.7-0
- Autogenerated by Bloom

* Fri Feb 06 2015 David Kent <davidkent@wpi.edu> - 0.0.6-0
- Autogenerated by Bloom

* Wed Jan 21 2015 David Kent <davidkent@wpi.edu> - 0.0.5-0
- Autogenerated by Bloom

* Wed Jan 21 2015 David Kent <davidkent@wpi.edu> - 0.0.4-1
- Autogenerated by Bloom

* Fri Jan 16 2015 David Kent <davidkent@wpi.edu> - 0.0.4-0
- Autogenerated by Bloom

* Tue Dec 02 2014 David Kent <davidkent@wpi.edu> - 0.0.3-0
- Autogenerated by Bloom

* Mon Nov 03 2014 David Kent <davidkent@wpi.edu> - 0.0.2-0
- Autogenerated by Bloom

* Fri Oct 31 2014 David Kent <davidkent@wpi.edu> - 0.0.1-0
- Autogenerated by Bloom
