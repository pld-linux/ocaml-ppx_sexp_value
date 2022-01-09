#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	A ppx rewriter that simplifies building S-expressions from OCaml values
Summary(pl.UTF-8):	Moduł przepisujący ppx upraszczający budowanie S-wyrażeń z wartości w OCamlu
Name:		ocaml-ppx_sexp_value
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_sexp_value/tags
Source0:	https://github.com/janestreet/ppx_sexp_value/archive/v%{version}/ppx_sexp_value-%{version}.tar.gz
# Source0-md5:	ef47fa8e25308e645552ad7bf5c06d28
URL:		https://github.com/janestreet/ppx_sexp_value
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppx_here-devel >= 0.14
BuildRequires:	ocaml-ppx_here-devel < 0.15
BuildRequires:	ocaml-ppx_sexp_conv-devel >= 0.14
BuildRequires:	ocaml-ppx_sexp_conv-devel < 0.15
BuildRequires:	ocaml-ppxlib-devel >= 0.11.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
A ppx rewriter that simplifies building S-expressions from OCaml
values.

This package contains files needed to run bytecode executables using
ppx_sexp_value library.

%description -l pl.UTF-8
Moduł przepisujący ppx upraszczający budowanie S-wyrażeń z wartości w
OCamlu.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_sexp_value.

%package devel
Summary:	A ppx rewriter that simplifies building S-expressions from OCaml values - development part
Summary(pl.UTF-8):	Moduł przepisujący ppx upraszczający budowanie S-wyrażeń z wartości w OCamlu - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-ppx_here-devel >= 0.14
Requires:	ocaml-ppx_sexp_conv-devel >= 0.14
Requires:	ocaml-ppxlib-devel >= 0.11.0

%description devel
This package contains files needed to develop OCaml programs using
ppx_sexp_value library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_sexp_value.

%prep
%setup -q -n ppx_sexp_value-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_sexp_value/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_sexp_value

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/ppx_sexp_value
%attr(755,root,root) %{_libdir}/ocaml/ppx_sexp_value/ppx.exe
%{_libdir}/ocaml/ppx_sexp_value/META
%{_libdir}/ocaml/ppx_sexp_value/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_sexp_value/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_sexp_value/*.cmi
%{_libdir}/ocaml/ppx_sexp_value/*.cmt
%{_libdir}/ocaml/ppx_sexp_value/*.cmti
%{_libdir}/ocaml/ppx_sexp_value/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_sexp_value/ppx_sexp_value.a
%{_libdir}/ocaml/ppx_sexp_value/*.cmx
%{_libdir}/ocaml/ppx_sexp_value/*.cmxa
%endif
%{_libdir}/ocaml/ppx_sexp_value/dune-package
%{_libdir}/ocaml/ppx_sexp_value/opam
