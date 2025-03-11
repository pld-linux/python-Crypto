
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	Crypto
Summary:	PyCrypto - The Python 2 Cryptography Toolkit
Summary(pl.UTF-8):	Kryptograficzny przybornik dla języka Python 2
Name:		python-%{module}
Version:	2.6.1
Release:	19
# Mostly Public Domain apart from parts of HMAC.py and setup.py, which are Python
License:	Public Domain and Python
Group:		Development/Languages/Python
Source0:	http://ftp.dlitz.net/pub/dlitz/crypto/pycrypto/pycrypto-%{version}.tar.gz
# Source0-md5:	55a61a054aa66812daf5161a0d5d7eda
Patch0:		pycrypto-optflags.patch
Patch1:		pycrypto-CVE-2013-7459.patch
Patch2:		pycrypto-CVE-2018-6594.patch
Patch3:		pycrypto-fix-pubkey-size-divisions.patch
Patch4:		pycrypto-unbundle-libtomcrypt.patch
Patch5:		pycrypto-link.patch
Patch6:		pycrypto-use-os-random.patch
Patch7:		pycrypto-drop-py2.1-support.patch
Patch8:		pycrypto-python3.10.patch
Patch9:		pycrypto-python3.11.patch
Patch10:	pycrypto-python3.12.patch
Patch11:	pycrypto-no-distutils.patch
Patch12:	pycrypto-SyntaxWarning.patch
Patch13:	pycrypto-2to3.patch
URL:		http://www.dlitz.net/software/pycrypto/
BuildRequires:	gmp-devel
%if %{with python2}
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules >= 1:2.5
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-2to3 >= 1:3.2
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Don't want provides for python shared objects
%define		_noautoprovfiles	%{py_sitedir}/%{module}/.*/.*.so

%description
The Toolkit is a collection of cryptographic algorithms and protocols,
implemented for use from Python 2. Among the contents of the package:
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
zaimplementowanych dla języka Python 2. Pakiet zawiera między innymi:
- funkcje haszujące: MD2, MD4, RIPEMD
- blokowe algorytmy szyfrujące: AES,ARC2, Blowfish, CAST, DES,
  Triple-DES, IDEA, RC5
- strumieniowe algorytmu szyfrujące: ARC4, zwykły XOR
- algorytmy z kluczem publicznym: RSA, DSA,ElGamal, qNEW
- protokoły: przekształcenia wszystko-albo-nic, chaffing/winnowing
- inne: RFC1751 moduł do konwersji kluczy 128 bitowych w zbiory słów
  angielskich, test liczb pierwszych
- programy demonstracyjne (aktualnie odrobinę stare i nieaktualne)

%package -n python3-%{module}
Summary:	PyCrypto - The Python 3 Cryptography Toolkit
Summary(pl.UTF-8):	Kryptograficzny przybornik dla języka Python 3
Group:		Development/Languages/Python

%description -n python3-%{module}
The Toolkit is a collection of cryptographic algorithms and protocols,
implemented for use from Python 3. Among the contents of the package:
- hash functions: MD2, MD4, RIPEMD
- block encryption algorithms: AES, ARC2, Blowfish, CAST, DES,
  Triple-DES, IDEA, RC5
- stream encryption algorithms: ARC4, simple XOR
- public-key algorithms: RSA, DSA, ElGamal, qNEW
- protocols: All-or-nothing transforms, chaffing/winnowing
- miscellaneous: RFC1751 module for converting 128-key keys into a set
  of English words, primality testing
- some demo programs (currently all quite old and outdated)

%description -n python3-%{module} -l pl.UTF-8
Ten przybornik jest zbiorem kryptograficznych algorytmów i protokołów
zaimplementowanych dla języka Python 3. Pakiet zawiera między innymi:
- funkcje haszujące: MD2, MD4, RIPEMD
- blokowe algorytmy szyfrujące: AES,ARC2, Blowfish, CAST, DES,
  Triple-DES, IDEA, RC5
- strumieniowe algorytmu szyfrujące: ARC4, zwykły XOR
- algorytmy z kluczem publicznym: RSA, DSA,ElGamal, qNEW
- protokoły: przekształcenia wszystko-albo-nic, chaffing/winnowing
- inne: RFC1751 moduł do konwersji kluczy 128 bitowych w zbiory słów
  angielskich, test liczb pierwszych
- programy demonstracyjne (aktualnie odrobinę stare i nieaktualne)

%prep
%setup -q -n pycrypto-%{version}
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1
%patch -P 9 -p1
%patch -P 10 -p1
%patch -P 11 -p1
%patch -P 12 -p1
%patch -P 13 -p1

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/Crypto/SelfTest
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/Crypto/SelfTest
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc ACKS COPYRIGHT ChangeLog README TODO Doc
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%dir %{py_sitedir}/%{module}/Cipher
%attr(755,root,root) %{py_sitedir}/%{module}/Cipher/_*.so
%{py_sitedir}/%{module}/Cipher/*.py[co]
%dir %{py_sitedir}/%{module}/Hash
%attr(755,root,root) %{py_sitedir}/%{module}/Hash/_*.so
%{py_sitedir}/%{module}/Hash/*.py[co]
%dir %{py_sitedir}/%{module}/Protocol
%{py_sitedir}/%{module}/Protocol/*.py[co]
%dir %{py_sitedir}/%{module}/PublicKey
%attr(755,root,root) %{py_sitedir}/%{module}/PublicKey/_fastmath.so
%{py_sitedir}/%{module}/PublicKey/*.py[co]
%dir %{py_sitedir}/%{module}/Random
%{py_sitedir}/%{module}/Random/*.py[co]
%dir %{py_sitedir}/%{module}/Random/Fortuna
%{py_sitedir}/%{module}/Random/Fortuna/*.py[co]
%dir %{py_sitedir}/%{module}/Signature
%{py_sitedir}/%{module}/Signature/*.py[co]
%dir %{py_sitedir}/%{module}/Util
%attr(755,root,root) %{py_sitedir}/%{module}/Util/_counter.so
%attr(755,root,root) %{py_sitedir}/%{module}/Util/strxor.so
%{py_sitedir}/%{module}/Util/*.py[co]
%{py_sitedir}/pycrypto-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc ACKS COPYRIGHT ChangeLog README TODO Doc
%dir %{py3_sitedir}/%{module}
%{py3_sitedir}/%{module}/*.py
%{py3_sitedir}/%{module}/__pycache__
%dir %{py3_sitedir}/%{module}/Cipher
%attr(755,root,root) %{py3_sitedir}/%{module}/Cipher/_*.cpython-*.so
%{py3_sitedir}/%{module}/Cipher/*.py
%{py3_sitedir}/%{module}/Cipher/__pycache__
%dir %{py3_sitedir}/%{module}/Hash
%attr(755,root,root) %{py3_sitedir}/%{module}/Hash/_*.cpython-*.so
%{py3_sitedir}/%{module}/Hash/*.py
%{py3_sitedir}/%{module}/Hash/__pycache__
%dir %{py3_sitedir}/%{module}/Protocol
%{py3_sitedir}/%{module}/Protocol/*.py
%{py3_sitedir}/%{module}/Protocol/__pycache__
%dir %{py3_sitedir}/%{module}/PublicKey
%attr(755,root,root) %{py3_sitedir}/%{module}/PublicKey/_fastmath.cpython-*.so
%{py3_sitedir}/%{module}/PublicKey/*.py
%{py3_sitedir}/%{module}/PublicKey/__pycache__
%dir %{py3_sitedir}/%{module}/Random
%{py3_sitedir}/%{module}/Random/*.py
%{py3_sitedir}/%{module}/Random/__pycache__
%dir %{py3_sitedir}/%{module}/Random/Fortuna
%{py3_sitedir}/%{module}/Random/Fortuna/*.py
%{py3_sitedir}/%{module}/Random/Fortuna/__pycache__
%dir %{py3_sitedir}/%{module}/Signature
%{py3_sitedir}/%{module}/Signature/*.py
%{py3_sitedir}/%{module}/Signature/__pycache__
%dir %{py3_sitedir}/%{module}/Util
%attr(755,root,root) %{py3_sitedir}/%{module}/Util/_counter.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/%{module}/Util/strxor.cpython-*.so
%{py3_sitedir}/%{module}/Util/*.py
%{py3_sitedir}/%{module}/Util/__pycache__
%{py3_sitedir}/pycrypto-%{version}-py*.egg-info
%endif
