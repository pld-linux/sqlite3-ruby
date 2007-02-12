Summary:	SQLite3 module for Ruby
Summary(pl.UTF-8):	Moduł SQLite3 dla Ruby
Name:		sqlite3-ruby
Version:	1.1.0
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/3089/%{name}-%{version}.tar.bz2
# Source0-md5:	83c6c16dc40a282931edfd0525d3aaf3
URL:		http://sqlite-ruby.sourceforge.net
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
%setup -q

%build
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
