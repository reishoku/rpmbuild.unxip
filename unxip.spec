
Name:           unxip
Version:        3.1
Release:        1%{?dist}
Summary:        A fast Xcode unarchiver

License:        LGPLv3
URL:            https://github.com/saagarjha/unxip
Source0:        https://github.com/saagarjha/unxip/archive/refs/tags/v%{version}.tar.gz

# swift-lang can be obtained from EPEL
BuildRequires:  swift-lang >= 6.0

BuildRequires:  libstdc++-static
BuildRequires:  libxml2-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel

Requires:       glibc
Requires:       libgcc
Requires:       libstdc++
Requires:       xz-libs
Requires:       zlib

%global debug_package %{nil}

%description
A fast Xcode unarchiver


%prep
%autosetup


%build
# swift >=6 is needed for --disable-local-rpath
swift build \
   -c release \
   -j %{?_smp_build_ncpus} \
   -Xswiftc '-O' \
   -Xswiftc '-gnone' \
   -Xswiftc '-whole-module-optimization' \
   -Xswiftc '-parse-as-library' \
   -Xlinker '--build-id' \
   -Xlinker '-s' \
   --disable-local-rpath \
   --static-swift-stdlib

%install
%{__mkdir_p} %{buildroot}%{_bindir}
%{__cp} -av \
  .build/release/unxip \
  %{buildroot}%{_bindir}/unxip

%files
%{_bindir}/unxip


%changelog
* Sat Mar 15 2025 KOSHIKAWA Kenichi <github.reishoku@reishoku.net>
- Initial RPM package
