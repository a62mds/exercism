#include "rna_transcription.h"

namespace rna_transcription {
    char to_rna(char nucleotide) {
        switch (nucleotide) {
            case 'G': return 'C';
            case 'C': return 'G';
            case 'T': return 'A';
            case 'A': return 'U';
            default:  return '-';
        }
    }
    std::string to_rna(std::string dna_seq) {
        std::string rna_seq;
        for (std::string::const_iterator nucleotide=dna_seq.begin(); nucleotide != dna_seq.end(); ++nucleotide) {
            rna_seq.push_back(to_rna(*nucleotide));
        }
        return rna_seq;
    }
}  // namespace rna_transcription
