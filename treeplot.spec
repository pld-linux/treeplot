Summary:	Phylogenetic tree file converter
Name:		treeplot
Version:	0.7
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.cnrs-gif.fr/pge/bioinfo/sources/%{name}-%{version}.tar.gz
URL:		http://www.cnrs-gif.fr/pge/bioinfo/treeplot/index.php?lang=en
BuildRequires:	libplotter-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Phylogenetic tree file converter (Phylip, Gif, Postscript, Adobe
Illustrator, xfig...).

%prep
%setup -q

%build
install %{_datadir}/automake/config.* .
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
