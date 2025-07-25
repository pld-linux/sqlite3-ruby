%define pkgname sqlite3
Summary:	SQLite3 module for Ruby
Summary(pl.UTF-8):	Moduł SQLite3 dla Ruby
Name:		%{pkgname}-ruby
Version:	1.2.5
Release:	10
License:	GPL
Group:		Development/Languages
Source0:	https://rubygems.org/downloads/%{name}-%{version}.gem
# Source0-md5:	eaa6328b0e971f4563f8d26715e37e13
Patch0:		%{name}-ruby-1.9.patch
URL:		http://rubyforge.org/projects/sqlite-ruby/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	ruby-devel
BuildRequires:	setup.rb >= 3.4.1-6
BuildRequires:	sqlite3-devel
BuildRequires:	swig-ruby >= 1.3.25
Obsoletes:	ruby-sqlite3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SQLite3 module for Ruby.

%description -l pl.UTF-8
Moduł SQLite3 dla Ruby.

%package rdoc
Summary:	HTML documentation for %{name}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{name}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4
BuildArch:	noarch

%description rdoc
HTML documentation for %{name}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{name}.

%package ri
Summary:	ri documentation for %{name}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{name}
Group:		Documentation
Requires:	ruby
BuildArch:	noarch

%description ri
ri documentation for %{name}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{name}.

%prep
%setup -q -n %{pkgname}-%{version}
%patch -P0 -p1

cp -p %{_datadir}/setup.rb .

%build
swig -ruby \
	-o ext/sqlite3_api/sqlite3_api_wrap.c \
	ext/sqlite3_api/sqlite3_api.i

ruby setup.rb config \
	--site-ruby=%{ruby_vendorlibdir} \
	--so-dir=%{ruby_vendorarchdir}
ruby setup.rb setup

rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -r ri/{DL,Kernel,String}
rm ri/created.rid
rm ri/cache.ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_ridir},%{ruby_rdocdir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{ruby_vendorarchdir}/sqlite3_api.so
%{ruby_vendorlibdir}/sqlite3.rb
%{ruby_vendorlibdir}/sqlite3

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/SQLite3
