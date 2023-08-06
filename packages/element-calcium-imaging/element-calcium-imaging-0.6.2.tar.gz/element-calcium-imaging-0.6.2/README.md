# DataJoint Element - Functional Calcium Imaging

DataJoint Element for functional calcium imaging with 
[ScanImage](https://docs.scanimage.org/), 
[Scanbox](https://scanbox.org/),
[Nikon NIS-Elements](https://www.microscope.healthcare.nikon.com/products/software/nis-elements), 
and `Bruker Prairie View` acquisition software; and 
[Suite2p](https://github.com/MouseLand/suite2p), 
[CaImAn](https://github.com/flatironinstitute/CaImAn), and
[EXTRACT](https://github.com/schnitzer-lab/EXTRACT-public) analysis 
software. DataJoint Elements collectively standardize and automate
data collection and analysis for neuroscience experiments. Each Element is a modular
pipeline for data storage and processing with corresponding database tables that can be
combined with other Elements to assemble a fully functional pipeline.

## Experiment Flowchart

![flowchart](https://raw.githubusercontent.com/datajoint/element-calcium-imaging/main/images/flowchart.svg)

## Data Pipeline Diagram

![pipeline](https://raw.githubusercontent.com/datajoint/element-calcium-imaging/main/images/pipeline_imaging.svg)

+ We have designed three variations of the pipeline to handle different use cases. Displayed above is the default `imaging` schema.  Details on all of the `imaging` schemas can be found in the [Data Pipeline](https://datajoint.com/docs/elements/element-calcium-imaging/latest/pipeline/) documentation page.

## Getting Started

+ Install from PyPI

     ```bash
     pip install element-calcium-imaging
     ```

+ [Interactive tutorial on GitHub Codespaces](https://github.com/datajoint/workflow-calcium-imaging#interactive-tutorial)

+ [Documentation](https://datajoint.com/docs/elements/element-calcium-imaging)

## Support

+ If you need help getting started or run into any errors, please contact our team by email at support@datajoint.com.
