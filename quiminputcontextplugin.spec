%define version 0.1.6
%define release 2.svn909.mdk

Name:           quiminputcontextplugin
Summary:        Uim context plugin for qt-immodule
Version:        %{version}
Release:        %{release}
Group:			System/Internationalization
License:		GPL or BSD
URL:			http://www.kde.gr.jp/~daisuke/immodule_for_qt/pukiwiki/?QUimInputContext
Source0:		%{name}-%{version}.tar.bz2
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:		uim
BuildRequires:	qt3-devel >= 3.3.2-17mdk

%description
uim context plugin for qt-immodule


%prep
%setup -q

%build
qmake
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/qt3/plugins/input
cp lib*.so $RPM_BUILD_ROOT/%{_libdir}/qt3/plugins/input

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc COPYING ChangeLog README.en README.ja

%dir %{_libdir}/qt3/plugins/input/
%{_libdir}/qt3/plugins/input/*


