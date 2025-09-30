lvp_symbols = [
  'gallivm_create',
  'gallivm_destroy',
  'gallivm_verify_function',
  'gallivm_compile_module',
  'lp_build_jit_resources_type',
  'lp_build_struct_get_ptr2',
  'lp_build_mask_begin',
  'lp_build_one',
  'lp_build_mask_end',
  'lp_build_nir_soa',
]

lvp_link_args = []
foreach sym : lvp_symbols
  lvp_link_args += '-Wl,-u,' + sym
endforeach

nak_symbols = [
  'nak_compiler_create',
  'nak_compiler_destroy',
  'nak_nir_options',
  'nak_preprocess_nir',
  'nak_compile_shader',
  'blob_reader_init',
  'nir_deserialize',
  'glsl_type_singleton_init_or_ref',
  'glsl_type_singleton_decref',
]

nak_link_args = []
foreach sym : nak_symbols
  nak_link_args += '-Wl,-u,' + sym
endforeach

shared_library('tinymesa', link_whole : [ _libnir ], link_args : nak_link_args, dependencies : [ idep_nak ])
shared_library('tinymesa_cpu', link_whole : [ _libnir ], link_args : lvp_link_args+nak_link_args, link_with : [ libgallium ], dependencies : [ idep_nak ])

