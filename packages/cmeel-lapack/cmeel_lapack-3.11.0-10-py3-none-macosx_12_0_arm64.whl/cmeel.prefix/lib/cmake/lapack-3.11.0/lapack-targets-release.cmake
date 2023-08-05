#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "blas" for configuration "Release"
set_property(TARGET blas APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(blas PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libblas.3.11.0.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libblas.3.dylib"
  )

list(APPEND _cmake_import_check_targets blas )
list(APPEND _cmake_import_check_files_for_blas "${_IMPORT_PREFIX}/lib/libblas.3.11.0.dylib" )

# Import target "lapack" for configuration "Release"
set_property(TARGET lapack APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(lapack PROPERTIES
  IMPORTED_LINK_DEPENDENT_LIBRARIES_RELEASE "blas"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/liblapack.3.11.0.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/liblapack.3.dylib"
  )

list(APPEND _cmake_import_check_targets lapack )
list(APPEND _cmake_import_check_files_for_lapack "${_IMPORT_PREFIX}/lib/liblapack.3.11.0.dylib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
