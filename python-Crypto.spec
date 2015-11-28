
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	Crypto
Summary:	PyCrypto - The Python 2 Cryptography Toolkit
Summary(pl.UTF-8):	Kryptograficzny przybornik dla języka Python 2
Name:		python-%{module}
Version:	2.6.1
Release:	5
# Mostly Public Domain apart from parts of HMAC.py and setup.py, which are Python
License:	Public Domain and Python
Group:		Development/Languages/Python
Source0:	http://ftp.dlitz.net/pub/dlitz/crypto/pycrypto/pycrypto-%{version}.tar.gz
# Source0-md5:	55a61a054aa66812daf5161a0d5d7eda
URL:		http://www.dlitz.net/software/pycrypto/
%if %{with python2}
BuildRequires:	python
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-modules
%endif
%if %{with python3}
BuildRequires:	python3
BuildRequires:	python3-2to3
BuildRequires:	python3-devel
BuildRequires:	python3-modules
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
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
%dir %{py_sitedir}/%{module}/Hash
%dir %{py_sitedir}/%{module}/Protocol
%dir %{py_sitedir}/%{module}/PublicKey
%dir %{py_sitedir}/%{module}/Random
%dir %{py_sitedir}/%{module}/Random/Fortuna
%dir %{py_sitedir}/%{module}/Random/OSRNG
%dir %{py_sitedir}/%{module}/Signature
%dir %{py_sitedir}/%{module}/Util
%attr(755,root,root) %{py_sitedir}/%{module}/*/*.so
%{py_sitedir}/%{module}/*/*.py[co]
%{py_sitedir}/%{module}/*/*/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitedir}/pycrypto-*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc ACKS COPYRIGHT ChangeLog README TODO Doc
%dir %{py3_sitedir}/%{module}
%{py3_sitedir}/%{module}/*.py
%{py3_sitedir}/%{module}/__pycache__
%dir %{py3_sitedir}/%{module}/Cipher
%dir %{py3_sitedir}/%{module}/Hash
%dir %{py3_sitedir}/%{module}/Protocol
%dir %{py3_sitedir}/%{module}/PublicKey
%dir %{py3_sitedir}/%{module}/Random
%dir %{py3_sitedir}/%{module}/Random/Fortuna
%dir %{py3_sitedir}/%{module}/Random/OSRNG
%dir %{py3_sitedir}/%{module}/Signature
%dir %{py3_sitedir}/%{module}/Util
%attr(755,root,root) %{py3_sitedir}/%{module}/*/*.so
%{py3_sitedir}/%{module}/*/*.py
%{py3_sitedir}/%{module}/*/__pycache__
%{py3_sitedir}/%{module}/*/*/*.py
%{py3_sitedir}/%{module}/*/*/__pycache__
%{py3_sitedir}/pycrypto-*.egg-info
%endif
