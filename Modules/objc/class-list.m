/*
 * Implements a function to fetch the list of objective-C classes known
 * in the runtime.
 */
#include "pyobjc.h"

#ifndef GNU_RUNTIME

	/* Implementation for MacOS X */

PyObject*
PyObjC_GetClassList(void)
{
	PyObject* 	result = NULL;
	Class*		buffer = NULL;
	int		bufferLen = 0;
	int		neededLen = 0;
	int             i;
	Class		initialBuffer[1024];

	/*
	 * objc_getClassList returns the number of classes known in the runtime,
	 * the documented way to fetch the list is:
	 * 1. call ret = objc_getClassList(NULL, 0);
	 * 2. allocate a buffer of 'ret' class-pointers
	 * 3. call objc_getClassList again with this buffer.
	 *
	 * Step 3 might return more classes because another thread may have 
	 * loaded a new framework/bundle. This means we need a loop to be sure
	 * we'll get all classes.
	 *
	 * We cheat a little for addition speed: our initial call uses a 
	 * fairly large static buffer, this way we need only one call unless
	 * there is a very large number of classes.
	 */
	neededLen = objc_getClassList(initialBuffer, 1024);
	if (neededLen >= 1024) {
		while (bufferLen < neededLen) {
			Class*    newBuffer;
			bufferLen = neededLen;

			/* Realloc(NULL, ...) might not work, call Malloc when
			 * the buffer is NULL.
			 */
			if (buffer == NULL) {
				newBuffer = malloc(sizeof(Class) * bufferLen);
			} else {
				newBuffer = realloc(buffer, 
						sizeof(Class) * bufferLen);
			}
			if (newBuffer == NULL) {
				PyErr_NoMemory();
				goto error;
			}
			buffer = newBuffer; newBuffer = NULL;
			neededLen = objc_getClassList(buffer, bufferLen);
		}
		bufferLen = neededLen;
	} else {
		bufferLen = neededLen;
		buffer = initialBuffer;
	}

	result = PyTuple_New(bufferLen);
	if (result == NULL) {
		goto error;
	}

	for (i = 0; i < bufferLen; i++) {
		PyObject* pyclass;

		pyclass = PyObjCClass_New(buffer[i]);
		if (pyclass == NULL) {
			goto error;
		}
		PyTuple_SET_ITEM(result, i, pyclass);
	}

	if (buffer != initialBuffer) {
		free(buffer); buffer = NULL;
	}
	return result;

error:
	if (buffer && buffer != initialBuffer) {
		free(buffer);
		buffer = NULL;
	}
	Py_XDECREF(result);
	return NULL;
}

#else	 /* GNU_RUNTIME */

	/* Implementation for the GNU runtime (e.g. GNUstep) */

PyObject*
PyObjC_GetClassList(void)
{
	PyObject* 	result = NULL;
	Class		classid;
	void*	        state = NULL;
	int             len = 0;
	int             i;

	while ((classid = objc_next_class(&state))) len++;

	result = PyTuple_New(len);

	state = NULL; i = 0;

	while ((i < len) && (classid = objc_next_class(&state))) {
		PyObject* pyclass = PyObjCClass_New(classid);
		if (pyclass == NULL) goto error;

		if (PyTuple_SET_ITEM(result, i, pyclass) < 0) {
			Py_DECREF(pyclass);
			goto error;
		}

		i++;
	}

	return result;

error:
	Py_XDECREF(result);
	return NULL;
}

#endif /* GNU_RUNTIME */
