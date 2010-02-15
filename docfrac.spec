# TODO:
# - __cc and rpm*flags
Summary:	Convert between RTF, HTML and text format
Summary(pl.UTF-8):	Prosty konwerter RTF/HTML/txt
Name:		docfrac
Version:	3.1.5
Release:	0.1
License:	LGPL
Group:		Applications
Source0:	http://dl.sourceforge.net/docfrac/%{name}-%{version}.src.tar.gz
URL:		http://www.docfrac.net/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DocFrac is a document converter that can convert between RTF, HTML and
ASCII text. This includes RTF to HTML and HTML to RTF.Supports text
formatting (e.g. bold); tables; and most European languages.Available
for Windows; Linux; ActiveX and DLL.

%description -l pl.UTF-8
DocFrac potrafi konwertować pliki w formatach RTF, HTML i tekstowym
ASCII. Konwersja RTF i HTML działa w obie strony. Program obsługuje
formatowanie tekstu (np. pogrubianie), tabele oraz wspiera większość
języków europejskich. Dostępny na platformy Linux i Windows (jako
kontrolka ActiveX i biblioteka DLL).

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install docfrac $RPM_BUILD_ROOT%{_bindir}
install doc/docfrac.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/docfrac
%{_mandir}/man1/docfrac.1*
