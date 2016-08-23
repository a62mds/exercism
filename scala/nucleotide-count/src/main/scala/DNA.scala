import scalaz.Scalaz._

class DNA(val mSeq: String) {

  type DNASeq = String
  type Count = Int
  type Nucleotide = Char
  type NucleotideCount = Map[Nucleotide, Count]

  val validNucleotides: Set[Nucleotide] = Set('A', 'T', 'C', 'G')
  val isValidDNASeq: Boolean = mSeq.forall(validNucleotides.contains(_))

  require(isValidDNASeq, s"Invalid DNA sequence: $mSeq")

  lazy val nucleotideCounts: NucleotideCount = {
    val init: NucleotideCount = validNucleotides.map(nucl => nucl -> 0).toMap
    val seqCount: NucleotideCount = mSeq.groupBy(identity).mapValues(_.size)
    init |+| seqCount
  }

}
