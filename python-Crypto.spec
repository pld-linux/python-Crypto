%include	/usr/lib/rpm/macros.python

%define         module Crypto

Summary:	Python Cryptography Toolkit
Summary(pl):	Kryptograficzny przybornik dla jêzyka Python
Name:		python-%{module}
Version:	1.9a4
Release:	1
License:	Free
Source0:	http://www.amk.ca/files/python/pycrypto-%{version}.tar.gz
URL:		http://www.amk.ca/python/code/crypto.html
Group:		Development/Languages/Python
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Toolkit is a collection of cryptographic algorithms and protocols,
implemented for use from Python. Among the contents of the package:
- hash functions: MD2, MD4, RIPEMD
- block encryption algorithms: AES, ARC2, Blowfish, CAST, DES, Triple-DES,
  IDEA, RC5
- stream encryption algorithms: ARC4, simple XOR
- public-key algorithms: RSA, DSA, ElGamal, qNEW
- protocols: All-or-nothing transforms, chaffing/winnowing
- miscellaneous: RFC1751 module for converting 128-key keys into a set
  of English words, primality testing
- some demo programs (currently all quite old and outdated)

%description -l pl
Przybornik jest zbiorem kryptograficznych algorytmów i protoko³ów
zaimplementowanych dla jêzyka Python. Pakiet zawiera miêdzy innymi:
- funkcje hashuj±ce: MD2, MD4, RIPEMD
- blokowe algorytmy szyfruj±ce: AES,ARC2, Blowfish, CAST, DES, Triple-DES,
  IDEA, RC5
- strumieniowe algorytmu szyfruj±ce: ARC4, zwyk³y XOR
- algorytmy z kluczem publicznym: RSA, DSA,ElGamal, qNEW
- protocols: All-or-nothing transforms, chaffing/winnowing 
- inne: RFC1751 modu³ do konwersji kluczy 128 bitowych w zbiory s³ów
  angielskich, test liczb pierwszych
- programy demo (aktualnie odrobine starych)

%prep
%setup -q -n pycrypto-%{version}

%build
CFLAGS="%{rpmcflags}"
export CLFAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

python setup.py install \
        --root=$RPM_BUILD_ROOT --optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKS ChangeLog README TODO Doc Demo
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]

%dir %{py_sitedir}/%{module}/Cipher
%attr(755,root,root) %{py_sitedir}/%{module}/Cipher/*.so
%{py_sitedir}/%{module}/Cipher/*.py[co]

%dir %{py_sitedir}/%{module}/Hash
%attr(755,root,root) %{py_sitedir}/%{module}/Hash/*.so
%{py_sitedir}/%{module}/Hash/*.py[co]

%dir %{py_sitedir}/%{module}/Protocol
%{py_sitedir}/%{module}/Protocol/*.py[co]

%dir %{py_sitedir}/%{module}/PublicKey
%{py_sitedir}/%{module}/PublicKey/*.py[co]

%dir %{py_sitedir}/%{module}/Util
%{py_sitedir}/%{module}/Util/*.py[co]
