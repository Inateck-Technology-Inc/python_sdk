# This file was autogenerated by some hot garbage in the `uniffi` crate.
# Trust me, you don't want to mess with it!

# Tell mypy (a type checker) to ignore all errors from this file.
# See https://mypy.readthedocs.io/en/stable/config_file.html?highlight=ignore-errors#confval-ignore_errors
# mypy: ignore-errors

# Common helper code.
#
# Ideally this would live in a separate .py file where it can be unittested etc
# in isolation, and perhaps even published as a re-useable package.
#
# However, it's important that the details of how this helper code works (e.g. the
# way that different builtin types are passed across the FFI) exactly match what's
# expected by the rust code on the other side of the interface. In practice right
# now that means coming from the exact some version of `uniffi` that was used to
# compile the rust component. The easiest way to ensure this is to bundle the Python
# helpers directly inline like we're doing here.

import os
import sys
import ctypes
import enum
import struct
import contextlib
import datetime

# Used for default argument values
DEFAULT = object()


class RustBuffer(ctypes.Structure):
    _fields_ = [
        ("capacity", ctypes.c_int32),
        ("len", ctypes.c_int32),
        ("data", ctypes.POINTER(ctypes.c_char)),
    ]

    @staticmethod
    def alloc(size):
        return rust_call(_UniFFILib.ffi_scanner_d0b2_rustbuffer_alloc, size)

    @staticmethod
    def reserve(rbuf, additional):
        return rust_call(_UniFFILib.ffi_scanner_d0b2_rustbuffer_reserve, rbuf, additional)

    def free(self):
        return rust_call(_UniFFILib.ffi_scanner_d0b2_rustbuffer_free, self)

    def __str__(self):
        return "RustBuffer(capacity={}, len={}, data={})".format(
            self.capacity,
            self.len,
            self.data[0:self.len]
        )

    @contextlib.contextmanager
    def allocWithBuilder():
        """Context-manger to allocate a buffer using a RustBufferBuilder.

        The allocated buffer will be automatically freed if an error occurs, ensuring that
        we don't accidentally leak it.
        """
        builder = RustBufferBuilder()
        try:
            yield builder
        except:
            builder.discard()
            raise

    @contextlib.contextmanager
    def consumeWithStream(self):
        """Context-manager to consume a buffer using a RustBufferStream.

        The RustBuffer will be freed once the context-manager exits, ensuring that we don't
        leak it even if an error occurs.
        """
        try:
            s = RustBufferStream(self)
            yield s
            if s.remaining() != 0:
                raise RuntimeError("junk data left in buffer after consuming")
        finally:
            self.free()


class ForeignBytes(ctypes.Structure):
    _fields_ = [
        ("len", ctypes.c_int32),
        ("data", ctypes.POINTER(ctypes.c_char)),
    ]

    def __str__(self):
        return "ForeignBytes(len={}, data={})".format(self.len, self.data[0:self.len])


class RustBufferStream(object):
    """
    Helper for structured reading of bytes from a RustBuffer
    """

    def __init__(self, rbuf):
        self.rbuf = rbuf
        self.offset = 0

    def remaining(self):
        return self.rbuf.len - self.offset

    def _unpack_from(self, size, format):
        if self.offset + size > self.rbuf.len:
            raise InternalError("read past end of rust buffer")
        value = struct.unpack(format, self.rbuf.data[self.offset:self.offset+size])[0]
        self.offset += size
        return value

    def read(self, size):
        if self.offset + size > self.rbuf.len:
            raise InternalError("read past end of rust buffer")
        data = self.rbuf.data[self.offset:self.offset+size]
        self.offset += size
        return data

    def readI8(self):
        return self._unpack_from(1, ">b")

    def readU8(self):
        return self._unpack_from(1, ">B")

    def readI16(self):
        return self._unpack_from(2, ">h")

    def readU16(self):
        return self._unpack_from(2, ">H")

    def readI32(self):
        return self._unpack_from(4, ">i")

    def readU32(self):
        return self._unpack_from(4, ">I")

    def readI64(self):
        return self._unpack_from(8, ">q")

    def readU64(self):
        return self._unpack_from(8, ">Q")

    def readFloat(self):
        v = self._unpack_from(4, ">f")
        return v

    def readDouble(self):
        return self._unpack_from(8, ">d")


class RustBufferBuilder(object):
    """
    Helper for structured writing of bytes into a RustBuffer.
    """

    def __init__(self):
        self.rbuf = RustBuffer.alloc(16)
        self.rbuf.len = 0

    def finalize(self):
        rbuf = self.rbuf
        self.rbuf = None
        return rbuf

    def discard(self):
        if self.rbuf is not None:
            rbuf = self.finalize()
            rbuf.free()

    @contextlib.contextmanager
    def _reserve(self, numBytes):
        if self.rbuf.len + numBytes > self.rbuf.capacity:
            self.rbuf = RustBuffer.reserve(self.rbuf, numBytes)
        yield None
        self.rbuf.len += numBytes

    def _pack_into(self, size, format, value):
        with self._reserve(size):
            # XXX TODO: I feel like I should be able to use `struct.pack_into` here but can't figure it out.
            for i, byte in enumerate(struct.pack(format, value)):
                self.rbuf.data[self.rbuf.len + i] = byte

    def write(self, value):
        with self._reserve(len(value)):
            for i, byte in enumerate(value):
                self.rbuf.data[self.rbuf.len + i] = byte

    def writeI8(self, v):
        self._pack_into(1, ">b", v)

    def writeU8(self, v):
        self._pack_into(1, ">B", v)

    def writeI16(self, v):
        self._pack_into(2, ">h", v)

    def writeU16(self, v):
        self._pack_into(2, ">H", v)

    def writeI32(self, v):
        self._pack_into(4, ">i", v)

    def writeU32(self, v):
        self._pack_into(4, ">I", v)

    def writeI64(self, v):
        self._pack_into(8, ">q", v)

    def writeU64(self, v):
        self._pack_into(8, ">Q", v)

    def writeFloat(self, v):
        self._pack_into(4, ">f", v)

    def writeDouble(self, v):
        self._pack_into(8, ">d", v)
# A handful of classes and functions to support the generated data structures.
# This would be a good candidate for isolating in its own ffi-support lib.

class InternalError(Exception):
    pass

class RustCallStatus(ctypes.Structure):
    """
    Error runtime.
    """
    _fields_ = [
        ("code", ctypes.c_int8),
        ("error_buf", RustBuffer),
    ]

    # These match the values from the uniffi::rustcalls module
    CALL_SUCCESS = 0
    CALL_ERROR = 1
    CALL_PANIC = 2

    def __str__(self):
        if self.code == RustCallStatus.CALL_SUCCESS:
            return "RustCallStatus(CALL_SUCCESS)"
        elif self.code == RustCallStatus.CALL_ERROR:
            return "RustCallStatus(CALL_ERROR)"
        elif self.code == RustCallStatus.CALL_PANIC:
            return "RustCallStatus(CALL_PANIC)"
        else:
            return "RustCallStatus(<invalid code>)"

def rust_call(fn, *args):
    # Call a rust function
    return rust_call_with_error(None, fn, *args)

def rust_call_with_error(error_ffi_converter, fn, *args):
    # Call a rust function and handle any errors
    #
    # This function is used for rust calls that return Result<> and therefore can set the CALL_ERROR status code.
    # error_ffi_converter must be set to the FfiConverter for the error class that corresponds to the result.
    call_status = RustCallStatus(code=RustCallStatus.CALL_SUCCESS, error_buf=RustBuffer(0, 0, None))

    args_with_error = args + (ctypes.byref(call_status),)
    result = fn(*args_with_error)
    if call_status.code == RustCallStatus.CALL_SUCCESS:
        return result
    elif call_status.code == RustCallStatus.CALL_ERROR:
        if error_ffi_converter is None:
            call_status.error_buf.free()
            raise InternalError("rust_call_with_error: CALL_ERROR, but error_ffi_converter is None")
        else:
            raise error_ffi_converter.lift(call_status.error_buf)
    elif call_status.code == RustCallStatus.CALL_PANIC:
        # When the rust code sees a panic, it tries to construct a RustBuffer
        # with the message.  But if that code panics, then it just sends back
        # an empty buffer.
        if call_status.error_buf.len > 0:
            msg = FfiConverterString.lift(call_status.error_buf)
        else:
            msg = "Unknown rust panic"
        raise InternalError(msg)
    else:
        raise InternalError("Invalid RustCallStatus code: {}".format(
            call_status.code))

# A function pointer for a callback as defined by UniFFI.
# Rust definition `fn(handle: u64, method: u32, args: RustBuffer, buf_ptr: *mut RustBuffer) -> int`
FOREIGN_CALLBACK_T = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_ulonglong, ctypes.c_ulong, RustBuffer, ctypes.POINTER(RustBuffer))
# Types conforming to `FfiConverterPrimitive` pass themselves directly over the FFI.
class FfiConverterPrimitive:
    @classmethod
    def lift(cls, value):
        return value

    @classmethod
    def lower(cls, value):
        return value

# Helper class for wrapper types that will always go through a RustBuffer.
# Classes should inherit from this and implement the `read` and `write` static methods.
class FfiConverterRustBuffer:
    @classmethod
    def lift(cls, rbuf):
        with rbuf.consumeWithStream() as stream:
            return cls.read(stream)

    @classmethod
    def lower(cls, value):
        with RustBuffer.allocWithBuilder() as builder:
            cls.write(value, builder)
            return builder.finalize()

# Contains loading, initialization code,
# and the FFI Function declarations in a com.sun.jna.Library.
# This is how we find and load the dynamic library provided by the component.
# For now we just look it up by name.
#
# XXX TODO: This will probably grow some magic for resolving megazording in future.
# E.g. we might start by looking for the named component in `libuniffi.so` and if
# that fails, fall back to loading it separately from `lib${componentName}.so`.

from pathlib import Path

def loadIndirect():
    if sys.platform == "darwin":
        libname = "lib/scanner_macos_arm64.dylib"
    elif sys.platform.startswith("win"):
        # As of python3.8, ctypes does not seem to search $PATH when loading DLLs.
        # We could use `os.add_dll_directory` to configure the search path, but
        # it doesn't feel right to mess with application-wide settings. Let's
        # assume that the `.dll` is next to the `.py` file and load by full path.
        libname = "lib/scanner_windows.dll"
    else:
        # Anything else must be an ELF platform - Linux, *BSD, Solaris/illumos
        libname = "lib{}.so"

    lib = libname.format("scanner")
    path = str(Path(__file__).parent / lib)
    return ctypes.cdll.LoadLibrary(path)

# A ctypes library to expose the extern-C FFI definitions.
# This is an implementation detail which will be called internally by the public API.

_UniFFILib = loadIndirect()
_UniFFILib.scanner_d0b2_scan_device.argtypes = (
    ctypes.POINTER(RustCallStatus),
)
_UniFFILib.scanner_d0b2_scan_device.restype = RustBuffer
_UniFFILib.scanner_d0b2_connect_device.argtypes = (
    RustBuffer,
    RustBuffer,
    RustBuffer,
    RustBuffer,
    ctypes.POINTER(RustCallStatus),
)
_UniFFILib.scanner_d0b2_connect_device.restype = RustBuffer
_UniFFILib.scanner_d0b2_disconnect_device.argtypes = (
    RustBuffer,
    ctypes.POINTER(RustCallStatus),
)
_UniFFILib.scanner_d0b2_disconnect_device.restype = RustBuffer
_UniFFILib.scanner_d0b2_get_device_basic_properties.argtypes = (
    RustBuffer,
    RustBuffer,
    ctypes.POINTER(RustCallStatus),
)
_UniFFILib.scanner_d0b2_get_device_basic_properties.restype = RustBuffer
_UniFFILib.scanner_d0b2_get_properties_info.argtypes = (
    RustBuffer,
    RustBuffer,
    ctypes.POINTER(RustCallStatus),
)
_UniFFILib.scanner_d0b2_get_properties_info.restype = RustBuffer
_UniFFILib.scanner_d0b2_edit_properties_info.argtypes = (
    RustBuffer,
    RustBuffer,
    RustBuffer,
    ctypes.POINTER(RustCallStatus),
)
_UniFFILib.scanner_d0b2_edit_properties_info.restype = RustBuffer
_UniFFILib.scanner_d0b2_get_barcode_properties.argtypes = (
    RustBuffer,
    ctypes.POINTER(RustCallStatus),
)
_UniFFILib.scanner_d0b2_get_barcode_properties.restype = RustBuffer
_UniFFILib.ffi_scanner_d0b2_rustbuffer_alloc.argtypes = (
    ctypes.c_int32,
    ctypes.POINTER(RustCallStatus),
)
_UniFFILib.ffi_scanner_d0b2_rustbuffer_alloc.restype = RustBuffer
_UniFFILib.ffi_scanner_d0b2_rustbuffer_from_bytes.argtypes = (
    ForeignBytes,
    ctypes.POINTER(RustCallStatus),
)
_UniFFILib.ffi_scanner_d0b2_rustbuffer_from_bytes.restype = RustBuffer
_UniFFILib.ffi_scanner_d0b2_rustbuffer_free.argtypes = (
    RustBuffer,
    ctypes.POINTER(RustCallStatus),
)
_UniFFILib.ffi_scanner_d0b2_rustbuffer_free.restype = None
_UniFFILib.ffi_scanner_d0b2_rustbuffer_reserve.argtypes = (
    RustBuffer,
    ctypes.c_int32,
    ctypes.POINTER(RustCallStatus),
)
_UniFFILib.ffi_scanner_d0b2_rustbuffer_reserve.restype = RustBuffer

# Public interface members begin here.


class FfiConverterString:
    @staticmethod
    def read(buf):
        size = buf.readI32()
        if size < 0:
            raise InternalError("Unexpected negative string length")
        utf8Bytes = buf.read(size)
        return utf8Bytes.decode("utf-8")

    @staticmethod
    def write(value, buf):
        utf8Bytes = value.encode("utf-8")
        buf.writeI32(len(utf8Bytes))
        buf.write(utf8Bytes)

    @staticmethod
    def lift(buf):
        with buf.consumeWithStream() as stream:
            return stream.read(stream.remaining()).decode("utf-8")

    @staticmethod
    def lower(value):
        with RustBuffer.allocWithBuilder() as builder:
            builder.write(value.encode("utf-8"))
            return builder.finalize()

def scan_device():
    return FfiConverterString.lift(rust_call(_UniFFILib.scanner_d0b2_scan_device,))



def connect_device(device_id,app_id,developer_id,app_key):
    device_id = device_id
    
    app_id = app_id
    
    developer_id = developer_id
    
    app_key = app_key
    
    return FfiConverterString.lift(rust_call(_UniFFILib.scanner_d0b2_connect_device,
        FfiConverterString.lower(device_id),
        FfiConverterString.lower(app_id),
        FfiConverterString.lower(developer_id),
        FfiConverterString.lower(app_key)))



def disconnect_device(device_id):
    device_id = device_id
    
    return FfiConverterString.lift(rust_call(_UniFFILib.scanner_d0b2_disconnect_device,
        FfiConverterString.lower(device_id)))



def get_device_basic_properties(device_id,property_key):
    device_id = device_id
    
    property_key = property_key
    
    return FfiConverterString.lift(rust_call(_UniFFILib.scanner_d0b2_get_device_basic_properties,
        FfiConverterString.lower(device_id),
        FfiConverterString.lower(property_key)))



def get_properties_info(device_id,property_key):
    device_id = device_id
    
    property_key = property_key
    
    return FfiConverterString.lift(rust_call(_UniFFILib.scanner_d0b2_get_properties_info,
        FfiConverterString.lower(device_id),
        FfiConverterString.lower(property_key)))



def edit_properties_info(device_id,property_key,data):
    device_id = device_id
    
    property_key = property_key
    
    data = data
    
    return FfiConverterString.lift(rust_call(_UniFFILib.scanner_d0b2_edit_properties_info,
        FfiConverterString.lower(device_id),
        FfiConverterString.lower(property_key),
        FfiConverterString.lower(data)))



def get_barcode_properties(device_id):
    device_id = device_id
    
    return FfiConverterString.lift(rust_call(_UniFFILib.scanner_d0b2_get_barcode_properties,
        FfiConverterString.lower(device_id)))



__all__ = [
    "InternalError",
    "scan_device",
    "connect_device",
    "disconnect_device",
    "get_device_basic_properties",
    "get_properties_info",
    "edit_properties_info",
    "get_barcode_properties",
]

if __name__ == '__main__':
    print(scan_device())
    print(connect_device("F7:7C:4A:1F:FB:3E","com.inateck.scanner","693be162686a","SrwG8UsCC6Fp7OSCDfckFHtfnNF8MRg9CmIvDgHXoFNFRsm3uiQviNtkyOfc//+m2ZpZ32uK3Z5g83optZwpZUFlnmX9DdyvYaaOqzIUJvruixZ3AfKmA/jYKxhbAhjvMLgoW+tHyPnARkJRAMMRULnayq4BLFXm47WGxVVQFXg="))
    print(get_properties_info("F7:7C:4A:1F:FB:3E","cache"))