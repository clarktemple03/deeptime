def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('hmm', parent_package, top_path)

    config.add_subpackage("init")

    config.add_extension('_hmm_bindings', sources=['_bindings/src/hmm_module.cpp'], language='c++')

    return config
