pybind11_add_module(_tram_bindings ../_bindings/src/tram_module.cpp)
target_link_libraries(_tram_bindings PUBLIC deeptime::deeptime)
if(OpenMP_FOUND)
    target_link_libraries(_tram_bindings PUBLIC OpenMP::OpenMP_CXX)
endif()
