Summary:	SQLite3 module for Ruby
Summary(pl.UTF-8):	Moduł SQLite3 dla Ruby
Name:		sqlite3-ruby
Version:	1.2.5
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{name}-%{version}.gem
# Source0-md5:	eaa6328b0e971f4563f8d26715e37e13
Patch0:		%{name}-ruby-1.9.patch
URL:		http://rubyforge.org/projects/sqlite-ruby/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	sqlite3-devel
BuildRequires:	swig-ruby >= 1.3.25
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SQLite3 module for Ruby.

%description -l pl.UTF-8
Moduł SQLite3 dla Ruby.

%prep
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README.txt -o -print | xargs touch --reference %{SOURCE0}
%patch0 -p1

cp /usr/share/setup.rb .

%build
swig -ruby \
	-o ext/sqlite3_api/sqlite3_api_wrap.c \
	ext/sqlite3_api/sqlite3_api.i

ruby setup.rb config --site-ruby=%{ruby_rubylibdir} --so-dir=%{ruby_archdir}
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{ruby_archdir}/*
%{ruby_rubylibdir}/sqlite3.rb
%{ruby_rubylibdir}/sqlite3
