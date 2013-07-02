rpm-glu
=======

An RPM spec file to build and install the Glu deployment automation platform.

`sudo yum -y install rpmdevtools && rpmdev-setuptree`
 
`wget https://raw.github.com/nmilford/rpm-glu/master/glu.spec -O ~/rpmbuild/SPECS/glu.spec`

`wget http://dl.bintray.com/pongasoft/glu/org.linkedin.glu.packaging-all-5.0.0.tgz?direct  -O ~/rpmbuild/SOURCES/org.linkedin.glu.packaging-all-5.0.0.tgz`

`wget https://raw.github.com/nmilford/rpm-glu/master/glu-agent -O ~/rpmbuild/SOURCES/glu-agent`

`wget https://raw.github.com/nmilford/rpm-glu/master/glu-console-jetty -O ~/rpmbuild/SOURCES/glu-console-jetty`
 
`rpmbuild -bb ~/rpmbuild/SPECS/glu.spec`
