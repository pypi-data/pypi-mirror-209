#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "master_board_sdk::master_board_sdk" for configuration "Release"
set_property(TARGET master_board_sdk::master_board_sdk APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(master_board_sdk::master_board_sdk PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libmaster_board_sdk.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libmaster_board_sdk.dylib"
  )

list(APPEND _cmake_import_check_targets master_board_sdk::master_board_sdk )
list(APPEND _cmake_import_check_files_for_master_board_sdk::master_board_sdk "${_IMPORT_PREFIX}/lib/libmaster_board_sdk.dylib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
