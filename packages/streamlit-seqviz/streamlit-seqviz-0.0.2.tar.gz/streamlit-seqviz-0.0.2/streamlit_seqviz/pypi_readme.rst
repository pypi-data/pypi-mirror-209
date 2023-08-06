|huggingface badge|

.. |huggingface badge| image:: https://huggingface.co/datasets/huggingface/badges/raw/refs%2Fpr%2F11/open-in-hf-spaces-md-dark.svg
    :target: https://huggingface.co/spaces/z-uo/DNASequenceVisualization


Streamlit seqviz
=============================

This library is a streamlit app for chemical or medical use that show DNA sequences effectively based on `seqviz <https://github.com/Lattice-Automation/seqviz>`_ js library.

.. image:: https://gitlab.com/nicolalandro/streamlit-seqviz/-/blob/main/imgs/white_screen.png
  :alt: Streamlit app example

.. code-block:: python

    from streamlit_seqviz import streamlit_seqviz

    streamlit_seqviz(
        name = "J23100",
        seq = "TTGACGGCTAGCTCAGTCCTAGGTACAGTGCTAGC",
        annotations = [{ "name": "promoter", "start": 0, "end": 30, "direction": 1 }],
        style =  { "height": "100vh", "width": "100vw" },
        highlights = [{ "start": 0, "end": 10 }],
        enzymes = [
            "EcoRI",
            "PstI",
            {
                "name": "Cas9",
                "rseq": "NGG", # recognition sequence
                "fcut": 0, # cut index on FWD strand, relative to start of rseq
                "rcut": 1, # cut index on REV strand, relative to start of rseq
                "color": "#D7E5F0", # color to highlight recognition site with
                "range": {
                    "start": 4,
                    "end": 8,
                },
            },
        ],
    )


