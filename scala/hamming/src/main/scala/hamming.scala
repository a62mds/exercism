object Hamming {

  type Nucleotide = Char
  type DNASeq = Seq[Nucleotide]

  def compute(seq1: DNASeq, seq2: DNASeq): Int = {
    require(seq1.length==seq2.length, "Sequences not the same length")
    seq1.zip(seq2).count({ case (nucl1, nucl2) => nucl1 != nucl2 })
  }

}
