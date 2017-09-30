Name:		timewarrior
Version:	1.1
Release:	1%{?dist}
Summary:  Timewarrior tracking time software
Group:		Unspecified
License:	MIT
URL:		 http://timewarrior.net

BuildRequires:	git
BuildRequires:	cmake
BuildRequires:	gcc-c++

%description

Timewarrior is Free and Open Source Software that tracks time from the command line

%build

git clone --recursive https://git.tasktools.org/TM/timew.git timew.git
cd timew.git
git checkout master 
cmake -DCMAKE_BUILD_TYPE=release -DCMAKE_INSTALL_PREFIX=../%{buildsubdir}/usr/local/ .
make
make install

%install

#copy timewarrior make install files
cp -av %{buildsubdir}/* %{buildroot}


%files
/usr/local/*

