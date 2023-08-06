package main

// #include <Python.h>
// int PyArg_ParseTuple_ssiisis(PyObject* args, char** a, char** b, int* c, int* d, char** e, int* f, char** g);
// int PyArg_ParseTuple_ssi(PyObject* args, char** a, char** b, int* c);
// void raise_exception(char *msg);
import "C"

import (
	"github.com/pytogo/portforward/internal"
)

//export forward
func forward(self *C.PyObject, args *C.PyObject) *C.PyObject {
	// Interface for C extension and only part that contains C.

	// Strings should not need to be freed
	// > A pointer to an existing string is stored in the character pointer variable whose address you pass.
	// https://docs.python.org/3/c-api/arg.html
	var namespace *C.char
	var podName *C.char

	var fromPort C.int
	var toPort C.int

	var configPath *C.char
	var logLevel C.int

	var kubeContext *C.char

	if C.PyArg_ParseTuple_ssiisis(args, &namespace, &podName, &fromPort, &toPort, &configPath, &logLevel, &kubeContext) == 0 {
		C.raise_exception(C.CString("Could not parse args"))
		return nil
	}

	var ns string = C.GoString(namespace)
	var pod string = C.GoString(podName)

	var cPath string = C.GoString(configPath)
	cLLevel := int(logLevel)

	var kContext string = C.GoString(kubeContext)

	if err := internal.Forward(ns, pod, int(fromPort), int(toPort), cPath, cLLevel, kContext); err != nil {
		C.raise_exception(C.CString(err.Error()))
		return nil
	}

	C.Py_IncRef(C.Py_None)
	return C.Py_None
}

//export stop
func stop(self *C.PyObject, args *C.PyObject) *C.PyObject {
	// Interface for C extension and only part that contains C.

	// Strings should not need to be freed
	// > A pointer to an existing string is stored in the character pointer variable whose address you pass.
	// https://docs.python.org/3/c-api/arg.html
	var namespace *C.char
	var podName *C.char
	var toPort C.int

	if C.PyArg_ParseTuple_ssi(args, &namespace, &podName, &toPort) == 0 {
		C.raise_exception(C.CString("Could not parse args"))
		return nil
	}

	var ns string = C.GoString(namespace)
	var pod string = C.GoString(podName)

	internal.StopForwarding(ns, pod, int(toPort))

	C.Py_IncRef(C.Py_None)
	return C.Py_None
}

func main() {}
