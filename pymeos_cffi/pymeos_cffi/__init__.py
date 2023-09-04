from .functions import *

from .errors import *

__all__ = [
    # Exceptions 
    'MeosException',
    'MeosInternalError',
    'MeosArgumentError',
    'MeosIoError',
    'MeosInternalTypeError',
    'MeosValueOutOfRangeError',
    'MeosDivisionByZeroError',
    'MeosMemoryAllocError',
    'MeosAggregationError',
    'MeosDirectoryError',
    'MeosFileError',
    'MeosInvalidArgError',
    'MeosInvalidArgTypeError',
    'MeosInvalidArgValueError',
    'MeosMfJsonInputError',
    'MeosMfJsonOutputError',
    'MeosTextInputError',
    'MeosTextOutputError',
    'MeosWkbInputError',
    'MeosWkbOutputError',
    'MeosGeoJsonInputError',
    'MeosGeoJsonOutputError',
    # Functions
    'py_error_handler',
    'create_pointer',
    'get_address',
    'datetime_to_timestamptz',
    'timestamptz_to_datetime',
    'timedelta_to_interval',
    'interval_to_timedelta',
    'geo_to_gserialized',
    'geometry_to_gserialized',
    'geography_to_gserialized',
    'gserialized_to_shapely_point',
    'gserialized_to_shapely_geometry',
    'intrange_to_intspan',
    'intspan_to_intrange',
    'floatrange_to_floatspan',
    'floatspan_to_floatrange',
    'as_tinstant',
    'as_tsequence',
    'as_tsequenceset',
    'lwpoint_make',
    'lwgeom_from_gserialized',
    'gserialized_from_lwgeom',
    'lwgeom_get_srid',
    'lwpoint_get_x',
    'lwpoint_get_y',
    'lwpoint_get_z',
    'lwpoint_get_m',
    'lwgeom_has_z',
    'lwgeom_has_m',
    'meos_initialize',
    'meos_finalize',
    'bool_in',
    'bool_out',
    'cstring2text',
    'pg_date_in',
    'pg_date_out',
    'pg_interval_cmp',
    'pg_interval_in',
    'pg_interval_make',
    'pg_interval_mul',
    'pg_interval_out',
    'pg_interval_pl',
    'pg_time_in',
    'pg_time_out',
    'pg_timestamp_in',
    'pg_timestamp_mi',
    'pg_timestamp_mi_interval',
    'pg_timestamp_out',
    'pg_timestamp_pl_interval',
    'pg_timestamptz_in',
    'pg_timestamptz_out',
    'text2cstring',
    'pg_timestamp_to_char',
    'pg_timestamptz_to_char',
    'pg_interval_to_char',
    'pg_to_timestamp',
    'pg_to_date',
    'geography_from_hexewkb',
    'geometry_from_hexewkb',
    'gserialized_as_ewkb',
    'gserialized_as_ewkt',
    'gserialized_as_geojson',
    'gserialized_as_hexewkb',
    'gserialized_as_text',
    'gserialized_from_ewkb',
    'gserialized_from_geojson',
    'gserialized_out',
    'geometry_from_text',
    'geography_from_text',
    'pgis_geography_in',
    'pgis_geometry_in',
    'pgis_gserialized_same',
    'bigintset_in',
    'bigintset_out',
    'bigintspan_in',
    'bigintspan_out',
    'bigintspanset_in',
    'bigintspanset_out',
    'floatset_in',
    'floatset_out',
    'floatspan_in',
    'floatspan_out',
    'floatspanset_in',
    'floatspanset_out',
    'geogset_in',
    'geoset_out',
    'geomset_in',
    'geoset_as_ewkt',
    'geoset_as_text',
    'intset_in',
    'intset_out',
    'intspan_in',
    'intspan_out',
    'intspanset_in',
    'intspanset_out',
    'period_in',
    'period_out',
    'periodset_in',
    'periodset_out',
    'set_as_hexwkb',
    'set_as_wkb',
    'set_from_hexwkb',
    'set_from_wkb',
    'set_out',
    'span_as_wkb',
    'span_as_hexwkb',
    'span_from_hexwkb',
    'span_from_wkb',
    'span_out',
    'spanset_as_wkb',
    'spanset_as_hexwkb',
    'spanset_from_hexwkb',
    'spanset_from_wkb',
    'spanset_out',
    'textset_in',
    'textset_out',
    'timestampset_in',
    'timestampset_out',
    'bigintset_make',
    'bigintspan_make',
    'floatset_make',
    'floatspan_make',
    'geoset_make',
    'intset_make',
    'intspan_make',
    'period_make',
    'set_copy',
    'span_copy',
    'spanset_copy',
    'spanset_make',
    'spanset_make_exp',
    'textset_make',
    'timestampset_make',
    'bigint_to_bigintset',
    'bigint_to_bigintspan',
    'bigint_to_bigintspanset',
    'float_to_floatset',
    'float_to_floatspan',
    'float_to_floatspanset',
    'geo_to_geoset',
    'int_to_intset',
    'int_to_intspan',
    'int_to_intspanset',
    'set_to_spanset',
    'span_to_spanset',
    'text_to_textset',
    'timestamp_to_period',
    'timestamp_to_periodset',
    'timestamp_to_tstzset',
    'bigintset_end_value',
    'bigintset_start_value',
    'bigintset_value_n',
    'bigintset_values',
    'bigintspan_lower',
    'bigintspan_upper',
    'bigintspanset_lower',
    'bigintspanset_upper',
    'floatset_end_value',
    'floatset_start_value',
    'floatset_value_n',
    'floatset_values',
    'floatspan_lower',
    'floatspan_upper',
    'floatspanset_lower',
    'floatspanset_upper',
    'geoset_end_value',
    'geoset_srid',
    'geoset_start_value',
    'geoset_value_n',
    'geoset_values',
    'intset_end_value',
    'intset_start_value',
    'intset_value_n',
    'intset_values',
    'intspan_lower',
    'intspan_upper',
    'intspanset_lower',
    'intspanset_upper',
    'period_duration',
    'period_lower',
    'period_upper',
    'periodset_duration',
    'periodset_end_timestamp',
    'periodset_lower',
    'periodset_num_timestamps',
    'periodset_start_timestamp',
    'periodset_timestamp_n',
    'periodset_timestamps',
    'periodset_upper',
    'set_hash',
    'set_hash_extended',
    'set_mem_size',
    'set_num_values',
    'set_span',
    'span_hash',
    'span_hash_extended',
    'span_lower_inc',
    'span_upper_inc',
    'span_width',
    'spanset_end_span',
    'spanset_hash',
    'spanset_hash_extended',
    'spanset_lower_inc',
    'spanset_mem_size',
    'spanset_num_spans',
    'spanset_span',
    'spanset_span_n',
    'spanset_spans',
    'spanset_start_span',
    'spanset_upper_inc',
    'spanset_width',
    'spatialset_stbox',
    'textset_end_value',
    'textset_start_value',
    'textset_value_n',
    'textset_values',
    'timestampset_end_timestamp',
    'timestampset_start_timestamp',
    'timestampset_timestamp_n',
    'timestampset_values',
    'floatset_round',
    'floatspan_round',
    'floatspanset_round',
    'geoset_round',
    'period_tprecision',
    'periodset_tprecision',
    'period_shift_tscale',
    'periodset_shift_tscale',
    'timestamp_tprecision',
    'timestampset_shift_tscale',
    'adjacent_bigintspan_bigint',
    'adjacent_bigintspanset_bigint',
    'adjacent_floatspan_float',
    'adjacent_floatspanset_float',
    'adjacent_intspan_int',
    'adjacent_intspanset_int',
    'adjacent_period_timestamp',
    'adjacent_periodset_timestamp',
    'adjacent_span_span',
    'adjacent_spanset_span',
    'adjacent_spanset_spanset',
    'contained_bigint_bigintset',
    'contained_bigint_bigintspan',
    'contained_bigint_bigintspanset',
    'contained_float_floatset',
    'contained_float_floatspan',
    'contained_float_floatspanset',
    'contained_int_intset',
    'contained_int_intspan',
    'contained_int_intspanset',
    'contained_set_set',
    'contained_span_span',
    'contained_span_spanset',
    'contained_spanset_span',
    'contained_spanset_spanset',
    'contained_text_textset',
    'contained_timestamp_period',
    'contained_timestamp_periodset',
    'contained_timestamp_timestampset',
    'contains_bigintset_bigint',
    'contains_bigintspan_bigint',
    'contains_bigintspanset_bigint',
    'contains_floatset_float',
    'contains_floatspan_float',
    'contains_floatspanset_float',
    'contains_intset_int',
    'contains_intspan_int',
    'contains_intspanset_int',
    'contains_period_timestamp',
    'contains_periodset_timestamp',
    'contains_set_set',
    'contains_span_span',
    'contains_span_spanset',
    'contains_spanset_span',
    'contains_spanset_spanset',
    'contains_textset_text',
    'contains_timestampset_timestamp',
    'overlaps_set_set',
    'overlaps_span_span',
    'overlaps_spanset_span',
    'overlaps_spanset_spanset',
    'after_timestamp_timestampset',
    'before_periodset_timestamp',
    'before_timestamp_timestampset',
    'left_float_floatspan',
    'left_floatspan_float',
    'left_int_intspan',
    'left_intspan_int',
    'left_set_set',
    'left_span_span',
    'left_span_spanset',
    'left_spanset_span',
    'left_spanset_spanset',
    'overafter_period_timestamp',
    'overafter_periodset_timestamp',
    'overafter_timestamp_period',
    'overafter_timestamp_periodset',
    'overafter_timestamp_timestampset',
    'overbefore_period_timestamp',
    'overbefore_periodset_timestamp',
    'overbefore_timestamp_period',
    'overbefore_timestamp_periodset',
    'overbefore_timestamp_timestampset',
    'overleft_float_floatspan',
    'overleft_floatspan_float',
    'overleft_int_intspan',
    'overleft_intspan_int',
    'overleft_set_set',
    'overleft_span_span',
    'overleft_span_spanset',
    'overleft_spanset_span',
    'overleft_spanset_spanset',
    'overright_float_floatspan',
    'overright_floatspan_float',
    'overright_int_intspan',
    'overright_intspan_int',
    'overright_set_set',
    'overright_span_span',
    'overright_span_spanset',
    'overright_spanset_span',
    'overright_spanset_spanset',
    'right_float_floatspan',
    'right_floatspan_float',
    'right_int_intspan',
    'right_intspan_int',
    'right_set_set',
    'right_span_span',
    'right_span_spanset',
    'right_spanset_span',
    'right_spanset_spanset',
    'intersection_bigintset_bigint',
    'intersection_bigintspan_bigint',
    'intersection_bigintspanset_bigint',
    'intersection_floatset_float',
    'intersection_floatspan_float',
    'intersection_floatspanset_float',
    'intersection_intset_int',
    'intersection_intspan_int',
    'intersection_intspanset_int',
    'intersection_period_timestamp',
    'intersection_periodset_timestamp',
    'intersection_set_set',
    'intersection_span_span',
    'intersection_spanset_span',
    'intersection_spanset_spanset',
    'intersection_textset_text',
    'intersection_timestampset_timestamp',
    'minus_bigint_bigintset',
    'minus_bigint_bigintspan',
    'minus_bigint_bigintspanset',
    'minus_bigintset_bigint',
    'minus_bigintspan_bigint',
    'minus_bigintspanset_bigint',
    'minus_float_floatset',
    'minus_float_floatspan',
    'minus_float_floatspanset',
    'minus_floatset_float',
    'minus_floatspan_float',
    'minus_floatspanset_float',
    'minus_int_intset',
    'minus_int_intspan',
    'minus_int_intspanset',
    'minus_intset_int',
    'minus_intspan_int',
    'minus_intspanset_int',
    'minus_period_timestamp',
    'minus_periodset_timestamp',
    'minus_set_set',
    'minus_span_span',
    'minus_span_spanset',
    'minus_spanset_span',
    'minus_spanset_spanset',
    'minus_text_textset',
    'minus_textset_text',
    'minus_timestamp_period',
    'minus_timestamp_periodset',
    'minus_timestampset_timestamp',
    'union_bigintset_bigint',
    'union_bigintspan_bigint',
    'union_bigintspanset_bigint',
    'union_floatset_float',
    'union_floatspan_float',
    'union_floatspanset_float',
    'union_intset_int',
    'union_intspan_int',
    'union_intspanset_int',
    'union_period_timestamp',
    'union_periodset_timestamp',
    'union_set_set',
    'union_span_span',
    'union_spanset_span',
    'union_spanset_spanset',
    'union_textset_text',
    'union_timestampset_timestamp',
    'distance_floatspan_float',
    'distance_intspan_int',
    'distance_set_set',
    'distance_period_timestamp',
    'distance_periodset_timestamp',
    'distance_span_span',
    'distance_spanset_span',
    'distance_spanset_spanset',
    'distance_timestampset_timestamp',
    'bigint_extent_transfn',
    'bigint_union_transfn',
    'float_extent_transfn',
    'float_union_transfn',
    'int_extent_transfn',
    'int_union_transfn',
    'period_tcount_transfn',
    'periodset_tcount_transfn',
    'set_extent_transfn',
    'set_union_finalfn',
    'set_union_transfn',
    'span_extent_transfn',
    'span_union_transfn',
    'spanset_extent_transfn',
    'spanset_union_finalfn',
    'spanset_union_transfn',
    'text_union_transfn',
    'timestamp_extent_transfn',
    'timestamp_tcount_transfn',
    'timestamp_union_transfn',
    'timestampset_tcount_transfn',
    'set_cmp',
    'set_eq',
    'set_ge',
    'set_gt',
    'set_le',
    'set_lt',
    'set_ne',
    'span_cmp',
    'span_eq',
    'span_ge',
    'span_gt',
    'span_le',
    'span_lt',
    'span_ne',
    'spanset_cmp',
    'spanset_eq',
    'spanset_ge',
    'spanset_gt',
    'spanset_le',
    'spanset_lt',
    'spanset_ne',
    'tbox_in',
    'tbox_out',
    'tbox_from_wkb',
    'tbox_from_hexwkb',
    'stbox_from_wkb',
    'stbox_from_hexwkb',
    'tbox_as_wkb',
    'tbox_as_hexwkb',
    'stbox_as_wkb',
    'stbox_as_hexwkb',
    'stbox_in',
    'stbox_out',
    'stbox_make',
    'stbox_copy',
    'tbox_make',
    'tbox_copy',
    'int_to_tbox',
    'float_to_tbox',
    'timestamp_to_tbox',
    'timestampset_to_tbox',
    'period_to_tbox',
    'periodset_to_tbox',
    'int_timestamp_to_tbox',
    'float_period_to_tbox',
    'float_timestamp_to_tbox',
    'geo_period_to_stbox',
    'geo_timestamp_to_stbox',
    'geo_to_stbox',
    'int_period_to_tbox',
    'numspan_to_tbox',
    'span_timestamp_to_tbox',
    'span_period_to_tbox',
    'tbox_to_floatspan',
    'tbox_to_period',
    'stbox_to_period',
    'tnumber_to_tbox',
    'stbox_to_geo',
    'tpoint_to_stbox',
    'timestamp_to_stbox',
    'timestampset_to_stbox',
    'period_to_stbox',
    'periodset_to_stbox',
    'tbox_hasx',
    'tbox_hast',
    'tbox_xmin',
    'tbox_xmin_inc',
    'tbox_xmax',
    'tbox_xmax_inc',
    'tbox_tmin',
    'tbox_tmin_inc',
    'tbox_tmax',
    'tbox_tmax_inc',
    'stbox_hasx',
    'stbox_hasz',
    'stbox_hast',
    'stbox_isgeodetic',
    'stbox_xmin',
    'stbox_xmax',
    'stbox_ymin',
    'stbox_ymax',
    'stbox_zmin',
    'stbox_zmax',
    'stbox_tmin',
    'stbox_tmin_inc',
    'stbox_tmax',
    'stbox_tmax_inc',
    'stbox_srid',
    'stbox_expand_space',
    'stbox_expand_time',
    'stbox_get_space',
    'stbox_round',
    'stbox_set_srid',
    'tbox_expand_value',
    'tbox_expand_time',
    'tbox_round',
    'contains_tbox_tbox',
    'contained_tbox_tbox',
    'overlaps_tbox_tbox',
    'same_tbox_tbox',
    'adjacent_tbox_tbox',
    'contains_stbox_stbox',
    'contained_stbox_stbox',
    'overlaps_stbox_stbox',
    'same_stbox_stbox',
    'adjacent_stbox_stbox',
    'left_tbox_tbox',
    'overleft_tbox_tbox',
    'right_tbox_tbox',
    'overright_tbox_tbox',
    'before_tbox_tbox',
    'overbefore_tbox_tbox',
    'after_tbox_tbox',
    'overafter_tbox_tbox',
    'left_stbox_stbox',
    'overleft_stbox_stbox',
    'right_stbox_stbox',
    'overright_stbox_stbox',
    'below_stbox_stbox',
    'overbelow_stbox_stbox',
    'above_stbox_stbox',
    'overabove_stbox_stbox',
    'front_stbox_stbox',
    'overfront_stbox_stbox',
    'back_stbox_stbox',
    'overback_stbox_stbox',
    'before_stbox_stbox',
    'overbefore_stbox_stbox',
    'after_stbox_stbox',
    'overafter_stbox_stbox',
    'union_tbox_tbox',
    'inter_tbox_tbox',
    'intersection_tbox_tbox',
    'union_stbox_stbox',
    'inter_stbox_stbox',
    'intersection_stbox_stbox',
    'stbox_quad_split',
    'tbox_eq',
    'tbox_ne',
    'tbox_cmp',
    'tbox_lt',
    'tbox_le',
    'tbox_ge',
    'tbox_gt',
    'stbox_eq',
    'stbox_ne',
    'stbox_cmp',
    'stbox_lt',
    'stbox_le',
    'stbox_ge',
    'stbox_gt',
    'tbool_in',
    'tbool_out',
    'temporal_as_hexwkb',
    'temporal_as_mfjson',
    'temporal_as_wkb',
    'temporal_from_hexwkb',
    'temporal_from_mfjson',
    'temporal_from_wkb',
    'tfloat_in',
    'tfloat_out',
    'tgeogpoint_in',
    'tgeompoint_in',
    'tint_in',
    'tint_out',
    'tpoint_as_ewkt',
    'tpoint_as_text',
    'tpoint_out',
    'ttext_in',
    'ttext_out',
    'tbool_from_base_temp',
    'tboolinst_make',
    'tboolseq_from_base_period',
    'tboolseq_from_base_timestampset',
    'tboolseqset_from_base_periodset',
    'temporal_copy',
    'tfloat_from_base_temp',
    'tfloatinst_make',
    'tfloatseq_from_base_period',
    'tfloatseq_from_base_timestampset',
    'tfloatseqset_from_base_periodset',
    'tint_from_base_temp',
    'tintinst_make',
    'tintseq_from_base_period',
    'tintseq_from_base_timestampset',
    'tintseqset_from_base_periodset',
    'tpoint_from_base_temp',
    'tpointinst_make',
    'tpointseq_from_base_period',
    'tpointseq_from_base_timestampset',
    'tpointseqset_from_base_periodset',
    'tsequence_make',
    'tsequence_make_exp',
    'tsequenceset_make',
    'tsequenceset_make_exp',
    'tsequenceset_make_gaps',
    'ttext_from_base_temp',
    'ttextinst_make',
    'ttextseq_from_base_period',
    'ttextseq_from_base_timestampset',
    'ttextseqset_from_base_periodset',
    'temporal_to_period',
    'tfloat_to_tint',
    'tint_to_tfloat',
    'tnumber_to_span',
    'tbool_end_value',
    'tbool_start_value',
    'tbool_values',
    'temporal_duration',
    'temporal_end_instant',
    'temporal_end_sequence',
    'temporal_end_timestamp',
    'temporal_hash',
    'temporal_instant_n',
    'temporal_instants',
    'temporal_interp',
    'temporal_max_instant',
    'temporal_min_instant',
    'temporal_num_instants',
    'temporal_num_sequences',
    'temporal_num_timestamps',
    'temporal_segments',
    'temporal_sequence_n',
    'temporal_sequences',
    'temporal_start_instant',
    'temporal_start_sequence',
    'temporal_start_timestamp',
    'temporal_stops',
    'temporal_subtype',
    'temporal_time',
    'temporal_timestamp_n',
    'temporal_timestamps',
    'tfloat_end_value',
    'tfloat_max_value',
    'tfloat_min_value',
    'tfloat_start_value',
    'tfloat_values',
    'tint_end_value',
    'tint_max_value',
    'tint_min_value',
    'tint_start_value',
    'tint_values',
    'tnumber_valuespans',
    'tpoint_end_value',
    'tpoint_start_value',
    'tpoint_values',
    'ttext_end_value',
    'ttext_max_value',
    'ttext_min_value',
    'ttext_start_value',
    'ttext_values',
    'temporal_set_interp',
    'temporal_shift',
    'temporal_shift_tscale',
    'temporal_to_tinstant',
    'temporal_to_tsequence',
    'temporal_to_tsequenceset',
    'temporal_tprecision',
    'temporal_tsample',
    'temporal_tscale',
    'tbool_at_value',
    'tbool_minus_value',
    'tbool_value_at_timestamp',
    'temporal_at_max',
    'temporal_at_min',
    'temporal_at_period',
    'temporal_at_periodset',
    'temporal_at_timestamp',
    'temporal_at_timestampset',
    'temporal_at_values',
    'temporal_minus_max',
    'temporal_minus_min',
    'temporal_minus_period',
    'temporal_minus_periodset',
    'temporal_minus_timestamp',
    'temporal_minus_timestampset',
    'temporal_minus_values',
    'tfloat_at_value',
    'tfloat_minus_value',
    'tfloat_value_at_timestamp',
    'tint_at_value',
    'tint_minus_value',
    'tint_value_at_timestamp',
    'tnumber_at_span',
    'tnumber_at_spanset',
    'tnumber_at_tbox',
    'tnumber_minus_span',
    'tnumber_minus_spanset',
    'tnumber_minus_tbox',
    'tpoint_at_geom_time',
    'tpoint_at_stbox',
    'tpoint_at_value',
    'tpoint_minus_geom_time',
    'tpoint_minus_stbox',
    'tpoint_minus_value',
    'tpoint_value_at_timestamp',
    'ttext_at_value',
    'ttext_minus_value',
    'ttext_value_at_timestamp',
    'temporal_append_tinstant',
    'temporal_append_tsequence',
    'temporal_delete_period',
    'temporal_delete_periodset',
    'temporal_delete_timestamp',
    'temporal_delete_timestampset',
    'temporal_insert',
    'temporal_merge',
    'temporal_merge_array',
    'temporal_update',
    'tand_bool_tbool',
    'tand_tbool_bool',
    'tand_tbool_tbool',
    'tbool_when_true',
    'tnot_tbool',
    'tor_bool_tbool',
    'tor_tbool_bool',
    'tor_tbool_tbool',
    'add_float_tfloat',
    'add_int_tint',
    'add_tfloat_float',
    'add_tint_int',
    'add_tnumber_tnumber',
    'div_float_tfloat',
    'div_int_tint',
    'div_tfloat_float',
    'div_tint_int',
    'div_tnumber_tnumber',
    'float_degrees',
    'mult_float_tfloat',
    'mult_int_tint',
    'mult_tfloat_float',
    'mult_tint_int',
    'mult_tnumber_tnumber',
    'sub_float_tfloat',
    'sub_int_tint',
    'sub_tfloat_float',
    'sub_tint_int',
    'sub_tnumber_tnumber',
    'tfloat_round',
    'tfloat_degrees',
    'tfloat_derivative',
    'tfloat_radians',
    'tnumber_abs',
    'tnumber_angular_difference',
    'tnumber_delta_value',
    'textcat_text_ttext',
    'textcat_ttext_text',
    'textcat_ttext_ttext',
    'ttext_upper',
    'ttext_lower',
    'distance_tfloat_float',
    'distance_tint_int',
    'distance_tnumber_tnumber',
    'distance_tpoint_geo',
    'distance_tpoint_tpoint',
    'nad_stbox_geo',
    'nad_stbox_stbox',
    'nad_tbox_tbox',
    'nad_tfloat_float',
    'nad_tfloat_tfloat',
    'nad_tint_int',
    'nad_tint_tint',
    'nad_tnumber_tbox',
    'nad_tpoint_geo',
    'nad_tpoint_stbox',
    'nad_tpoint_tpoint',
    'nai_tpoint_geo',
    'nai_tpoint_tpoint',
    'shortestline_tpoint_geo',
    'shortestline_tpoint_tpoint',
    'tbool_always_eq',
    'tbool_ever_eq',
    'tfloat_always_eq',
    'tfloat_always_le',
    'tfloat_always_lt',
    'tfloat_ever_eq',
    'tfloat_ever_le',
    'tfloat_ever_lt',
    'tint_always_eq',
    'tint_always_le',
    'tint_always_lt',
    'tint_ever_eq',
    'tint_ever_le',
    'tint_ever_lt',
    'tpoint_always_eq',
    'tpoint_ever_eq',
    'ttext_always_eq',
    'ttext_always_le',
    'ttext_always_lt',
    'ttext_ever_eq',
    'ttext_ever_le',
    'ttext_ever_lt',
    'temporal_cmp',
    'temporal_eq',
    'temporal_ge',
    'temporal_gt',
    'temporal_le',
    'temporal_lt',
    'temporal_ne',
    'teq_bool_tbool',
    'teq_float_tfloat',
    'teq_int_tint',
    'teq_point_tpoint',
    'teq_tbool_bool',
    'teq_temporal_temporal',
    'teq_text_ttext',
    'teq_tfloat_float',
    'teq_tpoint_point',
    'teq_tint_int',
    'teq_ttext_text',
    'tge_float_tfloat',
    'tge_int_tint',
    'tge_temporal_temporal',
    'tge_text_ttext',
    'tge_tfloat_float',
    'tge_tint_int',
    'tge_ttext_text',
    'tgt_float_tfloat',
    'tgt_int_tint',
    'tgt_temporal_temporal',
    'tgt_text_ttext',
    'tgt_tfloat_float',
    'tgt_tint_int',
    'tgt_ttext_text',
    'tle_float_tfloat',
    'tle_int_tint',
    'tle_temporal_temporal',
    'tle_text_ttext',
    'tle_tfloat_float',
    'tle_tint_int',
    'tle_ttext_text',
    'tlt_float_tfloat',
    'tlt_int_tint',
    'tlt_temporal_temporal',
    'tlt_text_ttext',
    'tlt_tfloat_float',
    'tlt_tint_int',
    'tlt_ttext_text',
    'tne_bool_tbool',
    'tne_float_tfloat',
    'tne_int_tint',
    'tne_point_tpoint',
    'tne_tbool_bool',
    'tne_temporal_temporal',
    'tne_text_ttext',
    'tne_tfloat_float',
    'tne_tpoint_point',
    'tne_tint_int',
    'tne_ttext_text',
    'bearing_point_point',
    'bearing_tpoint_point',
    'bearing_tpoint_tpoint',
    'tpoint_angular_difference',
    'tpoint_azimuth',
    'tpoint_convex_hull',
    'tpoint_cumulative_length',
    'tpoint_direction',
    'tpoint_get_coord',
    'tpoint_is_simple',
    'tpoint_length',
    'tpoint_speed',
    'tpoint_srid',
    'tpoint_stboxes',
    'tpoint_trajectory',
    'geo_expand_space',
    'tgeompoint_tgeogpoint',
    'tpoint_expand_space',
    'tpoint_round',
    'tpoint_make_simple',
    'tpoint_set_srid',
    'econtains_geo_tpoint',
    'edisjoint_tpoint_geo',
    'edisjoint_tpoint_tpoint',
    'edwithin_tpoint_geo',
    'edwithin_tpoint_tpoint',
    'eintersects_tpoint_geo',
    'eintersects_tpoint_tpoint',
    'etouches_tpoint_geo',
    'tcontains_geo_tpoint',
    'tdisjoint_tpoint_geo',
    'tdwithin_tpoint_geo',
    'tdwithin_tpoint_tpoint',
    'tintersects_tpoint_geo',
    'ttouches_tpoint_geo',
    'tbool_tand_transfn',
    'tbool_tor_transfn',
    'temporal_extent_transfn',
    'temporal_tagg_finalfn',
    'temporal_tcount_transfn',
    'tfloat_tmax_transfn',
    'tfloat_tmin_transfn',
    'tfloat_tsum_transfn',
    'tint_tmax_transfn',
    'tint_tmin_transfn',
    'tint_tsum_transfn',
    'tnumber_extent_transfn',
    'tnumber_integral',
    'tnumber_tavg_finalfn',
    'tnumber_tavg_transfn',
    'tnumber_twavg',
    'tpoint_extent_transfn',
    'tpoint_tcentroid_finalfn',
    'tpoint_tcentroid_transfn',
    'tpoint_twcentroid',
    'ttext_tmax_transfn',
    'ttext_tmin_transfn',
    'float_bucket',
    'floatspan_bucket_list',
    'int_bucket',
    'intspan_bucket_list',
    'period_bucket_list',
    'stbox_tile_list',
    'tbox_tile_list',
    'temporal_time_split',
    'tfloat_value_split',
    'tfloat_value_time_split',
    'timestamptz_bucket',
    'tint_value_split',
    'tint_value_time_split',
    'temporal_dyntimewarp_distance',
    'temporal_dyntimewarp_path',
    'temporal_frechet_distance',
    'temporal_frechet_path',
    'temporal_hausdorff_distance',
    'geo_to_tpoint',
    'temporal_simplify_min_dist',
    'temporal_simplify_min_tdelta',
    'temporal_simplify_dp',
    'temporal_simplify_max_dist',
    'tpoint_AsMVTGeom',
    'tpoint_to_geo_meas',
]
