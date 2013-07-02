# To Build:
#
# sudo yum -y install rpmdevtools && rpmdev-setuptree
# wget https://raw.github.com/nmilford/rpm-glu/master/glu.spec -O ~/rpmbuild/SPECS/glu.spec
# wget http://dl.bintray.com/pongasoft/glu/org.linkedin.glu.packaging-all-5.0.0.tgz?direct -O ~/rpmbuild/SOURCES/org.linkedin.glu.packaging-all-5.0.0.tgz
# wget https://raw.github.com/nmilford/rpm-glu/master/glu-agent -O ~/rpmbuild/SOURCES/glu-agent
# wget https://raw.github.com/nmilford/rpm-glu/master/glu-console-jetty -O ~/rpmbuild/SOURCES/glu-console-jetty
# wget http://mirror.cc.columbia.edu/pub/software/eclipse/jetty/8.1.10.v20130312/dist/jetty-distribution-8.1.10.v20130312.tar.gz -O ~/rpmbuild/SOURCES/jetty-distribution-8.1.10.v20130312.tar.gz
# rpmbuild -bb ~/rpmbuild/SPECS/glu.spec

%define __jar_repack %{nil}
%define glu_ver 5.0.0
%define glu_pkg org.linkedin.glu.packaging-all-%{glu_ver}
%define glu_home /opt/glu
%define zk_ver 2.0.0
%define jetty_ver 8.1.10.v20130312


Name:      glu
Version:   %{glu_ver}
Release:   1%{?dist}
Source0:   http://dl.bintray.com/pongasoft/glu/%{glu_pkg}.tgz
Source1:   glu-agent
Source2:   glu-console-jetty
License:   Apache
Group:     Development/Tools
Summary:   glu is a free/open source deployment and monitoring automation platform.
BuildRoot: %{_tmppath}/%{name}-%{version}-root
URL:       https://github.com/pongasoft/glu
Vendor:    Linkedin
BuildArch: noarch

%description
glu's goal is to deploy (and monitor) applications to an arbitrary large set of
nodes efficiently, with minimum/no human interaction, securely, in a
reproducible manner.

%package agent
Summary: Service and utils for a glu deployment agent.
Group: Development/Tools
Requires: %{name} = %{version}-%{release}, jdk
BuildArch: noarch
%description agent
The glu agent is an active process that needs to run on every host where
applications need to be deployed.

%package console
Summary: Web app and tools for the glu/Zk orchestration engine.
Group: Development/Tools
Requires: %{name} = %{version}-%{release}, jdk
BuildArch: noarch
%description console
The glu console is a web application that offers a graphical presentation on top
of the glu/Zk orchestration engine. This package expects you to setup and 
configure your own sevlet server, install the glu-console-jetty package if you
want to have jetty bundled snd ready to go.

%package console-jetty
Summary: Jetty Servlet Engine to host the Glu Console.
Group: Development/Tools
License: Eclipse
Requires: %{name} = %{version}-%{release},jdk, glu-console
BuildArch: noarch
%description console-jetty
Installs a jetty instance to server the Glu Console web application.  Install
this if you do not intend to host the Glu Console servlet on another engine.

%prep
%setup -n %{glu_pkg}

%build

%clean
rm -rf %{buildroot}

%install
install -d -m 755 %{buildroot}/%{glu_home}/
install    -m 644 %{_builddir}/%{glu_pkg}/*.txt  %{buildroot}/%{glu_home}/
install    -m 644 %{_builddir}/%{glu_pkg}/*.md   %{buildroot}/%{glu_home}/
install    -m 644 %{_builddir}/%{glu_pkg}/*.rst  %{buildroot}/%{glu_home}/
install    -m 644 %{_builddir}/%{glu_pkg}/*.html %{buildroot}/%{glu_home}/

install -d -m 755 %{buildroot}/%{glu_home}/agent-cli/
install -d -m 755 %{buildroot}/%{glu_home}/agent-cli/bin/
install    -m 755 %{_builddir}/%{glu_pkg}//agent-cli/bin/*.sh %{buildroot}/%{glu_home}/agent-cli/bin/

install -d -m 755 %{buildroot}/%{glu_home}/agent-cli/conf/
install    -m 644 %{_builddir}/%{glu_pkg}/agent-cli/conf/clientConfig.properties %{buildroot}/%{glu_home}/agent-cli/conf/
install    -m 644 %{_builddir}/%{glu_pkg}/agent-cli/conf/log4j.xml %{buildroot}/%{glu_home}/agent-cli/conf/

install -d -m 755 %{buildroot}/%{glu_home}/agent-cli/conf/keys/
install    -m 644 %{_builddir}/%{glu_pkg}/agent-cli/conf/keys/* %{buildroot}/%{glu_home}/agent-cli/conf/keys/

install -d -m 755 %{buildroot}/%{glu_home}/agent-server/
install    -m 644 %{_builddir}/%{glu_pkg}/agent-server/*.txt %{buildroot}/%{glu_home}/agent-server/

install -d -m 755 %{buildroot}/%{glu_home}/agent-server/bin
install    -m 755 %{_builddir}/%{glu_pkg}/agent-server/bin/*.sh %{buildroot}/%{glu_home}/agent-server/bin/

install -d -m 755 %{buildroot}/%{glu_home}/agent-server/%{glu_ver}/

install    -m 644 %{_builddir}/%{glu_pkg}/agent-server/%{glu_ver}/*.txt  %{buildroot}/%{glu_home}/agent-server/%{glu_ver}/
install    -m 644 %{_builddir}/%{glu_pkg}/agent-server/%{glu_ver}/*.md   %{buildroot}/%{glu_home}/agent-server/%{glu_ver}/
install    -m 644 %{_builddir}/%{glu_pkg}/agent-server/%{glu_ver}/*.rst  %{buildroot}/%{glu_home}/agent-server/%{glu_ver}/
install    -m 644 %{_builddir}/%{glu_pkg}/agent-server/%{glu_ver}/*.html %{buildroot}/%{glu_home}/agent-server/%{glu_ver}/

install -d -m 755 %{buildroot}/%{glu_home}/agent-server/%{glu_ver}/bin/
install    -m 755 %{_builddir}/%{glu_pkg}/agent-server/%{glu_ver}/bin/agentctl.sh %{buildroot}/%{glu_home}/agent-server/%{glu_ver}/bin/

install -d -m 755 %{buildroot}/%{glu_home}/agent-server/%{glu_ver}/conf/
install    -m 644 %{_builddir}/%{glu_pkg}/agent-server/%{glu_ver}/conf/* %{buildroot}/%{glu_home}/agent-server/%{glu_ver}/conf/

install -d -m 755 %{buildroot}/%{glu_home}/agent-server/%{glu_ver}/lib/
install    -m 644 %{_builddir}/%{glu_pkg}/agent-server/%{glu_ver}/lib/*.jar %{buildroot}/%{glu_home}/agent-server//%{glu_ver}/lib/

install -d -m 755 %{buildroot}/%{glu_home}/bin/
install    -m 755 %{_builddir}/%{glu_pkg}/bin/*.sh %{buildroot}/%{glu_home}/bin/

install -d -m 755 %{buildroot}/%{glu_home}/console-cli/
install -d -m 755 %{buildroot}/%{glu_home}/console-cli/bin
install    -m 755 %{_builddir}/%{glu_pkg}/console-cli/bin/*.py %{buildroot}/%{glu_home}/console-cli/bin/

install -d -m 755 %{buildroot}/%{glu_home}/console-cli/lib/
install -d -m 755 %{buildroot}/%{glu_home}/console-cli/lib/python/
install -d -m 755 %{buildroot}/%{glu_home}/console-cli/lib/python/gluconsole/
install    -m 755 %{_builddir}/%{glu_pkg}/console-cli/lib/python/gluconsole/*.py %{buildroot}/%{glu_home}/console-cli/lib/python/gluconsole/

install -d -m 755 %{buildroot}/%{glu_home}/console-cli/lib/python/site-packages/
install    -m 644 %{_builddir}/%{glu_pkg}/console-cli/lib/python/site-packages/* %{buildroot}/%{glu_home}/console-cli/lib/python/site-packages/

install -d -m 755 %{buildroot}/%{glu_home}/console-server/
install    -m 755 %{_builddir}/%{glu_pkg}/console-server/bin/*.sh %{buildroot}/%{glu_home}/console-server/

install -d -m 755 %{buildroot}/%{glu_home}/console-server/conf/
install    -m 644 %{_builddir}/%{glu_pkg}/console-server/conf/* %{buildroot}/%{glu_home}/console-server/conf/

install -d -m 755 %{buildroot}/%{glu_home}/console-server/keys/
install    -m 644 %{_builddir}/%{glu_pkg}/console-server/keys/* %{buildroot}/%{glu_home}/console-server/keys/

install -d -m 755 %{buildroot}/%{glu_home}/console-server/glu/
install -d -m 755 %{buildroot}/%{glu_home}/console-server/glu/docs/
install -d -m 755 %{buildroot}/%{glu_home}/console-server/glu/docs/html/
install    -m 644 %{_builddir}/%{glu_pkg}/console-server/glu/docs/html/*.html %{buildroot}/%{glu_home}/console-server/glu/docs/html/

install -d -m 755 %{buildroot}/%{glu_home}/console-server/glu/docs/html/_images/
install    -m 644 %{_builddir}/%{glu_pkg}/console-server/glu/docs/html/_images/*.png %{buildroot}/%{glu_home}/console-server/glu/docs/html/_images/

install -d -m 755 %{buildroot}/%{glu_home}/console-server/glu/docs/html/_static/
install    -m 644 %{_builddir}/%{glu_pkg}/console-server/glu/docs/html/_static/*.css %{buildroot}/%{glu_home}/console-server/glu/docs/html/_static/
install    -m 644 %{_builddir}/%{glu_pkg}/console-server/glu/docs/html/_static/*.png %{buildroot}/%{glu_home}/console-server/glu/docs/html/_static/
install    -m 644 %{_builddir}/%{glu_pkg}/console-server/glu/docs/html/_static/*.js  %{buildroot}/%{glu_home}/console-server/glu/docs/html/_static/

install -d -m 755 %{buildroot}/%{glu_home}/console-server/glu/repository/
install -d -m 755 %{buildroot}/%{glu_home}/console-server/glu/repository/plugins/
install    -m 644 %{_builddir}/%{glu_pkg}/console-server/glu/repository/plugins/*.txt %{buildroot}/%{glu_home}/console-server/glu/repository/plugins/

install -d -m 755 %{buildroot}/%{glu_home}/console-server/glu/repository/scripts/
install -d -m 755 %{buildroot}/%{glu_home}/console-server/glu/repository/scripts/hello-world/
install    -m 644 %{_builddir}/%{glu_pkg}/console-server/glu/repository/scripts/org.linkedin.glu.script-hello-world-%{glu_ver}/* %{buildroot}/%{glu_home}/console-server/glu/repository/scripts/hello-world

install -d -m 755 %{buildroot}/%{glu_home}/console-server/glu/repository/scripts/jetty/
install    -m 644 %{_builddir}/%{glu_pkg}/console-server/glu/repository/scripts/org.linkedin.glu.script-jetty-%{glu_ver}/* %{buildroot}/%{glu_home}/console-server/glu/repository/scripts/jetty/

install -d -m 755 %{buildroot}/%{glu_home}/console-server/glu/repository/scripts/noop/
install    -m 644 %{_builddir}/%{glu_pkg}/console-server/glu/repository/scripts/org.linkedin.glu.script-noop-%{glu_ver}/* %{buildroot}/%{glu_home}/console-server/glu/repository/scripts/noop/

install -d -m 755 %{buildroot}/%{glu_home}/console-server/glu/repository/systems/
install    -m 644 %{_builddir}/%{glu_pkg}/console-server/glu/repository/systems/*.json %{buildroot}/%{glu_home}/console-server/glu/repository/systems/

#install -d -m 755 %{buildroot}/%{glu_home}/console-server/glu/repository/tgzs/
#install    -m 644 %{_builddir}/%{glu_pkg}/console-server/glu/repository/tgzs/* %{buildroot}/%{glu_home}/console-server/glu/repository/tgzs/

install -d -m 755 %{buildroot}/%{glu_home}/console-server/glu/repository/wars/
install    -m 644 %{_builddir}/%{glu_pkg}/console-server/glu/repository/wars/* %{buildroot}/%{glu_home}/console-server/glu/repository/wars/

#install -d -m 755 %{buildroot}/%{glu_home}/zookeeper-server/
#install    -m 644 %{_builddir}/%{glu_pkg}/org.linkedin.zookeeper-server-%{zk_ver}/*.txt %{buildroot}/%{glu_home}/zookeeper-server/
#install    -m 644 %{_builddir}/%{glu_pkg}/org.linkedin.zookeeper-server-%{zk_ver}/*.md  %{buildroot}/%{glu_home}/zookeeper-server/

#install -d -m 755 %{buildroot}/%{glu_home}/zookeeper-server/bin/
#install    -m 755 %{_builddir}/%{glu_pkg}/org.linkedin.zookeeper-server-%{zk_ver}/bin/*.sh %{buildroot}/%{glu_home}/zookeeper-server/bin/

#install -d -m 755 %{buildroot}/%{glu_home}/zookeeper-server/conf/
#install    -m 644 %{_builddir}/%{glu_pkg}/org.linkedin.zookeeper-server-%{zk_ver}/conf/* %{buildroot}/%{glu_home}/zookeeper-server/conf/

#install -d -m 755 %{buildroot}/%{glu_home}/zookeeper-server/data/

#install -d -m 755 %{buildroot}/%{glu_home}/zookeeper-server/lib/
#install    -m 644 %{_builddir}/%{glu_pkg}/org.linkedin.zookeeper-server-%{zk_ver}/lib/*.jar %{buildroot}/%{glu_home}/zookeeper-server/lib/

rm -rf %{buildroot}/%{glu_home}/org.linkedin.*

install -d -m 755 %{buildroot}/%{glu_home}/zookeeper-server/logs/

install -d -m 755 %{buildroot}/%{glu_home}/setup/
install -d -m 755 %{buildroot}/%{glu_home}/setup/bin/
install    -m 755 %{_builddir}/%{glu_pkg}/setup/bin/*.sh %{buildroot}/%{glu_home}/setup/bin/

install -d -m 755 %{buildroot}/%{glu_home}/setup/org.linkedin.zookeeper-cli-%{zk_ver}
install    -m 644 %{_builddir}/%{glu_pkg}/setup/org.linkedin.zookeeper-cli-%{zk_ver}/*.txt %{buildroot}/%{glu_home}/setup/org.linkedin.zookeeper-cli-%{zk_ver}
install    -m 644 %{_builddir}/%{glu_pkg}/setup/org.linkedin.zookeeper-cli-%{zk_ver}/*.md  %{buildroot}/%{glu_home}/setup/org.linkedin.zookeeper-cli-%{zk_ver}

install -d -m 755 %{buildroot}/%{glu_home}/setup/org.linkedin.zookeeper-cli-%{zk_ver}/bin/
install    -m 755 %{_builddir}/%{glu_pkg}/setup/org.linkedin.zookeeper-cli-%{zk_ver}/bin/*.sh %{buildroot}/%{glu_home}/setup/org.linkedin.zookeeper-cli-%{zk_ver}/bin/

install -d -m 755 %{buildroot}/%{glu_home}/setup/org.linkedin.zookeeper-cli-%{zk_ver}/conf/
install    -m 644 %{_builddir}/%{glu_pkg}/setup/org.linkedin.zookeeper-cli-%{zk_ver}/conf/* %{buildroot}/%{glu_home}/setup/org.linkedin.zookeeper-cli-%{zk_ver}/conf/

install -d -m 755 %{buildroot}/%{glu_home}/setup/org.linkedin.zookeeper-cli-%{zk_ver}/lib/
install    -m 644 %{_builddir}/%{glu_pkg}/setup/org.linkedin.zookeeper-cli-%{zk_ver}/lib/* %{buildroot}/%{glu_home}/setup/org.linkedin.zookeeper-cli-%{zk_ver}/lib/

install -d -m 755 %{buildroot}/%{glu_home}/setup/zookeeper-config/
install    -m 755 %{_builddir}/%{glu_pkg}/setup/zookeeper-config/* %{buildroot}/%{glu_home}/setup/zookeeper-config/

# Put logging in /var/log
install -d -m 755 %{buildroot}/opt/glu/agent-server/data/
install -d -m 755 %{buildroot}/var/log/glu-agent/
cd %{buildroot}/opt/glu/agent-server/data/
ln -s /var/log/glu-agent/ logs
cd -

# Drop init scripts
install -d -m 755 %{buildroot}/%{_initrddir}
install    -m 755 %_sourcedir/glu-agent         %{buildroot}/%{_initrddir}/glu-agent
install    -m 755 %_sourcedir/glu-console-jetty %{buildroot}/%{_initrddir}/glu-console-jetty

install -d -m 755 %{buildroot}/%{glu_home}/console-server/glu/repository/tgzs/
install    -m 644 %{_builddir}/%{glu_pkg}/console-server/glu/repository/tgzs/* %{buildroot}/%{glu_home}/console-server/glu/repository/tgzs/

# Place Jetty
#tar -xf %_sourcedir/jetty-distribution-%{jetty_ver}.tar.gz -C %{buildroot}/%{glu_home}
tar -xf %{_builddir}/%{glu_pkg}/console-server/glu/repository/tgzs/jetty-distribution-%{jetty_ver}.tar.gz -C %{buildroot}/%{glu_home}

# Put jetty logging in /var/log
install -d -m 755 %{buildroot}/var/log/glu-console-jetty/
cd %{buildroot}/opt/glu/jetty-distribution-%{jetty_ver}/
rm -rf logs
ln -s /var/log/glu-console-jetty/ logs
cd -

%files
%defattr(-,root,root)
%{glu_home}/*.txt
%{glu_home}/*.md
%{glu_home}/*.html
%{glu_home}/*.rst
%{glu_home}/bin/setup-zookeeper.sh
%{glu_home}/bin/tutorial.sh
%{glu_home}/bin/zookeeper-cli.sh
%{glu_home}/bin/zookeeper-server.sh
%{glu_home}/setup/*

%files agent
%defattr(-,root,root)
%{glu_home}/bin/agent-cli.sh
%{glu_home}/bin/agent-server.sh
%{glu_home}/bin/setup-agent.sh
%{glu_home}/agent-*
/var/log/glu-agent/
%{_initrddir}/glu-agent

%files console
%defattr(-,root,root)
%{glu_home}/bin/console-cli.sh
%{glu_home}/bin/console-server.sh
%{glu_home}/console-*

%files console-jetty
%defattr(-,root,root)
%{glu_home}/jetty*/*
%{_initrddir}/glu-console-jetty
/var/log/glu-console-jetty/

%define service_macro() \
%post %1 \
chkconfig --add %{name}-%1 \
\
%preun %1 \
if [ $1 = 0 ]; then \
  service %{name}-%1 stop > /dev/null 2>&1 \
  chkconfig --del %{name}-%1 \
fi \
%postun %1 \
if [ $1 -ge 1 ]; then \
  service %{name}-%1 condrestart >/dev/null 2>&1 \
fi

%service_macro agent
%service_macro console-jetty

%changelog
* Sun Jun 30 2013 Nathan Milford <nathan@milford.io> - 5.0.0-1
- Bumped version.
* Mon Jun 17 2013 Nathan Milford <nathan@milford.io> - 4.7.2-1
- Initial Version
