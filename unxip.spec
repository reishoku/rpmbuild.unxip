
Name:           unxip
Version:        3.2
Release:        1%{?dist}
Summary:        A fast Xcode unarchiver

License:        LGPLv3
URL:            https://github.com/saagarjha/unxip
Source0:        https://github.com/saagarjha/unxip/archive/refs/tags/v%{version}.tar.gz

# swift-lang can be obtained from EPEL
BuildRequires:  swift-lang

# BuildRequires:  libstdc++-static
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  zlib-devel

# Requires:       glibc
# Requires:       libgcc
# Requires:       libstdc++
# Requires:       xz-libs
# Requires:       zlib

Recommends: epel-release

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
   -Xswiftc '-parse-as-library' \
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
* Sun Nov 23 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 3.2-1
- Update to 3.2

* Sat Mar 15 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 3.1-1
- Initial RPM package
