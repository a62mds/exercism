import java.util.Arrays;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class InvalidNucleotideException extends IllegalArgumentException {
  public InvalidNucleotideException(Character n) {
    super("Encountered invalid nucleotide: " + n);
  }
}

public class DNA {
  private final char[] _nucleotides = {'A', 'C', 'T', 'G'};
  private String _sequence;
  private Map<char, int> _count;
  public DNA(String sequence) {
    try {
      this.initCount();
      this.setSequence(sequence);
      this.countSequence();
    } catch (InvalidNucleotideException e) {
      e.printStackTrace();
    }
  }
  public void setSequence(String sequence) throws InvalidNucleotideException {
    this._sequence = "";
    for (int ii=0; ii < sequence.length(); ii++) {
      char c = sequence.charAt(ii);
      if (Arrays.asList(this._nucleotides).contains(c)) {
        this._sequence += c;
      } else {
        throw new InvalidNucleotideException(c);
      }
    }
  }
  public String getSequence() {
    return this._sequence;
  }
  public Integer count(Character nucleotide) throws InvalidNucleotideException {
    if (this._count.containsKey(nucleotide)) {
      return this._count.get(nucleotide);
    } else {
      throw new InvalidNucleotideException(nucleotide);
    }
  }
  public Map<Character, Integer> nucleotideCounts() {
    return this._count;
  }
  private void initCount() {
    for (int ii=0; ii<this._nucleotides.length; ii++) {
      this._count.put(this._nucleotides[ii], 0);
    }
  }
  private void countSequence() {
    for (int ii=0; ii < this._sequence.length(); ii++) {
      char n = this._sequence.charAt(ii);
      this._count.put(n, this._count.get(n) + 1);
    }
  }

  public static void main(String[] args) {
    DNA dna = new DNA("A");

  }
}
