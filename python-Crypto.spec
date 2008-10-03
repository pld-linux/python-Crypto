
%define		module	Crypto

Summary:	Python Cryptography Toolkit
Summary(pl.UTF-8):	Kryptograficzny przybornik dla języka Python
Name:		python-%{module}
Version:	2.0.1
Release:	5
License:	Free
Source0:	http://www.amk.ca/files/python/crypto/pycrypto-%{version}.tar.gz
# Source0-md5:	4d5674f3898a573691ffb335e8d749cd
URL:		http://www.amk.ca/python/code/crypto.html
Group:		Development/Languages/Python
%pyrequires_eq	python-modules
BuildRequires:	python
BuildRequires:	python-devel >= 2.2
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

%description -l pl.UTF-8
Ten przybornik jest zbiorem kryptograficznych algorytmów i protokołów
zaimplementowanych dla języka Python. Pakiet zawiera między innymi:
- funkcje haszujące: MD2, MD4, RIPEMD
- blokowe algorytmy szyfrujące: AES,ARC2, Blowfish, CAST, DES, Triple-DES,
  IDEA, RC5
- strumieniowe algorytmu szyfrujące: ARC4, zwykły XOR
- algorytmy z kluczem publicznym: RSA, DSA,ElGamal, qNEW
- protokoły: przekształcenia wszystko-albo-nic, chaffing/winnowing
- inne: RFC1751 moduł do konwersji kluczy 128 bitowych w zbiory słów
  angielskich, test liczb pierwszych
- programy demo (aktualnie odrobinę starych)

%prep
%setup -q -n pycrypto-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

python setup.py install \
	--root=$RPM_BUILD_ROOT --optimize=2

rm -f $RPM_BUILD_ROOT%{py_sitedir}/%{module}{,/*}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKS ChangeLog README TODO Doc
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%dir %{py_sitedir}/%{module}/Cipher
%dir %{py_sitedir}/%{module}/Hash
%dir %{py_sitedir}/%{module}/Protocol
%dir %{py_sitedir}/%{module}/PublicKey
%dir %{py_sitedir}/%{module}/Util
%attr(755,root,root) %{py_sitedir}/%{module}/*/*.so
%{py_sitedir}/%{module}/*/*.py[co]
