#include <nanobind/nanobind.h>

namespace nb = nanobind;

using namespace nb::literals;

struct Foo {
    int a;
    float b;
};

Foo makeFoo(int _a, float _b) {
    Foo foo = {_a, _b};
    return foo;
}

NB_MODULE(nanobind_example_ext, m) {
    m.def("add", [](int a, int b) { return a + b; }, "a"_a, "b"_a);

    nb::class_<Foo>(m, "Foo")
      .def_readonly("a", &Foo::a)
      .def_readonly("b", &Foo::b);

    m.def("make_foo", &makeFoo, nb::arg("a"), nb::arg("b"));

}
