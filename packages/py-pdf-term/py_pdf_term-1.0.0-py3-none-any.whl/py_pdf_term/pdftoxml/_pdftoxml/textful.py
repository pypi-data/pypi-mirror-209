from dataclasses import dataclass
from typing import Any, BinaryIO, Optional, Sequence, Tuple, Union

from pdfminer.converter import (
    Matrix,
    PathSegment,
    PDFConverter,
    PDFGraphicState,
    PDFStream,
    Rect,
)
from pdfminer.layout import (
    LAParams,
    LTAnno,
    LTChar,
    LTPage,
    LTText,
    LTTextBox,
    LTTextLine,
)
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.utils import bbox2str, enc

from .utils import clean_content_text

NColor = Union[float, Tuple[float, float, float], Tuple[float, float, float, float]]


@dataclass
class TextboxState:
    within_section: bool
    size: float
    ncolor: Optional[NColor]
    bbox: str
    text: str


class TextfulXMLConverter(PDFConverter[BinaryIO]):
    """A PDFConverter subclass that outputs textful XML format.

    Args
    ----
        rsrcmgr:
            A PDFResourceManager object from pdfminer.
        outfp:
            A file-like object to output XML.
        codec:
            A codec name to encode XML.
        pageno:
            A page number to start.
        laparams:
            A LAParams object from pdfminer.
        nfc_norm:
            If True, normalize text to NFC, otherwise keep original.
        include_pattern:
            A regular expression pattern of text to include in the output.
        exclude_pattern:
            A regular expression pattern of text to exclude from the output (overrides
            include_pattern).
    """

    def __init__(
        self,
        rsrcmgr: PDFResourceManager,
        outfp: BinaryIO,
        codec: str = "utf-8",
        pageno: int = 1,
        laparams: Optional[LAParams] = None,
        nfc_norm: bool = True,
        include_pattern: Optional[str] = None,
        exclude_pattern: Optional[str] = None,
    ) -> None:
        super().__init__(rsrcmgr, outfp, codec, pageno, laparams)

        def _clean_content_text(text: str) -> str:
            return clean_content_text(text, nfc_norm, include_pattern, exclude_pattern)

        self._clean_content_text = _clean_content_text

    def write_header(self) -> None:
        self._write('<?xml version="1.0" encoding="%s" ?>\n' % self.codec)
        self._write("<pages>\n")

    def receive_layout(self, ltpage: LTPage) -> None:
        self._render(ltpage)

    def write_footer(self) -> None:
        self._write("</pages>\n")

    # override to ignore LTFigure
    def begin_figure(self, name: str, bbox: Rect, matrix: Matrix) -> None:
        pass

    # override to ignore LTFigure
    def end_figure(self, _: str) -> None:
        pass

    # override to ignore LTImage
    def render_image(self, name: str, stream: PDFStream) -> None:
        pass

    # override to ignore LTLine, LTRect and LTCurve
    def paint_path(
        self,
        gstate: PDFGraphicState,
        stroke: bool,
        fill: bool,
        evenodd: bool,
        path: Sequence[PathSegment],
    ) -> None:
        pass

    def _render(self, item: Any) -> None:
        if isinstance(item, LTPage):
            self._render_page(item)
        elif isinstance(item, LTTextBox):
            self._render_textbox(item)
        elif isinstance(item, LTText):
            self._render_text(item)

    def _render_page(self, ltpage: LTPage) -> None:
        self._write('<page id="%s">\n' % ltpage.pageid)
        for child in ltpage:
            self._render(child)
        self._write("</page>\n")

    def _render_textbox(self, lttextbox: LTTextBox) -> None:
        state = TextboxState(False, 0.0, None, "", "")

        def render_textbox_child(child: Any) -> None:
            if isinstance(child, LTTextLine):
                for grandchild in child:
                    render_textbox_child(grandchild)
            elif isinstance(child, LTChar):
                if not state.within_section:
                    enter_text_section(child)
                    state.text += child.get_text()
                elif text_section_continues(child):
                    state.text += child.get_text()
                else:
                    exit_text_section()
                    enter_text_section(child)
                    state.text += child.get_text()
            elif isinstance(child, LTAnno):
                if not state.within_section:
                    pass
                elif text_section_continues(child):
                    state.text += child.get_text()
                else:
                    exit_text_section()

        def enter_text_section(item: LTChar) -> None:
            state.within_section = True
            state.size = item.size
            state.ncolor = item.graphicstate.ncolor
            state.bbox = bbox2str(item.bbox)
            state.text = ""

        def text_section_continues(item: Union[LTChar, LTAnno]) -> bool:
            if isinstance(item, LTAnno):
                return True
            return (
                state.ncolor == item.graphicstate.ncolor
                and abs(state.size - item.size) < 0.1
            )

        def exit_text_section() -> None:
            if not state.within_section:
                return

            text = self._clean_content_text(state.text)
            if text:
                self._write(
                    '<text size="%.3f" ncolor="%s" bbox="%s">'
                    % (state.size, state.ncolor, state.bbox)
                )
                self._write(enc(text))
                self._write("</text>\n")

            state.within_section = False
            state.size = 0.0
            state.ncolor = None
            state.bbox = ""
            state.text = ""

        for child in lttextbox:
            render_textbox_child(child)

        exit_text_section()

    def _render_text(self, lttext: LTText) -> None:
        text = self._clean_content_text(lttext.get_text())
        if text:
            self._write("<text>")
            self._write(enc(text))
            self._write("</text>\n")

    def _write(self, text: str) -> None:
        text_bytes = text.encode(self.codec)
        self.outfp.write(text_bytes)
