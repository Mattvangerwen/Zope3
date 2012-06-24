#
Summary:	An application server and portal toolkit for building Web sites
Summary(es):	Un servidor de aplicaciones y un conjunto de herramientas para la construcci�n de sitios Web
Summary(pl):	Serwer aplikacji i toolkit portalowy do tworzenia serwis�w WWW
Summary(pt_BR):	Um servidor de aplica��es e um conjunto de ferramentas para constru��o de sites Web
Name:		Zope3
Version:	3.2.0
Release:	1
License:	Zope Public License (ZPL)
Group:		Networking/Daemons
Source0:	http://www.zope.org/Products/Zope3/%{version}final/Zope-%{version}.tgz
# Source0-md5:	dbbb708281ebcf7186aa7aa3ee46844c
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Source3:	%{name}.logrotate
Source4:	mkzope3instance
Source5:	installzope3package
Patch0:		%{name}-skeleton_path.patch
Patch1:		%{name}-python_2_4_2.patch
URL:		http://dev.zope.org/Zope3
BuildRequires:	perl-base
BuildRequires:	python-devel >= 1:2.4.1
BuildRequires:	rpmbuild(macros) >= 1.213
Requires(post,preun):	/sbin/chkconfig
Requires(post,preun):	rc-scripts
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	expat >= 1.95.7
Requires:	logrotate
Requires:	python >= 2.4.1
Requires:	python-libs >= 2.4.1
Requires:	python-modules >= 2.4.1
Requires:	python-zope = %{epoch}:%{version}-%{release}
Requires:	rc-scripts
%pyrequires_eq	python
Provides:	group(zope)
Provides:	user(zope)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		zope_libdir /usr/%{_lib}/zope3
%define		zope_datadir /usr/share/zope3

%description
The Z Object Programming Environment (Zope) is a free, Open Source
Python-based application server for building high-performance, dynamic
web sites, using a powerful and simple scripting object model and
high-performance, integrated object database.

This project is a redesign of Zope 2 and seeks to improve the Zope
development experience through the use of Interfaces and Components.

%description -l es
Zope es una aplicaci�n basada en Python, Open Source[tm], para la
construcci�n de sitios din�micos, usa un modelo de escritura de
guiones poderoso y sencillo. Para instalar la aplicaci�n Zope, instale
ese paquete y despu�s, Zope-server, para un servidor HTTP integrado
simple, Zope-pcgi, para uso con el servidor Apache. Si desea instalar
solamente algunas partes de la aplicaci�n Zope, est�n diponibles otros
subpaquetes, usted debe instalar �stos en vez de ese RPM.

%description -l pl
Zope (Z Object Programming Environment - Obiektowe �rodowisko
Programistyczne Z) jest opartym o Pythona serwerem aplikacji do
tworzenia wysoko wydajnych, dynamicznych serwis�w WWW, przy u�yciu
u�ytecznego i prostego modelu obiektowego skrypt�w oraz wysoko
wydajnej zintegrowanej obiektowej bazy danych.

%description -l pt_BR
Zope � uma aplica��o baseada em Python, Open Source[tm], para
constru��o de sites din�micos, usando um modelo de scripting poderoso
e simples Para instalar o Zope, instale esse pacote e depois, ou o
Zope-server, para um servidor HTTP integrado simples, ou Zope-pcgi,
para uso com o Apache. Se voc� quiser instalar apenas algumas partes
do Zope, outros sub-pacotes est�o dispon�veis, e voc� deveria instalar
eles ao inv�s desse RPM.

%package -n python-zope
Summary:	Python packages developed as part of the Zope 3 project
Summary(pl):	Modu�y Pythona rozwijane w projekcie Zope 3
Group:		Development/Tools
Provides:	ZopeInterface
Provides:	python-zope-cachedescriptors = %{epoch}:%{version}-%{release}
Provides:	python-zope-component = %{epoch}:%{version}-%{release}
Provides:	python-zope-configuration = %{epoch}:%{version}-%{release}
Provides:	python-zope-deprecation = %{epoch}:%{version}-%{release}
Provides:	python-zope-documenttemplate = %{epoch}:%{version}-%{release}
Provides:	python-zope-event = %{epoch}:%{version}-%{release}
Provides:	python-zope-exceptions = %{epoch}:%{version}-%{release}
Provides:	python-zope-hookable = %{epoch}:%{version}-%{release}
Provides:	python-zope-i18n = %{epoch}:%{version}-%{release}
Provides:	python-zope-i18nmessageid = %{epoch}:%{version}-%{release}
Provides:	python-zope-index = %{epoch}:%{version}-%{release}
Provides:	python-zope-interface = %{epoch}:%{version}-%{release}
Provides:	python-zope-modulealias = %{epoch}:%{version}-%{release}
Provides:	python-zope-pagetemplate = %{epoch}:%{version}-%{release}
Provides:	python-zope-proxy = %{epoch}:%{version}-%{release}
Provides:	python-zope-publisher = %{epoch}:%{version}-%{release}
Provides:	python-zope-schema = %{epoch}:%{version}-%{release}
Provides:	python-zope-security = %{epoch}:%{version}-%{release}
Provides:	python-zope-server = %{epoch}:%{version}-%{release}
Provides:	python-zope-structuredtext = %{epoch}:%{version}-%{release}
Provides:	python-zope-tal = %{epoch}:%{version}-%{release}
Provides:	python-zope-tales = %{epoch}:%{version}-%{release}
Provides:	python-zope-testing = %{epoch}:%{version}-%{release}
Provides:	python-zope-thread = %{epoch}:%{version}-%{release}
Obsoletes:	ZopeInterface

%description -n python-zope
The "zope" package is a pure namespace package holding packages
developed as part of the Zope 3 project.

Generally, the immediate subpackages of the "zope" package should be
useful and usable outside of the Zope application server. Subpackages
of the "zope" package should have minimal interdependencies, although
most depend on "zope.interface".

%description -n python-zope -l pl
Pakiet "zope" to pakiet czystej przestrzeni nazw przechowuj�cej
pakiety tworzone jako cz�� projektu Zope 3.

Og�lnie bezpo�rednie podpakiety pakietu "zope" powinny by� przydatne i
u�ywalne poza serwerem aplikacji Zope. Podpakiety pakietu "zope"
powinny mie� minimalne zale�no�ci wzajemne, chocia� wi�kszo�� zale�y
od "zope.interface".

%prep
%setup -q -n Zope-%{version}
%patch0 -p1
%patch1 -p1

install -m755 %{SOURCE4} ./mkzope3instance

%build
./configure \
	--prefix=%{zope_libdir} \
	--force
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_sbindir},%{zope_datadir}/lib/python} \
	$RPM_BUILD_ROOT{/etc/logrotate.d,/etc/sysconfig,/etc/rc.d/init.d} \
	$RPM_BUILD_ROOT{/var/lib/zope3/main,/var/run/zope3,/var/log/zope3/main} \
$RPM_BUILD_ROOT%{_sysconfdir}/zope3/main

python install.py -q install --skip-build --home "%{zope_libdir}" --root "$RPM_BUILD_ROOT"
mv $RPM_BUILD_ROOT%{zope_libdir}/%{_lib}/python/zope  $RPM_BUILD_ROOT%{py_sitedir}
rm $RPM_BUILD_ROOT%{zope_libdir}/zopeskel/bin/{*.bat.in,zopeservice*}
mv $RPM_BUILD_ROOT%{zope_libdir}/zopeskel $RPM_BUILD_ROOT%{_sysconfdir}/zope3

cat >$RPM_BUILD_ROOT%{zope_libdir}/bin/mkzopeinstance <<EOF
#!/usr/bin/python
import sys
from zope.app.server.mkzopeinstance import main
sys.exit(main(from_checkout=False))
EOF

# plain text
echo "1" | PYTHONPATH="$RPM_BUILD_ROOT%{py_sitedir}:$RPM_BUILD_ROOT%{zope_libdir}/%{_lib}/python" \
	DESTDIR="$RPM_BUILD_ROOT" ./mkzope3instance main \
-u zope:zope -s $RPM_BUILD_ROOT%{_sysconfdir}/zope3/zopeskel

cat >> $RPM_BUILD_ROOT%{py_sitedir}/zope/app/__init__.py <<EOF
import sys
sys.path.insert(0,"%{zope_libdir}/%{_lib}/python")
sys.path.insert(0,"%{zope_datadir}/lib/python")
EOF

%py_comp $RPM_BUILD_ROOT%{py_sitedir}/zope
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/zope
# breaks pyskel
# %%py_postclean

for f in zconfig zconfig_schema2html zopetest; do
	ln -sf %{zope_libdir}/bin/"$f" $RPM_BUILD_ROOT%{_sbindir}/"$f"
done
for f in mkzeoinst runzeo zdctl zdrun zeoctl zeopasswd ; do
	ln -sf %{zope_libdir}/bin/"$f".py $RPM_BUILD_ROOT%{_sbindir}/"$f"
done

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/zope3
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/zope3
install %{SOURCE3} $RPM_BUILD_ROOT/etc/logrotate.d/zope3
install %{SOURCE4} $RPM_BUILD_ROOT%{_sbindir}/mkzope3instance
install %{SOURCE5} $RPM_BUILD_ROOT%{_sbindir}/installzope3package

touch $RPM_BUILD_ROOT/var/log/zope3/main/access.log
touch $RPM_BUILD_ROOT/var/log/zope3/main/transcript.log
touch $RPM_BUILD_ROOT/var/log/zope3/main/z3.log

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 112 zope
%useradd -u 112 -d /var/lib/zope/main -s /bin/false -c "Zope User" -g zope zope

%post
/sbin/chkconfig --add zope3
%service zope3 restart "Zope 3 daemon"

%preun
if [ "$1" = "0" ]; then
	%service zope3 stop
	/sbin/chkconfig --del zope3
fi

%postun
if [ "$1" = "0" ] ; then
	%userremove zope
	%groupremove zope
fi

%files
%defattr(644,root,root,755)
%doc Zope/doc/*
%attr(754,root,root) /etc/rc.d/init.d/zope3
%attr(755,root,root) %{_sbindir}/*
%dir %{zope_libdir}
%dir %{zope_libdir}/bin
%attr(755,root,root) %{zope_libdir}/bin/*
%{zope_libdir}/include
%{zope_libdir}/%{_lib}
%{zope_datadir}
%{py_sitedir}/zope/app
%attr(775,root,zope) %dir /var/run/zope3
%attr(755,root,root) %dir /var/lib/zope3
%attr(775,root,root) %dir /var/lib/zope3/main
%dir /var/lib/zope3/main/bin
%attr(755,root,root) %dir /var/lib/zope3/main/bin/*
/var/lib/zope3/main%{_sysconfdir}
/var/lib/zope3/main/lib
/var/lib/zope3/main/log
%attr(775,root,zope) %dir /var/lib/zope3/main/var
/var/lib/zope3/main/var/README.txt
/var/lib/zope3/main/README.txt
%attr(755,root,zope) %dir /var/log/zope3
%attr(775,root,zope) %dir /var/log/zope3/main
%attr(751,root,zope) %dir %{_sysconfdir}/zope3
%attr(751,root,zope) %dir %{_sysconfdir}/zope3/main
%attr(751,root,zope) %dir %{_sysconfdir}/zope3/main/package-includes
%attr(640,root,zope) %dir %{_sysconfdir}/zope3/main/*.conf
%{_sysconfdir}/zope3/main/*.zcml
%{_sysconfdir}/zope3/main/*.pem
%{_sysconfdir}/zope3/main/ssh_host_rsa_key
%{_sysconfdir}/zope3/main/package-includes/*.zcml
%{_sysconfdir}/zope3/main/package-includes/README.txt
%dir %{_sysconfdir}/zope3/zopeskel
%dir %{_sysconfdir}/zope3/zopeskel/bin
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/zope3/zopeskel/bin/*
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/zope3/zopeskel%{_sysconfdir}
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/zope3/zopeskel/lib
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/zope3/zopeskel/log
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/zope3/zopeskel/var
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/zope3/zopeskel/README.txt
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/zope3
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/zope3
%ghost /var/log/zope3/main/access.log
%ghost /var/log/zope3/main/transcript.log
%ghost /var/log/zope3/main/z3.log

%files -n python-zope
%defattr(644,root,root,755)
%{py_sitedir}/zope
%exclude %{py_sitedir}/zope/app
