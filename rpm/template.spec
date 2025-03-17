%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-ur-calibration
Version:        2.6.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ur_calibration package

License:        BSD-3-Clause
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-humble-rclcpp
Requires:       ros-humble-ur-client-library
Requires:       ros-humble-ur-robot-driver
Requires:       yaml-cpp-devel
Requires:       ros-humble-ros-workspace
BuildRequires:  eigen3-devel
BuildRequires:  ros-humble-ament-cmake
BuildRequires:  ros-humble-rclcpp
BuildRequires:  ros-humble-ur-client-library
BuildRequires:  ros-humble-ur-robot-driver
BuildRequires:  yaml-cpp-devel
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-cmake-gmock
BuildRequires:  ros-humble-ament-cmake-gtest
BuildRequires:  ros-humble-ament-lint-auto
BuildRequires:  ros-humble-ament-lint-common
%endif

%description
Package for extracting the factory calibration from a UR robot and change it
such that it can be used by ur_description to gain a correct URDF

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
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
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Mon Mar 17 2025 Felix Exner <feex@universal-robots.com> - 2.6.0-1
- Autogenerated by Bloom

* Thu Jan 23 2025 Felix Exner <feex@universal-robots.com> - 2.5.2-1
- Autogenerated by Bloom

* Sat Dec 21 2024 Felix Exner <feex@universal-robots.com> - 2.5.1-1
- Autogenerated by Bloom

* Wed Dec 18 2024 Felix Exner <feex@universal-robots.com> - 2.5.0-1
- Autogenerated by Bloom

* Wed Dec 11 2024 Felix Exner <exner@fzi.de> - 2.2.16-6
- Autogenerated by Bloom

* Tue Oct 29 2024 Felix Exner <exner@fzi.de> - 2.2.16-5
- Autogenerated by Bloom

* Tue Oct 29 2024 Felix Exner <exner@fzi.de> - 2.2.16-4
- Autogenerated by Bloom

* Tue Oct 29 2024 Felix Exner <exner@fzi.de> - 2.2.16-3
- Autogenerated by Bloom

* Tue Oct 29 2024 Felix Exner <exner@fzi.de> - 2.2.16-2
- Autogenerated by Bloom

* Tue Oct 29 2024 Felix Exner <exner@fzi.de> - 2.2.16-1
- Autogenerated by Bloom

* Fri Jul 26 2024 Felix Exner <exner@fzi.de> - 2.2.15-1
- Autogenerated by Bloom

* Mon Jul 01 2024 Felix Exner <exner@fzi.de> - 2.2.14-1
- Autogenerated by Bloom

* Mon Jun 17 2024 Felix Exner <exner@fzi.de> - 2.2.13-1
- Autogenerated by Bloom

* Sat May 18 2024 Felix Exner <exner@fzi.de> - 2.2.12-1
- Autogenerated by Bloom

* Mon Nov 28 2022 Felix Exner <exner@fzi.de> - 2.2.6-1
- Autogenerated by Bloom

* Tue Nov 22 2022 Felix Exner <exner@fzi.de> - 2.2.5-1
- Autogenerated by Bloom

* Fri Oct 07 2022 Felix Exner <exner@fzi.de> - 2.2.4-1
- Autogenerated by Bloom

* Mon Aug 01 2022 Felix Exner <exner@fzi.de> - 2.2.3-1
- Autogenerated by Bloom

* Tue Jul 19 2022 Felix Exner <exner@fzi.de> - 2.2.2-1
- Autogenerated by Bloom

* Mon Jun 27 2022 Felix Exner <exner@fzi.de> - 2.2.1-1
- Autogenerated by Bloom

* Tue Jun 21 2022 Felix Exner <exner@fzi.de> - 2.2.0-1
- Autogenerated by Bloom

