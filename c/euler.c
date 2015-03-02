#include <Python.h>
#include <math.h>

static PyObject * is_prime(PyObject *self, PyObject *args) {
    int n;

    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;

    if (n <= 1) {
        return Py_BuildValue("i", 0);
    }
    if (n < 4) {
        return Py_BuildValue("i", 1); // 2 and 3 are prime
    }
    if (n % 2 == 0) {
        return Py_BuildValue("i", 0);
    }
    if (n < 9) {
        return Py_BuildValue("i", 1); // we have already excluded 4, 6 and 8
    }
    if (n % 3 == 0) {
        return Py_BuildValue("i", 0);
    }

    int limit = (int) sqrt(n);
    int k = 5;
    while (k <= limit) { // check through all the numbers of the form 6k ± 1
        if (n % k == 0 || n % (k+2) == 0) {
            return Py_BuildValue("i", 0);
        }
        k += 6;
    }
    return Py_BuildValue("i", 1);
}

static PyMethodDef eulerMethods[] = {
    {"is_prime",  is_prime, METH_VARARGS, "Check if a number is prime"},
    {NULL}
};

PyMODINIT_FUNC initeuler(void) {
    (void) Py_InitModule("euler", eulerMethods);
}
