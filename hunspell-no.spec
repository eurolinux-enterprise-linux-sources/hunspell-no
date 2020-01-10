Name: hunspell-no
Summary: Norwegian hunspell dictionaries
Version: 2.1
Release: 2%{?dist}
Source: https://alioth.debian.org/frs/download.php/3764/no_NO-pack2-2.1.zip
Group: Applications/Text
URL: http://spell-norwegian.alioth.debian.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPL+
BuildArch: noarch

%description
Norwegian hunspell dictionaries.

%package -n hunspell-nb
Summary: Bokmaal hunspell dictionaries
Group: Applications/Text
Requires: hunspell

%description -n hunspell-nb
Bokmaal hunspell dictionaries.

%package -n hunspell-nn
Summary: Nynorsk hunspell dictionaries
Group: Applications/Text
Requires: hunspell

%description -n hunspell-nn
Nynorsk hunspell dictionaries.

%package -n hyphen-nb
Summary: Bokmaal hyphenation rules
Group: Applications/Text
Requires: hyphen

%description -n hyphen-nb
Bokmaal hyphenation rules.

%package -n hyphen-nn
Summary: Nynorsk hyphenation rules
Group: Applications/Text
Requires: hyphen

%description -n hyphen-nn
Nynorsk hyphenation rules

%package -n mythes-nb
Summary: Bokmaal thesaurus
Group: Applications/Text
Requires: mythes

%description -n mythes-nb
Bokmaal thesaurus.

%package -n mythes-nn
Summary: Nynorsk thesaurus 
Group: Applications/Text
Requires: mythes

%description -n mythes-nn
Nynorsk thesaurus.

%prep
%setup -q -c

%build
unzip -q nb_NO.zip
unzip -q nn_NO.zip
unzip -q hyph_nb_NO.zip
unzip -q hyph_nn_NO.zip
unzip -q th_nb_NO_v2.zip
unzip -q th_nn_NO_v2.zip
for i in README_nb_NO.txt README_nn_NO.txt README_hyph_nb_NO.txt \
  README_hyph_nn_NO.txt README_th_nb_NO_v2.txt README_th_nn_NO_v2.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p nn_NO.aff nn_NO.dic nb_NO.aff nb_NO.dic $RPM_BUILD_ROOT/%{_datadir}/myspell
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_nn_NO.dic hyph_nb_NO.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_nb_NO_v2.dat th_nb_NO_v2.idx th_nn_NO_v2.dat th_nn_NO_v2.idx $RPM_BUILD_ROOT/%{_datadir}/mythes

%clean
rm -rf $RPM_BUILD_ROOT

%files -n hunspell-nb
%defattr(-,root,root,-)
%doc README_nb_NO.txt
%{_datadir}/myspell/nb_NO.*

%files -n hunspell-nn
%defattr(-,root,root,-)
%doc README_nn_NO.txt
%{_datadir}/myspell/nn_NO.*

%files -n hyphen-nb
%defattr(-,root,root,-)
%doc README_hyph_nb_NO.txt
%{_datadir}/hyphen/hyph_nb_NO.*

%files -n hyphen-nn
%defattr(-,root,root,-)
%doc README_hyph_nn_NO.txt
%{_datadir}/hyphen/hyph_nn_NO.*

%files -n mythes-nb
%defattr(-,root,root,-)
%doc README_th_nb_NO_v2.txt
%{_datadir}/mythes/th_nb_NO_v2.*

%files -n mythes-nn
%defattr(-,root,root,-)
%doc README_th_nb_NO_v2.txt
%{_datadir}/mythes/th_nn_NO_v2.*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 01 2012 Caolán McNamara <caolanm@redhat.com> - 2.1-1
- latest -version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 05 2010 Caolán McNamara <caolanm@redhat.com> - 2.0.10-8
- Resolves: rhbz#648740 revert this, and silence hunspell instead

* Tue Nov 02 2010 Caolán McNamara <caolanm@redhat.com> - 2.0.10-7
- Resolves: rhbz#648740 thousands of trailing empty rules spew

* Sun Apr 04 2010 Caolán McNamara <caolanm@redhat.com> - 2.0.10-6
- mythes now owns /usr/share/mythes

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolán McNamara <caolanm@redhat.com> - 2.0.10-4
- tidy spec

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 27 2008 Caolán McNamara <caolanm@redhat.com> - 2.0.10-2
- silly require

* Thu Nov 20 2008 Caolán McNamara <caolanm@redhat.com> - 2.0.10-1
- initial version
