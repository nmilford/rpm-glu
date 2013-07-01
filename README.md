rpm-glu
=======

An RPM spec file to build and install the Glu deployment automation platform.

`sudo yum -y install rpmdevtools && rpmdev-setuptree`
 
`wget https://raw.github.com/nmilford/rpm-glu/master/glu.spec -O ~/rpmbuild/SPECS/glu.spec`

`wget http://dl.bintray.com/pongasoft/glu/org.linkedin.glu.packaging-all-5.0.0.tgz?direct  -O ~/rpmbuild/SOURCES/org.linkedin.glu.packaging-all-5.0.0.tgz`

`wget https://raw.github.com/nmilford/rpm-glu/master/glu-agent -O ~/rpmbuild/SOURCES/glu-agent`

`wget https://raw.github.com/nmilford/rpm-glu/master/glu-console -O ~/rpmbuild/SOURCES/glu-console`

`wget http://mirror.cc.columbia.edu/pub/software/eclipse/jetty/8.1.10.v20130312/dist/jetty-distribution-8.1.10.v20130312.tar.gz -O ~/rpmbuild/SOURCES/jetty-distribution-8.1.10.v20130312.tar.gz`

 
`rpmbuild -bb ~/rpmbuild/SPECS/activemq.spec`