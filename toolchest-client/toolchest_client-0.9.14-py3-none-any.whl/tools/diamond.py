"""
toolchest_client.tools.Diamond
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the Diamond implementation of the Tool class.
"""
from toolchest_client.files import OutputType
from . import Tool


class DiamondBlastp(Tool):
    """
    The DIAMOND BLASTP implementation of the Tool class.
    """
    def __init__(self, inputs, database_name, database_version, output_path, output_primary_name, tool_args, **kwargs):
        super().__init__(
            tool_name="diamond_blastp",
            tool_version="2.0.14",
            tool_args=tool_args,
            output_primary_name=output_primary_name,
            inputs=inputs,
            database_name=database_name,
            database_version=database_version,
            parallel_enabled=False,
            output_type=OutputType.GZ_TAR,
            output_path=output_path,
            expected_output_file_names=[output_primary_name, "diamond.log"],
            **kwargs,
        )


class DiamondBlastx(Tool):
    """
    The DIAMOND BLASTX implementation of the Tool class.
    """
    def __init__(self, inputs,  database_name, database_version, output_path, output_primary_name, tool_args, **kwargs):
        super().__init__(
            tool_name="diamond_blastx",
            tool_version="2.0.13",
            tool_args=tool_args,
            output_primary_name=output_primary_name,
            inputs=inputs,
            database_name=database_name,
            database_version=database_version,
            parallel_enabled=False,
            output_type=OutputType.GZ_TAR,
            output_path=output_path,
            expected_output_file_names=[output_primary_name, "diamond.log"],
            **kwargs,
        )
