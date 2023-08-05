# AUTOGENERATED FILE! PLEASE DON'T EDIT
"""
This is for functions that are actually biology-related
"""
from k1lib.cli.init import BaseCli
import k1lib; import k1lib.cli as cli
import os; from functools import partial
from typing import Iterator, Union
__all__ = ["go", "quality", "longFa", "idx",
           "transcribe", "complement", "translate", "medAa", "longAa"]
settings = k1lib.Settings()
k1lib.settings.cli.add("bio", settings, "from k1lib.cli.bio module");
def _patchDir(term, s, p):
    if p != None: p = os.path.abspath(os.path.expanduser(p))
    s.__dict__[term] = p
settings.add("blast", None, "location of BLAST database", partial(_patchDir, "blast"))
settings.add("go", None, "location of gene ontology file (.obo)", partial(_patchDir, "go"))
settings.add("so", None, "location of sequence ontology file", partial(_patchDir, "so"));
settings.add("lookupImgs", True, "sort of niche. Whether to auto looks up extra gene ontology relationship images")
def go(term:int):
    """Looks up a GO term"""
    if settings.go is None and not os.path.exists("go.obo"):
        answer = input("""No gene ontology obo file specified! You can:
- Specify the file using `settings.cli.bio.go = '/some/folder/go.obo'`
- Download this automatically to file `go.obo`

You want to download this automatically? (y/n) """)
        if answer.lower().startswith("y"):
            url = "http://current.geneontology.org/ontology/go.obo"
            print(f"Downloading from {url}...      ", end="")
            cli.wget(url); print("Finished!")
        else: return print("Aborted")
    file = settings.go or "go.obo"; term = f"{term}".rjust(7, "0")
    cli.cat(file) | cli.grep(f"id: GO:{term}", 0, 10) > cli.stdout()
    print(f"https://www.ebi.ac.uk/QuickGO/GTerm?id=GO:{term}")
    if settings.lookupImgs:
        class Repr:
            def _repr_html_(self):
                return f"""<img src="http://amigo.geneontology.org/visualize?mode=amigo&term_data_type=string&format=png&inline=false&term_data=GO%3A{term}" />"""
        return Repr()
settings.add("phred", """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJ""", "Phred quality score")
class toIdx(BaseCli):
    def __init__(self, chars:str): self.chars = {v:k for k, v in enumerate(chars)}
    def __ror__(self, it):
        chars = self.chars
        for e in it: yield chars[e]
def quality(log=True):
    """Get numeric quality of sequence.
Example::

    # returns [2, 2, 5, 30]
    "##&?" | quality() | deref()

:param log: whether to use log scale (0 -> 40), or linear scale (1 -> 0.0001)"""
    if log: return toIdx(settings.phred)
    else: return toIdx(settings.phred) | cli.apply(lambda x: 10**(-x/10))
def longFa():
    """Takes in a fasta file and put each sequence on 1 line.
File "gene.fa"::

    >AF086833.2 Ebola virus - Mayinga, Zaire, 1976, complete genome
    CGGACACACAAAAAGAAAGAAGAATTTTTAGGATC
    TTTTGTGTGCGAATAACTATGAGGAAGATTAATAA
    >something other gene
    CGGACACACAAAAAGAAAGAAGA
    TTTTGTGTGCGAATAACTATGAG

Code::

    cat("gene.fa") | bio.longFa() | cli.headOut()

Prints out::

    >AF086833.2 Ebola virus - Mayinga, Zaire, 1976, complete genome
    CGGACACACAAAAAGAAAGAAGAATTTTTAGGATCTTTTGTGTGCGAATAACTATGAGGAAGATTAATAA
    >something other gene
    CGGACACACAAAAAGAAAGAAGATTTTGTGTGCGAATAACTATGAG"""
    return cli.grep("^>", sep=True).till() | (cli.item() & (~cli.head(1) | cli.join(""))).all() | cli.joinStreams()
def _fileWithoutExt(f): return ".".join(f.split(".")[:-1])
class idx(BaseCli):
    """Indexes files with various formats."""
    @staticmethod
    def blast(fileName:str=None, dbtype:str=None):
        """Uses ``makeblastdb`` to create a blast database from a fasta file.
Example::

    "file.fa" | bio.idx.blast()
    bio.idx.blast("file.fa")"""
        f = cli.applyS(lambda fileName: None | cli.cmd(f"makeblastdb -dbtype {dbtype or 'nucl'} -in {fileName} -out {_fileWithoutExt(fileName)}"))
        return f if fileName is None else f(fileName)
    @staticmethod
    def bwa(fileName:str=None):
        """Uses ``bwa`` to index a fasta file.
Example::

    "file.fa" | bio.idx.bwa()
    bio.idx.bwa("file.bwa")"""
        f = cli.applyS(lambda fileName: None | cli.cmd(f"bwa index {fileName}"))
        return f if fileName is None else f(fileName)
    @staticmethod
    def bam(fileName:str=None):
        """Uses ``samtools`` to index a bam file.
Example::

    "file.bam" | bio.idx.bam()
    bio.idx.bam("file.bam")"""
        f = cli.applyS(lambda fileName: None | cli.cmd(f"samtools index {fileName}"))
        return f if fileName is None else f(fileName)
class transcribe(BaseCli):
    """Transcribes (DNA -> RNA) incoming rows.
Example::

    # returns "AUCG"
    "ATCG" | transcribe()
    # returns ["AUCG"]
    ["ATCG"] | transcribe() | deref()"""
    def __ror__(self, it:Union[Iterator[str], str]):
        if isinstance(it, str): return [it] | self | cli.item()
        return (line.upper().replace("T", "U") for line in it)
class complement(BaseCli):
    """Get the reverse complement of DNA.
Example::

    # returns "TAGC"
    "ATCG" | bio.complement()
    # returns ["TAGC"]
    ["ATCG"] | bio.complement() | deref()"""
    def __ror__(self, it:Union[Iterator[str], str]):
        if isinstance(it, str): return [it] | self | cli.item()
        return (line.upper().replace("A", "0").replace("T", "A").replace("0", "T").upper().replace("C", "0").replace("G", "C").replace("0", "G") for line in it)
ntAa = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
        "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",

        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",

        "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",

        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}
_shortAa = {v:v for v in ntAa.values()}
_medAa = {
    "F": "Phe", "L": "Leu", "I": "Ile", "M": "Met", "V": "Val",
    "S": "Ser", "P": "Pro", "T": "Thr", "A": "Ala", "Y": "Tyr",
    "*": "Stop", "H": "His", "Q": "Gln", "N": "Asn", "K": "Lys",
    "D": "Asp", "E": "Glu", "C": "Cys", "W": "Trp", "R": "Arg",
    "G": "Gly", "U": "Sec", "?": "?"
}
_longAa = {
    "F": "Phenylalanine", "L": "Leucine", "I": "Isoleucine", "M": "Methionine", "V": "Valine",
    "S": "Serine", "P": "Proline", "T": "Threonine", "A": "Alanine", "Y": "Tyrosine",
    "*": "Stop", "H": "Histidine", "Q": "Glutamine", "N": "Asparagine", "K": "Lysine",
    "D": "AsparticAcid", "E": "GlutamicAcid", "C": "Cysteine", "W": "Tryptophan", "R": "Arginine",
    "G": "Glycine", "U": "Selenocysteine", "?": "?"
}
class translate(BaseCli):
    def __init__(self, length:int=0):
        """Translates incoming rows.

:param length: 0 for short (L), 1 for med (Leu), 2 for long (Leucine)"""
        super().__init__(); self.delim = "" if length == 0 else " "
        self.dict = [_shortAa, _medAa, _longAa][length]
    def __ror__(self, it:Iterator[str]):
        super().__ror__(it)
        if isinstance(it, str): it = [it]
        it = it | transcribe()
        for line in it:
            line = line.replace(" ", "")
            answer = ""; n = len(line)
            for i in range(0, n - n % 3, 3):
                codon = line[i:i+3].upper()
                answer += (self.dict[ntAa[codon]] if codon in ntAa else "?") + self.delim
            yield answer
class medAa(BaseCli):
    """Converts short aa sequence to medium one"""
    def __ror__(self, it:Iterator[str]):
        if isinstance(it, str): it = [it]
        for line in it:
            yield " ".join(_medAa[c] for c in line)
class longAa(BaseCli):
    """Converts short aa sequence to long one"""
    def __ror__(self, it:Iterator[str]):
        if isinstance(it, str): it = [it]
        for line in it:
            yield " ".join(_longAa[c] for c in line)