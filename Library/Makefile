.PHONY: unpack-deps deps dep-KrisLibrary dep-ode dep-glui dep-tinyxml

ODECONFIG = --with-trimesh=none --disable-demos
#Uncomment this if you want to build ODE as a shared library
#ODECONFIG += --enable-shared
#Comment this out if you want to build ODE in single precision
#(not recommended on Linux, may give reasonable performance on Windows)
ODECONFIG += --enable-double-precision

UNAME = $(shell uname)

unpack-deps:
	git clone https://github.com/krishauser/KrisLibrary
	cd KrisLibrary; git checkout old_motion_planning
	tar xvzf ode-0.11.1.tar.gz
	tar xvzf glui-2.36.tgz

deps: dep-tinyxml dep-glui dep-ode dep-KrisLibrary

dep-KrisLibrary:
	cd KrisLibrary; cmake .
	cd KrisLibrary; make KrisLibrary

dep-tinyxml:
	cd tinyxml; make lib

ifeq ($(UNAME), Darwin)
dep-glui:
	patch -N glui-2.36/src/makefile < glui-mac-osx.patch || true
	cd glui-2.36/src; make
else
dep-glui:
	cd glui-2.36/src; make
endif

dep-ode:
	cd ode-0.11.1; X_EXTRA_LIBS=-lX11 ./configure $(ODECONFIG)
	cd ode-0.11.1/ode/src; make

#NOTE: call sudo make ldconfig-ode if you have set --enable-shared in ODECONFIG
ldconfig-ode:
	echo "$(CURDIR)/ode-0.11.1/ode/src/.libs" > /etc/ld.so.conf.d/ode.conf
	ldconfig
