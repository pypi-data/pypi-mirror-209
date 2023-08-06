import os
import streamlit.components.v1 as components

_RELEASE = True

componet_name = 'streamlit_seqviz'

if not _RELEASE:
  _component_func = components.declare_component(
    componet_name,
    url="http://localhost:5173", # vite dev server port
  )
else:
  parent_dir = os.path.dirname(os.path.abspath(__file__))
  build_dir = os.path.join(parent_dir, "frontend/dist")
  _component_func = components.declare_component(componet_name, path=build_dir)

def streamlit_seqviz(name, seq, annotations,style, highlights, enzymes, key=None):
  component_value = _component_func(
    name=name, seq=seq, annotations=annotations, style=style, highlights=highlights, enzymes=enzymes, 
    key=key, default=0
  )
  return component_value

if not _RELEASE:
  import streamlit as st
  st.subheader("Component Test")
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
