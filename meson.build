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

symbol_prefix = ''
if host_machine.system() == 'darwin'
  symbol_prefix = '_'
endif

lvp_link_args = []
foreach sym : lvp_symbols
  lvp_link_args += '-Wl,-u,' + symbol_prefix + sym
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
  nak_link_args += '-Wl,-u,' + symbol_prefix + sym
endforeach

ir3_symbols = [
  'ir3_compile_shader_nir',
  'ir3_get_compiler_options',
  'ir3_nir_lower_io_vars_to_temporaries',
  'ir3_nir_post_finalize',
  'ir3_shader_assemble',
  'ir3_isa_disasm',
]

ir3_link_args = []
foreach sym : ir3_symbols
  ir3_link_args += '-Wl,-u,' + symbol_prefix + sym
endforeach

shared_library('tinymesa', link_whole : [ _libnir ], link_args : nak_link_args+ir3_link_args, link_with : [ libfreedreno_ir3 ], dependencies : [ idep_nak ])
shared_library('tinymesa_cpu', link_whole : [ _libnir ], link_args : lvp_link_args+nak_link_args, link_with : [ libfreedreno_ir3, libgallium ], dependencies : [ idep_nak ])

