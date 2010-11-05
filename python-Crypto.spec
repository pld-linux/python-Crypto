%define		module	Crypto
Summary:	PyCrypto - The Python Cryptography Toolkit
Summary(pl.UTF-8):	Kryptograficzny przybornik dla języka Python
Name:		python-%{module}
Version:	2.3
Release:	1
# Mostly Public Domain apart from parts of HMAC.py and setup.py, which are Python
License:	Public Domain and Python
Group:		Development/Languages/Python
Source0:	http://ftp.dlitz.net/pub/dlitz/crypto/pycrypto/pycrypto-%{version}.tar.gz
# Source0-md5:	2b811cfbfc342d83ee614097effb8101
URL:		http://www.dlitz.net/software/pycrypto/
BuildRequires:	python
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Don't want provides for python shared objects
%define		_noautoprovfiles	%{py_sitedir}/%{module}/.*/.*.so

%description
The Toolkit is a collection of cryptographic algorithms and protocols,
implemented for use from Python. Among the contents of the package:
- hash functions: MD2, MD4, RIPEMD
- block encryption algorithms: AES, ARC2, Blowfish, CAST, DES,
  Triple-DES, IDEA, RC5
- stream encryption algorithms: ARC4, simple XOR
- public-key algorithms: RSA, DSA, ElGamal, qNEW
- protocols: All-or-nothing transforms, chaffing/winnowing
- miscellaneous: RFC1751 module for converting 128-key keys into a set
  of English words, primality testing
- some demo programs (currently all quite old and outdated)

%description -l pl.UTF-8
Ten przybornik jest zbiorem kryptograficznych algorytmów i protokołów
zaimplementowanych dla języka Python. Pakiet zawiera między innymi:
- funkcje haszujące: MD2, MD4, RIPEMD
- blokowe algorytmy szyfrujące: AES,ARC2, Blowfish, CAST, DES,
  Triple-DES, IDEA, RC5
- strumieniowe algorytmu szyfrujące: ARC4, zwykły XOR
- algorytmy z kluczem publicznym: RSA, DSA,ElGamal, qNEW
- protokoły: przekształcenia wszystko-albo-nic, chaffing/winnowing
- inne: RFC1751 moduł do konwersji kluczy 128 bitowych w zbiory słów
  angielskich, test liczb pierwszych
- programy demo (aktualnie odrobinę starych)

%prep
%setup -q -n pycrypto-%{version}

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

rm -rf $RPM_BUILD_ROOT%{py_sitedir}/Crypto/SelfTest

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKS COPYRIGHT ChangeLog README TODO Doc
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%dir %{py_sitedir}/%{module}/Cipher
%dir %{py_sitedir}/%{module}/Hash
%dir %{py_sitedir}/%{module}/Protocol
%dir %{py_sitedir}/%{module}/PublicKey
%dir %{py_sitedir}/%{module}/Random
%dir %{py_sitedir}/%{module}/Random/Fortuna
%dir %{py_sitedir}/%{module}/Random/OSRNG
%dir %{py_sitedir}/%{module}/Util
%attr(755,root,root) %{py_sitedir}/%{module}/*/*.so
%{py_sitedir}/%{module}/*/*.py[co]
%{py_sitedir}/%{module}/*/*/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitedir}/pycrypto-*.egg-info
%endif
