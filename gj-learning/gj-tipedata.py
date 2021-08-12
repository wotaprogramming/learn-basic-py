# Tipe data

# tipe data integer
data_int = 4
print("data = ", data_int)
print("bertipe : ", type(data_int))

# tipe data float
data_float = 1.5
print("data = ", data_float)
print("bertipe : ", type(data_float))

# tipe data string
data_str = "Namikaze"
print("data = ", data_str)
print("bertipe : ", type(data_str))

# tipe data bool
data_bool = True
print("data = ", data_bool)
print("bertipe : ", type(data_bool))

## Tipe data Khusus

# tipe data kompleks
data_complex = complex(3,4)
print("data = ", data_complex)
print("bertipe : ", type(data_complex))

# tipe data dari bahasa c
from ctypes import c_double

# tipe data c double
data_c_double = c_double(3.678)
print("data = ", data_c_double)
print("bertipe : ", type(data_c_double))
