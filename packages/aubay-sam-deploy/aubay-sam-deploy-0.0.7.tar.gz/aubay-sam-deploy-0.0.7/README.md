# aubay-sam-deploy
Deploy &amp; Documentation tool for Aubay SAM specifications

## SAM_DOC_GEN
> Sam Documentation Generator

This module allows the conversion of a file in YAML format to an HTML file.

The generated HTML document presents the OpenAPI style, by default, describing each YAML grouping as an OpenAPI endpoint grouping (sections).

The connectors approach assumes the existence of the 'specifications' directory, where each of the specifications will be distributed.


Script Example:

`generate-active --source isylight/calle`
