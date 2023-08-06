#include <Python.h>

// ===== START PYTHON PART =====

/* Will come from go */
PyObject* forward(PyObject* , PyObject*);
PyObject* stop(PyObject* , PyObject*);

/*
To shim go's missing variadic function support.

Ref https://docs.python.org/3/c-api/arg.html

Reminder from docs about memory management when parsing arguments:
> In general, when a format sets a pointer to a buffer,
> the buffer is managed by the corresponding Python object,
> and the buffer shares the lifetime of this object. You
> won’t have to release any memory yourself. The only
> exceptions are es, es#, et and et#.
*/
int PyArg_ParseTuple_ssiisis(PyObject* args, char** a, char** b, int* c, int* d, char** e, int* f, char** g) {
    return PyArg_ParseTuple(args, "ssiisis", a, b, c, d, e, f, g);
}

int PyArg_ParseTuple_ssi(PyObject* args, char** a, char** b, int* c) {
    return PyArg_ParseTuple(args, "ssi", a, b, c);
}

static struct PyMethodDef methods[] = {
    {
    "forward",
    (PyCFunction)forward,
    METH_VARARGS,
    "Connects to a Pod and tunnels traffic from a local port to this pod. It uses the kubectl kube config from the home dir."
    },
    {
    "stop",
    (PyCFunction)stop,
    METH_VARARGS,
    "Stops a port-forwarding."
    },
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "_portforward",
    "Kubernetes Port-Forward Go-Edition For Python",
    -1,
    methods
};

static PyObject *PortforwardError = NULL;

PyMODINIT_FUNC PyInit__portforward(void) {
    PyObject *m;

    m = PyModule_Create(&module);
    if (m == NULL)
        return NULL;

    /* Initialize new exception object */
    PortforwardError = PyErr_NewException("_portforward.PortforwardError", PyExc_RuntimeError, NULL);
    Py_XINCREF(PortforwardError);

    /* Add exception object to your module */
    if (PyModule_AddObject(m, "error", PortforwardError) < 0) {
        Py_XDECREF(PortforwardError);
        Py_CLEAR(PortforwardError);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}

// ===== END PYTHON PART =====

void raise_exception(char *msg) {
    PyErr_SetString(PortforwardError, msg);
}
