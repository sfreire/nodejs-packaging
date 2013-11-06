#!/bin/bash

SPEC=nodejs-packaging.spec
VERSION=$(cat nodejs-packaging.spec |grep "Version:"| tr -d " "| cut -d ":" -f 2)
RELEASE=$(cat nodejs-packaging.spec |grep "Release:"| tr -d " "| cut -d ":" -f 2  | cut -d "%" -f 1)
RELEASE=$RELEASE.el5
DESTDIR=/tmp
#RPMTOPDIR=./rpmbuild

#mkdir -p $RPMTOPDIR/{SOURCES,SPECS,BUILD,SRPMS,RPMS,BUILDROOT}

wget --no-check-certificate -q -c https://fedorahosted.org/released/nodejs-packaging/nodejs-packaging-el6-$VERSION.tar.xz

CONFIG=ptin-5-x86_64
#mock -r $CONFIG --buildsrpm --spec $RPMTOPDIR/SPECS/$SPEC  --sources $RPMTOPDIR/SOURCES/
mock -r $CONFIG --buildsrpm --spec $SPEC  --sources . 
[ $? -eq 0 ] || exit 1
cp /var/lib/mock/$CONFIG/result/nodejs-packaging-$VERSION-$RELEASE.src.rpm $DESTDIR
[ $? -eq 0 ] || exit 1
mock -r $CONFIG --rebuild /$DESTDIR/nodejs-packaging-$VERSION-$RELEASE.src.rpm
[ $? -eq 0 ] || exit 1
cp /var/lib/mock/$CONFIG/result/nodejs-packaging-$VERSION-$RELEASE.noarch.rpm  $DESTDIR
