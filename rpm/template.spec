%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-ur-controllers
Version:        2.3.10
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ur_controllers package

License:        BSD-3-Clause
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-iron-angles
Requires:       ros-iron-controller-interface
Requires:       ros-iron-joint-trajectory-controller
Requires:       ros-iron-lifecycle-msgs
Requires:       ros-iron-pluginlib
Requires:       ros-iron-rclcpp-lifecycle
Requires:       ros-iron-rcutils
Requires:       ros-iron-realtime-tools
Requires:       ros-iron-std-msgs
Requires:       ros-iron-std-srvs
Requires:       ros-iron-ur-dashboard-msgs
Requires:       ros-iron-ur-msgs
Requires:       ros-iron-ros-workspace
BuildRequires:  ros-iron-ament-cmake
BuildRequires:  ros-iron-angles
BuildRequires:  ros-iron-controller-interface
BuildRequires:  ros-iron-joint-trajectory-controller
BuildRequires:  ros-iron-lifecycle-msgs
BuildRequires:  ros-iron-pluginlib
BuildRequires:  ros-iron-rclcpp-lifecycle
BuildRequires:  ros-iron-rcutils
BuildRequires:  ros-iron-realtime-tools
BuildRequires:  ros-iron-std-msgs
BuildRequires:  ros-iron-std-srvs
BuildRequires:  ros-iron-ur-dashboard-msgs
BuildRequires:  ros-iron-ur-msgs
BuildRequires:  ros-iron-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Provides controllers that use the speed scaling interface of Universal Robots.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/iron" \
    -DAMENT_PREFIX_PATH="/opt/ros/iron" \
    -DCMAKE_PREFIX_PATH="/opt/ros/iron" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Sun Aug 11 2024 Denis Stogl <denis@stoglrobotics.de> - 2.3.10-1
- Autogenerated by Bloom

* Mon Jul 01 2024 Denis Stogl <denis@stoglrobotics.de> - 2.3.9-1
- Autogenerated by Bloom

* Mon Jun 17 2024 Denis Stogl <denis@stoglrobotics.de> - 2.3.8-1
- Autogenerated by Bloom

* Sat May 18 2024 Denis Stogl <denis@stoglrobotics.de> - 2.3.7-1
- Autogenerated by Bloom

