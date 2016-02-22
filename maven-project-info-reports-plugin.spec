%global pkg_name maven-project-info-reports-plugin
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        2.6
Release:        8.15%{?dist}
Summary:        Maven Project Info Reports Plugin

License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-project-info-reports-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip
BuildArch: noarch

BuildRequires: %{?scl_prefix_java_common}javapackages-tools
BuildRequires: %{?scl_prefix}apache-commons-parent
BuildRequires: %{?scl_prefix_java_common}maven-local
BuildRequires: %{?scl_prefix}maven-dependency-tree
BuildRequires: %{?scl_prefix}maven-plugin-annotations
BuildRequires: %{?scl_prefix}maven-plugin-plugin
BuildRequires: %{?scl_prefix}maven-reporting-api
BuildRequires: %{?scl_prefix}maven-reporting-impl
BuildRequires: %{?scl_prefix}maven-doxia-tools
BuildRequires: %{?scl_prefix}maven-shared-jar
BuildRequires: %{?scl_prefix}maven-wagon-file
BuildRequires: %{?scl_prefix}maven-wagon-http-lightweight
BuildRequires: %{?scl_prefix}maven-wagon-provider-api
BuildRequires: %{?scl_prefix}maven-scm
BuildRequires: %{?scl_prefix}maven-doxia-sink-api
BuildRequires: %{?scl_prefix}maven-doxia-logging-api
BuildRequires: %{?scl_prefix}maven-doxia-core
BuildRequires: %{?scl_prefix}maven-doxia-module-xhtml
BuildRequires: %{?scl_prefix}maven-doxia-sitetools
BuildRequires: %{?scl_prefix}plexus-containers-container-default
BuildRequires: %{?scl_prefix}plexus-component-api
BuildRequires: %{?scl_prefix}plexus-i18n
BuildRequires: %{?scl_prefix}plexus-utils
BuildRequires: %{?scl_prefix}apache-commons-validator
BuildRequires: %{?scl_prefix}maven-plugin-testing-harness
BuildRequires: %{?scl_prefix_java_common}tomcat-servlet-3.0-api
BuildRequires: %{?scl_prefix}maven-jarsigner-plugin
BuildRequires: %{?scl_prefix}keytool-maven-plugin
BuildRequires: %{?scl_prefix}joda-time
BuildRequires: %{?scl_prefix}maven-resources-plugin


%description
The Maven Project Info Reports Plugin is a plugin 
that generates standard reports for the specified project.
  

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.


%prep
%setup -q -c -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
pushd %{pkg_name}-%{version}
# removed cvsjava provider since we don't support it anymore
%pom_remove_dep :maven-scm-provider-cvsjava
# not actually needed
%pom_remove_dep :wagon-ssh

%pom_xpath_remove "pom:dependency[pom:scope[text()='test']]"
popd
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
pushd %{pkg_name}-%{version}
%mvn_build -f
popd
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
pushd %{pkg_name}-%{version}
%mvn_install
popd
%{?scl:EOF}

%files -f %{pkg_name}-%{version}/.mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%doc %{pkg_name}-%{version}/LICENSE %{pkg_name}-%{version}/NOTICE

%files javadoc -f %{pkg_name}-%{version}/.mfiles-javadoc
%doc %{pkg_name}-%{version}/LICENSE %{pkg_name}-%{version}/NOTICE

%changelog
* Mon Jan 18 2016 Michal Srb <msrb@redhat.com> - 2.6-8.15
- Drop wagon-ssh dependency

* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 2.6-8.14
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 2.6-8.13
- maven33 rebuild

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-8.12
- Add directory ownership on %%{_mavenpomdir} subdir

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 2.6-8.11
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 2.6-8.10
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-8.9
- Mass rebuild 2014-05-26

* Thu Feb 20 2014 Michael Simacek <msimacek@redhat.com> - 2.6-8.8
- Adjust maven-wagon R/BR

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-8.7
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-8.6
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-8.5
- Remove requires on java

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-8.4
- Rebuild to fix incorrect auto-requires

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-8.3
- SCL-ize requires and build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-8.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-8.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.6-8
- Mass rebuild 2013-12-27

* Mon Aug 26 2013 Michal Srb <msrb@redhat.com> - 2.6-7
- Migrate away from mvn-rpmbuild (Resolves: #997511)
- Add missing BR: maven-resources-plugin

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-6
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Apr  8 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-5
- Remove dependencies with test scope

* Mon Apr  8 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-4
- Add missing Requires on doxia packages
- Resolves: rhbz#909250

* Fri Feb 08 2013 Michal Srb <msrb@redhat.com> - 2.6-3
- Migrate from maven-doxia to doxia subpackages (Resolves: #909250)
- Add BR on maven-local

* Tue Dec 11 2012 Michal Srb <msrb@redhat.com> - 2.6-2
- Migrated to plexus-containers-container-default (Resolves: #878559)
- Removed build dependency on netbeans-cvsclient

* Mon Oct 29 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-1
- Update to upstream version 2.6

* Tue Sep 11 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5.1-1
- Update to upstream version 2.5.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 22 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.4-6
- Remove cvsjava support (still can use cvsexe)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 5 2011 Alexander Kurtakov <akurtako@redhat.com> 2.4-4
- One more missing R - joda-time.

* Mon Sep 5 2011 Alexander Kurtakov <akurtako@redhat.com> 2.4-3
- Requires maven-scm.

* Mon Sep 5 2011 Alexander Kurtakov <akurtako@redhat.com> 2.4-2
- Add missing R.

* Mon May 30 2011 Alexander Kurtakov <akurtako@redhat.com> 2.4-1
- Update to upstream version 2.4.

* Mon May 23 2011 Alexander Kurtakov <akurtako@redhat.com> 2.3.1-1
- UPdate to upstream version 2.3.1.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 9 2010 Chris Spike <chris.spike@arcor.de> 2.2-5
- Removed obsolete patch
- tomcat5 -> tomcat6 BRs/Rs

* Tue Oct 26 2010 akurtakov <akurtakov@redhat.com> 2.2-4
- Fix apache-commons-validator BR/R.

* Thu Sep 09 2010 Hui Wang <huwang@redhat.com> - 2.2-3
- Add missing BR netbeans-cvsclient

* Mon Jun 07 2010 Hui Wang <huwang@redhat.com> - 2.2-2
- Added missing requires

* Thu Jun 02 2010 Hui Wang <huwang@redhat.com> - 2.2-1
- Initial version of the package
