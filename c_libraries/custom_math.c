#include <Python.h>

static PyObject* simpsons_rule(PyObject* self, PyObject* args, PyObject* kwargs) {
    PyObject *x_obj = NULL, *y_obj = NULL;
    static char* keywords[] = {"x", "y", NULL};

    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "|OO", keywords, &x_obj, &y_obj)) {
            return NULL;
        }

    if (x_obj == NULL || y_obj == NULL) {
        PyErr_SetString(PyExc_ValueError, "X and Y must be provided as keyword arguments");
        return NULL;
    }

    Py_ssize_t n = PyList_Size(x_obj);
    if (n <= 1 || PyList_Size(y_obj) != n) {
        PyErr_SetString(PyExc_ValueError, "X and Y must be non-empty lists of equal length");
        return NULL;
    }

    double *x = (double *)malloc(n * sizeof(double));
    double *y = (double *)malloc(n * sizeof(double));
    if (!x || !y) {
        PyErr_SetString(PyExc_MemoryError, "Failed to allocate memory");
        free(x);
        free(y);
        return NULL;
    }

    // Extract values from Python lists
    for (Py_ssize_t i = 0; i < n; ++i) {
        x[i] = PyFloat_AsDouble(PyList_GetItem(x_obj, i));
        y[i] = PyFloat_AsDouble(PyList_GetItem(y_obj, i));
        if (PyErr_Occurred()) {
            free(x);
            free(y);
            return NULL;
        }
    }

    // Simpson's rule integration
    double h = (x[n - 1] - x[0]) / (n - 1);
    double integral = y[0] + y[n - 1]; // First and last terms
    for (int i = 1; i < n - 1; i++) {
        if (i % 2 == 1)
            integral += 4 * y[i];
        else
            integral += 2 * y[i];
    }

    integral *= h / 3;

    free(x);
    free(y);

    return Py_BuildValue("d", integral);
}

static PyMethodDef methods[] = {
    {"simpsons_rule", (PyCFunction)simpsons_rule, METH_VARARGS | METH_KEYWORDS, "Numerical integration using Simpson's rule."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "custom_math",
    "Custom extension to do fast math operations.",
    -1,
    methods
};

PyMODINIT_FUNC PyInit_custom_math(void) {
    return PyModule_Create(&module);
}
