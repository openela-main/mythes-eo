Name: mythes-eo
Summary: Esperanto thesaurus
%global upstreamid 20180330
Version: 0.%{upstreamid}
Release: 8%{?dist}
Source: http://esperanto.mv.ru/Download/dict-eo.oxt
URL: http://esperanto.mv.ru/Download/
License: GPLv3+
BuildArch: noarch

%description
Esperanto thesaurus.

%package -n hyphen-eo
Summary: Esperanto hyphen rules
Requires: hyphen
Supplements: (hyphen and langpacks-eo)

%description -n hyphen-eo
Esperanto hyphenation rules.

%prep
%autosetup -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p dictionaries/hyph_eo.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p dictionaries/th_eo.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_eo.dat
cp -p dictionaries/th_eo.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_eo.idx

%files
%doc description/desc_en.txt
%license licenses/license-en.txt
%{_datadir}/mythes/*

%files -n hyphen-eo
%doc description/desc_en.txt
%license licenses/license-en.txt
%{_datadir}/hyphen/*

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 0.20180330-8
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.20180330-7
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20180330-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20180330-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20180330-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20180330-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Nov 23 2018 Carmen Bianca Bakker <carmen@carmenbianca.eu> - 0.20180330-2
- Renamed from super-eo to mythes-eo.
- Minor fixes according to package reviews.

* Wed Oct 31 2018 Carmen Bianca Bakker <carmen@carmenbianca.eu> - 0.20180330-1
- Initial package

