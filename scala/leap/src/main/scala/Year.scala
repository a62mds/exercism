object Year { def apply(aYear: Int) = new Year(aYear) }

class Year(mYear: Int) {
  // Predicate: y => (4|y ^ (100|y -> 400|y))
  // Using P -> Q <-> ~P v Q, rewrite predicate as
  //            y => (4|y ^ (~100|y v 400|y))
  def isLeap: Boolean = 
    divides(4, mYear) && (!divides(100, mYear) || divides(400, mYear))

  def divides(denom: Int, numer: Int): Boolean = numer % denom == 0
}