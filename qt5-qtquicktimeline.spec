#
# Conditional build:
%bcond_without	doc	# Documentation

%define		orgname		qtquicktimeline
%define		qtbase_ver		%{version}
%define		qtdeclarative_ver	%{version}
%define		qttools_ver		%{version}
Summary:	The Qt5 Quick Timeline module
Summary(pl.UTF-8):	Moduł Qt5 Quick Timeline
Name:		qt5-%{orgname}
Version:	5.15.14
Release:	1
License:	GPL v3+ or commercial
Group:		X11/Libraries
Source0:	https://download.qt.io/official_releases/qt/5.15/%{version}/submodules/%{orgname}-everywhere-opensource-src-%{version}.tar.xz
# Source0-md5:	7b5c43879632534f002ad817a75ee10d
URL:		https://www.qt.io/
BuildRequires:	Qt5Core-devel >= %{qtbase_ver}
BuildRequires:	Qt5Qml-devel >= %{qtdeclarative_ver}
BuildRequires:	Qt5Quick-devel >= %{qtdeclarative_ver}
%if %{with doc}
BuildRequires:	qt5-assistant >= %{qttools_ver}
BuildRequires:	qt5-doc-common >= %{qttools_ver}
%endif
BuildRequires:	qt5-build >= %{qtbase_ver}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.016
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing
%define		qt5dir		%{_libdir}/qt5

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains Qt5 Quick Timeline module.

%description -l pl.UTF-8
Qt to wieloplatformowy szkielet aplikacji i interfejsów użytkownika.
Przy użyciu Qt można pisać aplikacje powiązane z WWW i wdrażać je w
systemach biurkowych, przenośnych i wbudowanych bez przepisywania kodu
źródłowego.

Ten pakiet zawiera moduł Qt5 Quick Timeline.

%package -n Qt5Quick-Timeline
Summary:	The Qt5 Quick Timeline module
Summary(pl.UTF-8):	Moduł Qt5 Quick Timeline
Group:		X11/Libraries
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5Qml >= %{qtdeclarative_ver}
Requires:	Qt5Quick >= %{qtdeclarative_ver}

%description -n Qt5Quick-Timeline
Qt5 Quick Timeline module.

%description -n Qt5Quick-Timeline -l pl.UTF-8
Moduł Qt5 Quick Timeline.

%package doc
Summary:	Qt5 Quick Timeline module documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja do modułu Qt5 Quick Timeline w formacie HTML
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
BuildArch:	noarch

%description doc
Qt5 Quick Timeline module documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja do modułu Qt5 Quick Timeline w formacie HTML.

%package doc-qch
Summary:	Qt5 Quick Timeline module documentation in QCH format
Summary(pl.UTF-8):	Dokumentacja do modułu Qt5 Quick Timeline w formacie QCH
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
BuildArch:	noarch

%description doc-qch
Qt5 Quick Timeline module documentation in QCH format.

%description doc-qch -l pl.UTF-8
Dokumentacja do modułu Qt5 Quick Timeline w formacie QCH.

%prep
%setup -q -n %{orgname}-everywhere-src-%{version}

%build
%{qmake_qt5}
%{__make}

%{?with_doc:%{__make} docs}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%if %{with doc}
%{__make} install_docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n Qt5Quick-Timeline
%defattr(644,root,root,755)
%doc README.md dist/changes-*
# R: Qt5Core Qt5Qml Qt5Quick
%dir %{qt5dir}/qml/QtQuick/Timeline
%attr(755,root,root) %{qt5dir}/qml/QtQuick/Timeline/libqtquicktimelineplugin.so
%{qt5dir}/qml/QtQuick/Timeline/plugins.qmltypes
%{qt5dir}/qml/QtQuick/Timeline/qmldir

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtquicktimeline

%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtquicktimeline.qch
%endif
