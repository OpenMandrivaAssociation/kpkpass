#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define major 6
%define libname %mklibname KPim6PkPass
%define devname %mklibname KPim6PkPass -d

Name: 		plasma6-kpkpass
Version:	25.04.0
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/kpkpass/-/archive/%{gitbranch}/kpkpass-%{gitbranchd}.tar.bz2#/kpkpass-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/kpkpass-%{version}.tar.xz
%endif
Summary:	Library for handling Apple Wallet pass files
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(KF6Archive)
BuildRequires: shared-mime-info-devel
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant

%description
Library for handling Apple Wallet pass files

%package -n %{libname}
Summary: Library for handling Apple Wallet pass files
Group: System/Libraries
Requires: %{name} >= %{EVRD}

%description -n %{libname}
Library for handling Apple Wallet pass files

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1 -n kpkpass-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_datadir}/qlogging-categories6/org_kde_kpkpass.categories

%files -n %{libname}
%{_libdir}/libKPim6PkPass.so*

%files -n %{devname}
%{_includedir}/KPim6/KPkPass
%{_libdir}/cmake/*
