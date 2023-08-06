from typing import List, Optional, Type, cast
from xml.etree.ElementTree import Element, parse

from py_pdf_term.pdftoxml import PDFnXMLElement, PDFnXMLPath
from py_pdf_term.tokenizers import BaseLanguageTokenizer, Term, Token, Tokenizer

from .augmenters import AugmenterCombiner, BaseAugmenter
from .classifiers import BaseTokenClassifier, MeaninglessMarker
from .data import DomainCandidateTermList, PageCandidateTermList, PDFCandidateTermList
from .filters import BaseCandidateTermFilter, BaseCandidateTokenFilter, FilterCombiner
from .splitters import BaseSplitter, SplitterCombiner
from .utils import textnode_fontsize, textnode_ncolor, textnode_text


class CandidateTermExtractor:
    """A term extractor which extracts candidate terms from a XML file.

    Args
    ----
        lang_tokenizer_clses:
            A list of language tokenizer classes to tokenize texts. If None, the default
            language tokenizers are used.

        token_classifier_clses:
            A list of token classifier classes to classify tokens. If None, the default
            token classifiers are used.

        token_filter_clses:
            A list of token filter classes to filter tokens. If None, the default token
            filters are used.

        term_filter_clses:
            A list of term filter classes to filter candidate terms. If None, the
            default term filters are used.

        splitter_clses:
            A list of splitter classes to split candidate terms. If None, the default
            splitters are used.

        augmenter_clses:
            A list of augmenter classes to augment candidate terms. If None, the default
            augmenters are used.
    """

    def __init__(
        self,
        lang_tokenizer_clses: Optional[List[Type[BaseLanguageTokenizer]]] = None,
        token_classifier_clses: Optional[List[Type[BaseTokenClassifier]]] = None,
        token_filter_clses: Optional[List[Type[BaseCandidateTokenFilter]]] = None,
        term_filter_clses: Optional[List[Type[BaseCandidateTermFilter]]] = None,
        splitter_clses: Optional[List[Type[BaseSplitter]]] = None,
        augmenter_clses: Optional[List[Type[BaseAugmenter]]] = None,
    ) -> None:
        lang_tokenizers = (
            list(map(lambda cls: cls(), lang_tokenizer_clses))
            if lang_tokenizer_clses is not None
            else None
        )
        self._tokenizer = Tokenizer(lang_tokenizers=lang_tokenizers)

        token_filters = (
            list(map(lambda cls: cls(), token_filter_clses))
            if token_filter_clses is not None
            else None
        )
        term_filters = (
            list(map(lambda cls: cls(), term_filter_clses))
            if term_filter_clses is not None
            else None
        )
        self._filter = FilterCombiner(token_filters, term_filters)

        classifiers = (
            list(map(lambda cls: cls(), token_classifier_clses))
            if token_classifier_clses is not None
            else None
        )
        self._marker = MeaninglessMarker(classifiers)

        splitters = (
            list(map(lambda cls: cls(classifiers), splitter_clses))
            if splitter_clses is not None
            else None
        )
        self._splitter = SplitterCombiner(splitters)

        augmenters = (
            list(map(lambda cls: cls(), augmenter_clses))
            if augmenter_clses is not None
            else None
        )
        self._augmenter = AugmenterCombiner(augmenters)

    def extract_from_domain_files(
        self, domain: str, pdfnxmls: List[PDFnXMLPath]
    ) -> DomainCandidateTermList:
        """Extract candidte terms from pairs of PDF and XML files in a domain.

        Args
        ----
            domain:
                A domain name of PDF files.
            pdfnxmls:
                A list of pairs of paths to PDF and XML files in a domain.

        Returns
        -------
            DomainCandidateTermList:
                A list of candidate terms in a domain.
        """

        xmls = list(map(self.extract_from_xml_file, pdfnxmls))
        return DomainCandidateTermList(domain, xmls)

    def extract_from_xml_file(self, pdfnxml: PDFnXMLPath) -> PDFCandidateTermList:
        """Extract candidate terms from a pair of PDF and XML files.

        Args
        ----
            pdfnxml:
                A pair of paths to a PDF and XML file.

        Returns
        -------
            PDFCandidateTermList:
                A list of candidate terms in a PDF file.
        """

        xml_root = parse(pdfnxml.xml_path).getroot()
        xml_candidates = self._extract_from_xmlroot(pdfnxml.pdf_path, xml_root)
        return xml_candidates

    def extract_from_domain_elements(
        self, domain: str, pdfnxmls: List[PDFnXMLElement]
    ) -> DomainCandidateTermList:
        """Extract candidate terms from pairs of PDF and XML elements in a domain.

        Args
        ----
            domain:
                A domain name of PDF files.
            pdfnxmls:
                A list of pairs of paths to PDF and XML elements in a domain.

        Returns
        -------
            DomainCandidateTermList:
                A list of candidate terms in a domain.
        """

        xmls = list(map(self.extract_from_xml_element, pdfnxmls))
        return DomainCandidateTermList(domain, xmls)

    def extract_from_xml_element(self, pdfnxml: PDFnXMLElement) -> PDFCandidateTermList:
        """Extract candidate terms from a pair of PDF and XML elements.

        Args
        ----
            pdfnxml:
                A pair of path to a PDF and XML elements.

        Returns
        -------
            PDFCandidateTermList:
                A list of candidate terms in a PDF file.
        """

        xml_candidates = self._extract_from_xmlroot(pdfnxml.pdf_path, pdfnxml.xml_root)
        return xml_candidates

    def extract_from_text(
        self, text: str, fontsize: float = 0.0, ncolor: str = ""
    ) -> List[Term]:
        """Extract candidate terms from a text. This method is mainly used for testing.

        Args
        ----
            text:
                A text to extract candidate terms.
            fontsize:
                A font size of output terms.
            ncolor:
                A color of output terms.

        Returns
        -------
            List[Term]:
                A list of candidate terms in a text.
        """

        tokens = self._tokenizer.tokenize(text)
        return self._extract_from_tokens(tokens, fontsize, ncolor)

    def _extract_from_xmlroot(
        self, pdf_path: str, xml_root: Element
    ) -> PDFCandidateTermList:
        page_candidates: List[PageCandidateTermList] = []
        for page in xml_root.iter("page"):
            page_candidates.append(self._extract_from_page(page))

        return PDFCandidateTermList(pdf_path, page_candidates)

    def _extract_from_page(self, page: Element) -> PageCandidateTermList:
        page_num = int(cast(str, page.get("id")))

        candicate_terms: List[Term] = []
        for textnode in page.iter("text"):
            text = textnode_text(textnode)
            fontsize = textnode_fontsize(textnode)
            ncolor = textnode_ncolor(textnode)
            tokens = self._tokenizer.tokenize(text)
            terms = self._extract_from_tokens(tokens, fontsize, ncolor)
            candicate_terms.extend(terms)

        return PageCandidateTermList(page_num, candicate_terms)

    def _extract_from_tokens(
        self, tokens: List[Token], fontsize: float, ncolor: str
    ) -> List[Term]:
        candicate_terms: List[Term] = []
        candicate_tokens: List[Token] = []
        for idx, token in enumerate(tokens):
            if self._filter.is_partof_candidate(tokens, idx):
                candicate_tokens.append(token)
                continue

            terms = self._terms_from_tokens(candicate_tokens, fontsize, ncolor)
            candicate_terms.extend(terms)
            candicate_tokens = []

        terms = self._terms_from_tokens(candicate_tokens, fontsize, ncolor)
        candicate_terms.extend(terms)

        return candicate_terms

    def _terms_from_tokens(
        self, candicate_tokens: List[Token], fontsize: float, ncolor: str
    ) -> List[Term]:
        candidate_term = Term(candicate_tokens, fontsize, ncolor)

        candicate_terms: List[Term] = []
        splitted_candidates = self._splitter.split(candidate_term)
        for splitted_candidate in splitted_candidates:
            augmented_candidates = self._augmenter.augment(splitted_candidate)
            candicate_terms.extend(augmented_candidates)
            candicate_terms.append(splitted_candidate)

        return list(
            map(self._marker.mark, filter(self._filter.is_candidate, candicate_terms))
        )
