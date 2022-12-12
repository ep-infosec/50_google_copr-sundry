%global provider        github
%global provider_tld    com
%global project         cznic
%global repo            strutil
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider}.com/%{project}/%{repo}
%global commit          1eb03e3cc9d345307a45ec82bd3016cde4bd4464
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global debug_package   %{nil}

Name:           golang-github-cznic-%{repo}
Version:        0
Release:        1%{?dist}
Summary:        Collects utils supplemental to the standard strings package
License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://github.com/cznic/%{repo}/archive/%{commit}.zip

BuildRequires:  golang

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

Provides:      golang(%{import_path}) = %{version}-%{release}

%description devel
%{summary}

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
# source codes for building projects
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
for ext in go s; do
    # find all *.go but no *_test.go files.
    for file in $(find . -iname "*.$ext" \! -iname "*_test.go") ; do
        install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
        cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    done
done

%files -n %{name}-devel
%license LICENSE
%doc README
%dir %{gopath}/src/%{import_path}
/usr/share/gocode/src/github.com/cznic/strutil/strutil.go


%changelog
* Thu Jul 07 2016 Vladimir Rusinov <vrusinov@google.com> 0-1.git1eb03e3
- First version.
