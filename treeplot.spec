Summary:	Phylogenetic tree file converter
Summary(pl):	Konwerter plików drzew filogenetycznych
Name:		treeplot
Version:	0.7
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.cnrs-gif.fr/pge/bioinfo/sources/%{name}-%{version}.tar.gz
Patch0:		%{name}-c++.patch
URL:		http://www.cnrs-gif.fr/pge/bioinfo/treeplot/index.php?lang=en
BuildRequires:	automake
BuildRequires:	libplotter-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Phylogenetic tree file converter (Phylip, Gif, Postscript, Adobe
Illustrator, xfig...).

%description -l pl
Konwerter plików drzew filogenetycznych (Phylip, Gif, Postscript,
Adobe Illustrator, xfig...).

%prep
%setup -q
%patch0 -p1

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
