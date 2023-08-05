{% macro copy_into(destination, source, materialization_schema, cast_types) %}
COPY INTO {{ destination }}
FROM (
    SELECT
        {%- for column in materialization_schema.columns %}
            {%- if data_types.data_type_from_proto(column.feature_server_data_type) == data_types.ArrayType(data_types.StringType()) %}
                TO_ARRAY({{ column.name }},'string') AS {{ column.name }}
            {%- elif cast_types.get(data_types.data_type_from_proto(column.feature_server_data_type)) != None %}
                {{ column.name }}::{{ cast_types[data_types.data_type_from_proto(column.feature_server_data_type)] }} AS {{ column.name }}
            {%- else %}
                {{ column.name }}
            {%- endif %}
            {%- if not loop.last %}, {%- endif %}
        {%- endfor %}
    FROM ({{ source }})
)
header = true
detailed_output = true
file_format = (type=parquet)
{% endmacro %}
