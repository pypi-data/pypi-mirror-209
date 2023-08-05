import base64

import streamlit as st
from IPython.display import display

from .. import loaders, viewer_backends
from ..loaders.image import SVGWrapper
from .viewer import Viewer


class Image(Viewer):
    """Viewer for images"""

    def __init__(self, data=None):
        self.compatible_data_types = [loaders.Image]
        #: Image to display
        self.image = None
        super().__init__(data)

    def add(self, data_container):
        """Replace the viewer's image"""
        self.check_data_compatibility(data_container)
        self.image = data_container.image

    def svg_format(self, svg):
        b64 = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
        html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
        st.write(html, unsafe_allow_html=True)

    def show(self):
        if viewer_backends.current_backend == "jupyter notebook":
            display(self.image)

        elif viewer_backends.current_backend == "streamlit":
            with st.container():
                if isinstance(self.image, SVGWrapper):
                    self.svg_format(self.image.src)
                else:
                    st.image(self.image)
        else:  # python
            self.image.show()
