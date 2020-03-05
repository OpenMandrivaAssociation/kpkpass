%define major 5
%define libname %mklibname KPimPkPass %{major}
%define devname %mklibname KPimPkPass -d

Name: 		kpkpass
Version:	19.12.3
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Summary:	Library for handling Apple Wallet pass files
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(KF5Archive)
BuildRequires: shared-mime-info-devel

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
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_datadir}/qlogging-categories5/org_kde_kpkpass.categories
%{_datadir}/mime/packages/application-vnd-apple-pkpass.xml

%files -n %{libname}
%{_libdir}/libKPimPkPass.so.%{major}*

%files -n %{devname}
%{_includedir}/KPim/KPkPass
%{_libdir}/*.so
%{_libdir}/cmake/*
